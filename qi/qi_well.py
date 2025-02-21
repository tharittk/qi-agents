import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from welly import Well
from  enum import Enum


class FaciesColor(Enum):
    shale = 'grey'
    brine = 'skyblue'
    gas = 'firebrick'
    oil = 'green'
    coal = 'black'
    _gas = 'red'
    _brine = 'blue'
    _oil = 'green',
    hc_others = 'pink',
    dirty_sand = 'orange'  # later to change
    _invalid_sand = 'yellow' # later changed

def get_facies_color(facies):
    return FaciesColor[facies].value

# Litho mapping (well mapping stays explicit in data loader)
cfg_arthit = {}
cfg_g161 = {}
cfg_bongkot = {}

class QIWell:

    def __init__(self, well_name, las_path, remap):
        """Initialize with well data and default values."""
        self.well_name = well_name
        self.X = 0
        self.Y = 0
        self.KB = 0
        self.step = 0
        self.step_unit = 'm'
        self.is_up_scaled = False
        self.litho_config = None

        self.top_name = np.array([], dtype=str)
        self.top_depth = np.array([], dtype=float)
        self.Dev = pd.DataFrame(columns=['MD', 'X', 'Y', 'TVD', 'TVDSS'])
        self._read_las_file_to_dataframe(las_path, remap)
        self.unit_tag = "whole"
    
    def __repr__(self):
        return f"QIWell(name={self.well_name})"
    def set_facies_config(self, field_name):
        self.litho_config = field_name
    
    def _read_las_file_to_dataframe(self, las_path, remap):
        well = Well.from_las(las_path)
        depth_col = list(well.data.keys())[0]
        df = well.df(basis=well.data[depth_col].basis).reset_index()

        log = pd.DataFrame()
        if remap:
            log = df[list(remap.keys())].rename(columns=remap)

        # Replace NaNs in FLUID log with shale values (0)
        if 'FLUID' in remap.values():
            log['FLUID'] = log['FLUID'].replace(np.nan, 0)

        self.NaNLog = log.copy().replace(np.nan, 0)
        #self.Log = log.dropna()
        # Coal issue. Some log fails - THIS Remains to be tested when shale == 0
        # You may run into the issue where all nan value is marked as 'shale'
        self.Log = log.copy().replace(np.nan, 0)

    def load_geological_tops(self, top_path, col_name, col_depth, separator, n_header):
        """
        Load geological tops/markers from a file and store them in the top_name and top_depth attributes.
        """
        self.top_name = np.loadtxt(top_path, skiprows=n_header, delimiter=separator, dtype=str, usecols=[col_name - 1])
        top_depth = np.loadtxt(top_path, skiprows=n_header, delimiter=separator, usecols=[col_depth - 1])
        self.top_depth = np.concatenate([[top_depth, top_depth]])  # MD and TVDSS

        self._process_all_logs_with_top()

    def _process_all_logs_with_top(self):
        """
        Process top markers into both NaNLog and Log.
        """
        for log_df, to_nan_log in [(self.NaNLog, True), (self.Log, False)]:
            self._map_top_markers(log_df, to_nan_log)
        self._convert_top_to_tvdss()

    def _map_top_markers(self, log, to_nan_log):
        """
        Map top markers to the log data.
        """
        depth = log[log.columns[0]]
        top_log = np.full(len(depth), 'Shallow', dtype=object)

        for i, top_name in enumerate(self.top_name):
            top_log[depth > self.top_depth[0][i]] = top_name

        self.add_log('Unit', top_log, to_nan_log)

    def add_log(self, log_name, new_log, to_nan_log = False):
        """Add a new log to either the NaNLog or Log dataframe."""
        if to_nan_log:
            self.NaNLog[log_name] = new_log
        else:
            self.Log[log_name] = new_log

    def _convert_top_to_tvdss(self):
        """
        Convert MD top depths to TVDSS based on the well's deviation survey.
        """
        self.top_depth[1] = np.interp(self.top_depth[0], self.Dev['MD'], self.Dev['TVDSS'])

    def load_deviation(self, dev_path, KB, col_MD, col_X, col_Y, col_TVD, separator, n_header, preview=False):
        """
        Load the deviation survey from a file, store it, and optionally display a preview.
        """
        self.KB = KB
        raw_dev = np.loadtxt(dev_path, delimiter=separator, skiprows=n_header)
        self.Dev['MD'] = raw_dev[:, col_MD - 1]
        self.Dev['X'] = raw_dev[:, col_X - 1]
        self.Dev['Y'] = raw_dev[:, col_Y - 1]
        self.Dev['TVD'] = raw_dev[:, col_TVD - 1]
        self.Dev['TVDSS'] = self.Dev['TVD'] - self.KB

        if preview:
            self._preview_deviation_survey()

        self._insert_tvdss_log()

    def _insert_tvdss_log(self):
        """
        Insert TVDSS values into Log and NaNLog using deviation survey interpolation.
        """
        tvdss_interp = np.interp(self.Log['MD'], self.Dev['MD'], self.Dev['TVD'])
        tvdss_interp_nan = np.interp(self.NaNLog['MD'], self.Dev['MD'], self.Dev['TVD'])

        self.NaNLog.insert(loc=1, column='TVDSS', value=tvdss_interp_nan)
        self.Log.insert(loc=1, column='TVDSS', value=tvdss_interp)

    def preprocess_acoustic_logs(self):
        self._add_velocity_and_density_logs()
        self._compute_and_add_ai_log()
        self._compute_and_add_vpvs_log()
        self._combine_litho_and_fluid_to_facies_log()

    def _add_velocity_and_density_logs(self):
        """
        Compute and add velocity (Vp, Vs) and density (RHOB) related logs.
        """
        self._assert_log_columns(['DTC', 'DTS'])
        ft_per_m = 0.3048
        us = 1e-6
        self.add_log('Vp', (1 / self.Log['DTC']) * (ft_per_m / us))
        self.add_log('Vs', (1 / self.Log['DTS']) * (ft_per_m / us))

    def _assert_log_columns(self, required_columns):
        """
        Ensure that all required logs are present.
        """
        for column in required_columns:
            if column not in self.Log.columns:
                raise ValueError(f"Log '{column}' not found in well logs.")

    def _compute_and_add_ai_log(self):
        self.add_log('AI', self.Log['RHOB'] * self.Log['Vp'])

    def _compute_and_add_vpvs_log(self):
        self.add_log('Vp/Vs', self.Log['Vp'] / self.Log['Vs'])

    def _combine_litho_and_fluid_to_facies_log(self):
        """
        Combine the lithology log (LITHOLOGY) (sand, shale, coal, etc.) and fluid log (FLUID)
        and create a new log (Lithology) that has 5 facies: shale, brine, gas, coal, and hc_others
        """
        self._assert_log_columns(['LITHO', 'FLUID'])
        match self.litho_config:
            case "Arthit":
                conditions = [
                    (self.Log['LITHO'] == 0), # shale
                    (self.Log['LITHO'] == 1) & (self.Log['FLUID'] == 0), # brine
                    (self.Log['LITHO'] == 1) & (self.Log['FLUID'] == 4), # gas
                    (self.Log['LITHO'] == 99) & (self.Log['FLUID'] == 99), # oil
                    (self.Log['LITHO'] == 2), # coal
                    (self.Log['FLUID'] >= 5) # hc_others
                ]
            
            case "Bongkot":
                conditions = [ # TO BE UPDATED
                    (self.Log['LITHO'] == 0), # shale
                    (self.Log['LITHO'] == 1) & (self.Log['FLUID'] == 0), # brine
                    (self.Log['LITHO'] == 1) & (self.Log['FLUID'] == 4), # gas
                    (self.Log['LITHO'] == 99) & (self.Log['FLUID'] == 99), # oil
                    (self.Log['LITHO'] == 2), # coal
                    (self.Log['FLUID'] >= 5) # hc_others
                ]
            case "G161":
                conditions = [ # TO BE UPDATED
                    (self.Log['LITHO'] == 1), # shale
                    (self.Log['LITHO'] == 2) & (self.Log['FLUID'] == 1), # brine
                    (self.Log['LITHO'] == 2) & (self.Log['FLUID'] == 2), # gas
                    (self.Log['LITHO'] == 2) & (self.Log['FLUID'] == 3), # oil
                    (self.Log['LITHO'] == 3), # coal
                    (self.Log['FLUID'] >= 4) # hc_others
                ]      


        facies = ['shale', 'brine', 'gas', 'oil', 'coal', 'hc_others']
        self.add_log('Facies', np.select(conditions, facies, default='shale'))
