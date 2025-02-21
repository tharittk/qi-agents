
import numpy as np
import matplotlib.pyplot as plt
import rockphypy

from copy import deepcopy
from .qi_well import *

LogColor = {
    "RHOB" :'darkorange',
    "PHIE" : 'skyblue',
    "Sw" : 'blue',
    "DTC" : 'green',
    "DTS" : 'darkgreen',
    "Vsh" : 'grey',
    "FLUID" : 'black',
    "LITHO" : 'grey',
    "Unit" : 'blue',
    "Facies": 'firebrick',
}


def extract_log_interval_by_unit(well: QIWell, unit: str) -> QIWell:
    new_well = deepcopy(well)
    new_well.Log = new_well.Log[new_well.Log['Unit'] == unit]
    new_well.unit_tag = unit
    
    return new_well

def extract_log_interval_by_depth(well: QIWell, min_depth: float, max_depth: float
                                  , depth_col: str):
    new_well = deepcopy(well)
    new_well.Log = new_well.Log[(new_well.Log[depth_col] >= min_depth) & (new_well.Log[depth_col] <= max_depth)]
    new_well.unit_tag = f'by_depth_{min_depth}-{max_depth}_m_{depth_col}'
    return new_well

def plot_logs(well: QIWell, log_list: list[str], depth_col: str, save_fig=False):
    n_log = len(log_list)

    width = 2 * n_log
    height = 10
    fig = plt.figure(figsize=(width, height))
    for i, log_name in enumerate(log_list):
        ax = fig.add_subplot(1, n_log, i + 1)
        
        clr = LogColor[log_name] if log_name in LogColor else "skyblue"

        ax.plot(well.Log[log_name], well.Log[depth_col], 
                c=clr)
            
        ax.set_xlabel(log_name, fontsize=16)
        ax.xaxis.set_label_position('top')

        ax.set_ylim(ax.get_ylim()[::-1])
        ax.tick_params(axis="y", labelsize=0)
            
        ax.grid()

        if i == 0:
            ax.set_ylabel(depth_col, fontsize=16)
            ax.tick_params(axis="y", labelsize=11)


    fig.suptitle(f"{well.well_name} {log_list} in {depth_col}", fontsize=20)
    fig.subplots_adjust(top=0.9)

    if save_fig:
        fig_name = f"{well.well_name}_custom_logs_{depth_col}"
        file_name = f"./img/{fig_name}"
        fig.savefig(file_name)
        return file_name

def plot_crossplot_insitu(well: QIWell, x_attr: str, y_attr: str, facies_list: list[str], save_fig=False):

    fig, ax = plt.subplots(1, 1, sharey=True)

    for facies in facies_list:
        # Possible when restrict to in-situ fluid
        facies_log = np.array(well.Log['Facies'])

        xx = np.array(well.Log[x_attr])[facies_log == facies].flatten()
        yy = np.array(well.Log[y_attr])[facies_log == facies].flatten()

        ax.scatter(xx, yy, c=get_facies_color(facies), s=5, label=f":{facies}")

    if x_attr.startswith("AI") and y_attr.startswith("Vp/Vs"):
        ax.set_xlim([4000, 14000])  # AI min, AI max
        ax.set_ylim([1.45, 2.1])  # Vp/Vs min, Vp/Vs max
    
    xunit = ' (g/cm3 * m/s)' if x_attr.startswith('AI') else ' --unit--'

    ax.set_title(f"Xplot {x_attr} vs. {y_attr} || Unit: {well.unit_tag}")
    ax.set_xlabel(f"{x_attr} {xunit}")
    ax.set_ylabel(f"{y_attr} --unit--")

    ax.legend()

    if save_fig:
        fig_name = f"{well.well_name}_xplot_{well.unit_tag}"
        file_name = f"./img/{fig_name}"
        fig.savefig(file_name)
        return file_name

def plot_crossplot_fluid_sub(well: QIWell, x_attr: str, y_attr: str, facies_list: list[str], save_fig=False):
    # Preprocess for symbolic alignment (adding "_")
    facies_list = _preprocess_facies_list_for_fluid_sub(facies_list) 

    fig, ax = plt.subplots(1, 1, sharey=True)

    for facies in facies_list:
        # Fluid-substituted specific logs
        if facies.startswith("_"):
            facies_log = np.array(well.Log['Facies' + facies])

        else:
            facies_log = np.array(well.Log['Facies'])

        if x_attr in ["AI", "Vp/Vs", "Vp", "Vs", "RHOB"] and facies.startswith("_"):
            x_attr_plot = x_attr + facies
        else:
            x_attr_plot = x_attr

        if y_attr in ["AI", "Vp/Vs", "Vp", "Vs", "RHOB"] and  facies.startswith("_"):
            y_attr_plot = y_attr + facies
        else:
            y_attr_plot = y_attr

        xx = np.array(well.Log[x_attr_plot])[facies_log == facies].flatten()
        yy = np.array(well.Log[y_attr_plot])[facies_log == facies].flatten()

        ax.scatter(xx, yy, c=get_facies_color(facies), s=5, label=f":{facies}")

    if x_attr.startswith("AI") and y_attr.startswith("Vp/Vs"):
        ax.set_xlim([4000, 14000])  # AI min, AI max
        ax.set_ylim([1.45, 2.1])  # Vp/Vs min, Vp/Vs max
    
    ax.set_title(f"Xplot (Sub) {x_attr} vs. {y_attr} || Unit: {well.unit_tag}")
    ax.set_xlabel(f"{x_attr} --unit--")
    ax.set_ylabel(f"{y_attr} --unit--")

    ax.legend()

    if save_fig:
        fig_name = f"{well.well_name}_xplot_fluid_sub_{well.unit_tag}"
        file_name = f"./img/{fig_name}"
        fig.savefig(file_name)
        return file_name

def substitute_fluid(well: QIWell, hc_type: str, hc_sat: float, vsh_cut=0.2, mod_Sw=True) -> QIWell:

    Kwater = 2.5e9
    rhowater = 1.0e3
    Kmineral=36.6e9
    
    if hc_type == "brine":
        # do it by substitute 0% gas
        hc_sat = 0.0
        rhohc, Khc = _get_hydrocarbon_properties("gas")

    else:
        rhohc, Khc = _get_hydrocarbon_properties(hc_type)

    vp_log = well.Log['Vp']
    vs_log = well.Log['Vs']
    rhob_log = well.Log['RHOB'] * 1000

    # Preconditioning Sw
    if mod_Sw:
        Sw_mod = well.Log['Sw'].copy()
        Sw_mod.loc[well.Log['Facies'] == 'brine'] = 0.999
        sw_log = np.clip(Sw_mod, 0.001, 0.999) # Reduce spikes

    else:
        sw_log = well.Log['Sw']

    phie = well.Log['PHIE']

    # Mixing process
    rhofl_inst = sw_log * rhowater + (1-sw_log) * rhohc
    Kfl_inst = 1/ ( (sw_log/Kwater) + ((1 - sw_log)/Khc))

    sat_target = np.ones(sw_log.shape) * hc_sat
    rhofl_target = (1-sat_target) * rhowater + sat_target * rhohc
    Kfl_target = 1/( ((1-sat_target)/Kwater) + (sat_target/Khc))

    vp2_log, vs2_log = rockphypy.Fluid.Gassmann_vels(vp_log, vs_log, rhob_log, rhofl_inst, Kfl_inst,
                                               rhofl_target, Kfl_target, Kmineral, phie)

    # clean sand condition
    sand_identity_log = _get_sand_identity_log(well, vsh_cut)

    vp_log_target = sand_identity_log * vp2_log + (~sand_identity_log) * vp_log
    vs_log_target = sand_identity_log * vs2_log + (~sand_identity_log) * vs_log
    rhob_log_target = (rhob_log - (phie * rhofl_inst) + (phie * rhofl_target)) / 1000

    well_sub = deepcopy(well)

    # use "_" to signifies substituted fluid
    well_sub = _add_fluid_sub_logs(well_sub, vp_log_target, vs_log_target, 
                        rhob_log_target, sand_identity_log,  "_" + hc_type)


    return well_sub

def _get_hydrocarbon_properties(hc_type):
    if hc_type == 'gas':
        return 0.15e3, 0.038e9  # gas properties
    elif hc_type == 'oil':
        return 0.83e3, 1.15e9  # oil properties
    else:
        raise ValueError("Invalid hydrocarbon type. Expected 'gas' or 'oil'.")

def _get_sand_identity_log(well, vsh_cut):
    facies_mask = (well.Log['Facies'].isin(['brine', 'gas', 'oil']))
    Vsh_mask = (well.Log['Vsh'] <= vsh_cut)

    return facies_mask & Vsh_mask

def _add_fluid_sub_logs(well, vp_log, vs_log, rhob_log, sand_identity_log, suffix):
        ai_log = vp_log * rhob_log
        vpvs_log = vp_log / vs_log

        vp_col = 'Vp' + suffix
        vs_col = 'Vs' + suffix
        rhob_col = 'RHOB' + suffix
        ai_col = 'AI' + suffix
        vpvs_col = 'Vp/Vs' + suffix
        facies_col = 'Facies' + suffix

        # Add Vp_gas, for example
        well.add_log(vp_col, vp_log)
        well.add_log(vs_col, vs_log)
        well.add_log(rhob_col, rhob_log)
        well.add_log(ai_col, ai_log)
        well.add_log(vpvs_col, vpvs_log)
        
        # pre-process facies log
        tmp1 = well.Log['Facies'].copy()
        tmp2 = pd.Series(tmp1).replace('brine', 'dirty_sand')
        tmp3 = pd.Series(tmp2).replace('gas', 'dirty_sand')
        tmp4 = pd.Series(tmp3).replace('oil', 'dirty_sand')

        well.add_log(facies_col, tmp4)
        
        well.Log.loc[sand_identity_log, facies_col] = suffix

        # _gas sand after fluid substitution must have Vp/Vs in range (1.41, 2.0)
        condition = ((well.Log[vpvs_col] < 1.41) | (well.Log[vpvs_col] > 2.0)) & (well.Log[facies_col] == '_gas')

        well.Log.loc[condition, facies_col] = '_invalid_sand'

        return well


def _preprocess_facies_list_for_fluid_sub(facies_list):
    # Preprocess for symbolic alignment (adding "_")
    tmp = []
    for facies in facies_list:
        if facies in ["gas", "oil", "brine"]:
            tmp.append("_" + facies)
        else:
            tmp.append(facies)
    
    return tmp

# Compute and plot
def compute_facies_separation_fluid_sub(well, log_name, facies_list, save_fig=False):
    # Preprocess for symbolic alignment (adding "_")
    facies_list = _preprocess_facies_list_for_fluid_sub(facies_list) 

    gnb_list = []
    log_list = []

    for label, facies in enumerate(facies_list):
        # for condiational data extraction
        if facies.startswith("_"):
            facies_log = np.array(well.Log['Facies' + facies])
        else:
            facies_log = np.array(well.Log['Facies'])

        # select fluid_sub log if the property was changed by fluid substitution
        if log_name in ["AI", "Vp/Vs", "Vp", "Vs", "RHOB"] and facies.startswith("_"):
            log_name_target = log_name + facies
        else:
            log_name_target = log_name

        extracted_log = np.array(well.Log[log_name_target])[facies_log == facies].flatten()
        log_list.append(extracted_log)

        gnb = _fit_gaussian_nbs(extracted_log, label)
        gnb_list.append(gnb)
        
    # range for pdfs
    if log_name == 'AI':
        xmin = 4000
        xmax = 13000
    elif log_name == 'Vp/Vs':
        xmin = 1.0
        xmax = 2.4
    else:
        xmin = min(map(lambda x: min(x), log_list)) 
        xmax = max(map(lambda x: max(x), log_list))

    xrange = np.linspace(xmin, xmax, 100)

    pdf_list = _compute_analytical_pdf(gnb_list, xrange)

    # compute sepration score
    scores = {}

    # combinations of indexes
    pairs = []
    for i in range(len(facies_list)):
        for j in range(i+1, len(facies_list)):
            pairs.append( (i,j) )

    dx = (xrange[-1] - xrange[0]) / xrange.shape[0]

    title = f"{log_name} separation || Unit: {well.unit_tag} \n"
    
    for pair in pairs:
       
       score =  _compute_separation_score(pdf_list[pair[0]], pdf_list[pair[1]], dx)
       # key is (facies1, facies2)
       scores[(facies_list[pair[0]], facies_list[pair[1]])] = score
       
       title += f"({facies_list[pair[0]]}, {facies_list[pair[1]]}) | score: {score:.3f} \n"

    fig, ax = plt.subplots(figsize=(9, 6))
    
    # histogram & analytical pdf
    bins = 50
    for i, facies in enumerate(facies_list):
        ax.hist(log_list[i], bins=bins, label=f': {facies}',
                 alpha=0.3, density=True, color=get_facies_color(facies))
        
        ax.plot(xrange, pdf_list[i], get_facies_color(facies), linestyle="--")

    # Decoration
    ax.legend()
    ax.set_xlim([xmin, xmax])
    ax.set_title(title, fontsize=8)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    if save_fig:
        fig_name = f"{well.well_name}_separability_{well.unit_tag}"
        file_name = f"./img/{fig_name}"
        fig.savefig(file_name)
        return file_name
    return

from sklearn.naive_bayes import GaussianNB
import scipy

def _fit_gaussian_nbs(log, label):

    gnb = GaussianNB()
    # 1D to 2D array (n, 1)
    filt_log = (log[~ np.isnan(log)]).reshape(-1,1)
    gnb.fit(filt_log, np.ones(filt_log.shape[0]) * label)  # Predict 1
    return gnb

def _compute_analytical_pdf(gnb_list, xrange):
    
    pdf_list = []

    for gnb in gnb_list:
        pdf = scipy.stats.norm.pdf(xrange, gnb.theta_[0][0],
                                    np.sqrt(gnb.var_[0][0]))
        
        pdf_list.append(pdf)

    return pdf_list

def _compute_separation_score(pdf1, pdf2, dx):
    area_c1 = np.sum(pdf1 * dx) # Reimann's approximation
    area_c2 = np.sum(pdf2 * dx)
    overlap = np.sum(np.minimum(pdf1, pdf2) * dx)
    return ((area_c1 + area_c2) - 2 * overlap) / (area_c1 + area_c2)

def plot_depth_trend_insitu(well, log_name, depth_col="TVDSS", save_fig=False):

    fig, ax = plt.subplots(figsize=(7, 12))

    logs = well.Log.copy()

    # Plot facies groupings
    grouped_logs = logs.groupby("Facies")
    _plot_facies_groups(ax, grouped_logs, log_name, depth_col)

    # Plot top markers
    _plot_top_markers(ax, log_name, well, depth_col)

    # Set labels and plot attributes
    _set_plot_attributes(ax, log_name, well, depth_col)

    # legend
    names = []
    for facies, _ in reversed(list(grouped_logs)):
                names.append(f': {facies}')
    ax.legend(names)

    if save_fig:
        if log_name.startswith('Vp/Vs'):
            log_name = 'VpVs'
        fig_name = f"{well.well_name}_depth_trend_insitu_{log_name}"
        file_name = f"./img/{fig_name}"
        fig.savefig(file_name)
        return file_name
    
def plot_depth_trend_fluid_sub(well, log_name, depth_col="TVDSS", save_fig=False):

    fig, ax = plt.subplots(figsize=(7, 12))

    logs = well.Log.copy()

    # take "Facies_brine", "Facies_gas" etc column
    # so that we know how many fluid types are modelled
    facies_columns = []
    for col in list(well.Log.columns):
        if col.startswith('Facies_'):
            facies_columns.append(col)
    
    # Plot background: shale, coal, other from insitu
    grouped_logs = logs.groupby("Facies")
    
    # do not plot insitu sands
    _plot_facies_groups(ax, grouped_logs, log_name, depth_col, exclusion=["brine", "gas", "oil"])

    # collect legend name
    names = []
    for facies, _ in reversed(list(grouped_logs)):
        if facies not in ["brine", "gas", "oil"]:
            names.append(f': {facies}')

    # Plot substituted sand: _brine, _gas, etc.
    for fcol in facies_columns:
        if log_name in ["AI", "Vp/Vs", "Vp", "Vs", "RHOB"]:
            log_name_target = log_name + fcol[6:] # "_fluid"
        else:
            log_name_target = log_name

        grouped_logs = logs.groupby(fcol)
        _plot_facies_groups(ax, grouped_logs, log_name_target, depth_col, 
                            exclusion=["shale", "coal", "dirty_sand", "_invalid_sand"])

        #collect legend name
        for facies, _ in reversed(list(grouped_logs)):
            if facies in ["_gas", "_brine", "_oil"]:
                names.append(f': {facies}')

    # Plot top markers
    _plot_top_markers(ax, log_name, well, depth_col)

    # Set labels and plot attributes
    _set_plot_attributes(ax, log_name, well, depth_col)
        
    ax.legend(names)

    if save_fig:
        if log_name.startswith('Vp/Vs'):
            log_name = 'VpVs'
        fig_name = f"{well.well_name}_depth_trend_fluid_sub_{log_name}"
        file_name = f"./img/{fig_name}"
        fig.savefig(file_name)
        return file_name

    return

def _plot_facies_groups(ax, grouped_logs, log_name, depth_col, exclusion = []):
    # reverse so that shale comes first and thus be a background
    for facies, group in reversed(list(grouped_logs)):
        if facies in exclusion:
            continue
        color = get_facies_color(facies)
        ax.scatter(group[log_name], group[depth_col], color=color, s=20)
    

def _plot_top_markers(ax, log_name, well, depth_col):
    
    min_data_depth, max_data_depth = ax.get_ylim()
    tol = 0.05
    # Assume MD is at col 0 and TVDSS is at 1, 
    # which is safe because we import with this convention
    depth_key = 0 if depth_col == 'MD' else 1

    log = well.Log[log_name]

    valid_log = log[(~np.isinf(log))].dropna()
    
    log_mean = np.mean(valid_log)
    log_std = np.std(valid_log)

    if log_name.startswith("AI"):
        lower_bound = 2000
        upper_bound = 14000
    elif log_name.startswith("Vp/Vs"):
        lower_bound = 1.2
        upper_bound = 2.4
    else:
        lower_bound = log_mean - 3 * log_std
        upper_bound = log_mean + 3 * log_std

    for j, top_depth in enumerate(well.top_depth[depth_key]):
        # Tops are within the range of the plot
        if min_data_depth < top_depth < max_data_depth:

            # Plot line for tops
            ax.plot([lower_bound, upper_bound],
                    [top_depth, top_depth],
                    linestyle='--', color='darkgray')

            # Add label for tops
            ax.text(upper_bound,
                    top_depth - 5,
                    well.top_name[j],
                    fontsize=11, color='black')
            
def _set_plot_attributes(ax, log_name, well, depth_col):
    # Set scale information
    suffix = '(Up Scale)' if well.is_up_scaled else '(Log Scale)'

    ax.set_ylim(ax.get_ylim()[::-1])  # Reverse y-axis for depth
    # specialized depth limit for AI and Vp/Vs
    if log_name.startswith('AI'):
        ax.set_xlim([2000, 16000])
    elif log_name.startswith('Vp/Vs'):
        ax.set_xlim([1.2, 2.6])

    
    unit = ' (g/cm3 * m/s)' if log_name.startswith('AI') else ' (--unit--)'

    ax.set_xlabel(log_name + unit, fontsize=14)
    ax.set_ylabel(f'{depth_col} (m)', fontsize=14)
    ax.set_title(f'{log_name} - {depth_col} Trend: {well.well_name} {suffix}', fontsize=16, pad=15)
    ax.grid()
    plt.tight_layout()


def create_upscale_well(well: QIWell, window=40, stride=20):
    vp_alias = ['Vp', 'Vp_brine', 'Vp_gas', 'Vp_oil']
    vs_alias = ['Vs', 'Vs_brine', 'Vs_gas', 'Vs_oil']
    rhob_alias = ["RHOB", "RHOB_brine", "RHOB_gas", "RHOB_oil"]
    ai_alias = ['AI', 'AI_brine', 'AI_gas', 'AI_oil']
    depth_alias = ['MD', 'TVDSS', 'Unit']

    exclusion_list = vp_alias + vs_alias + rhob_alias + depth_alias + ai_alias

    uwell = deepcopy(well)

    column_names = uwell.Log.columns

    # Non-acoustic properties
    for log_name in column_names:
        if log_name not in exclusion_list:
            log = _upscale_non_acoustic_log(well, log_name, window, stride)
            # replace the non-upscale
            uwell.add_log(log_name, log)

    # _gas, _oil, _brine
    suffixes = _accumulate_suffix(column_names)

    # Acoustic properties need different treatment
    # it must be addressed through moduli
    for suffix in suffixes:
        vp, vs, rhob = _upscale_acoustic_log(well, suffix, window, stride)

        ai = vp * rhob
        vpvs = vp / vs

        uwell.add_log('Vp' + suffix, vp)
        uwell.add_log('Vs' + suffix, vs)
        uwell.add_log('RHOB' + suffix, rhob)
        uwell.add_log('AI' + suffix, ai)
        uwell.add_log('Vp/Vs' + suffix, vpvs)

    uwell.is_up_scaled = True

    return uwell

def _upscale_non_acoustic_log(well, log_name, window, stride, do_facies_upscale = False):
    dz = well.Log['MD'].iloc[1] - well.Log['MD'].iloc[0]
    
    # metres -> n samples
    nw = int(window / dz)
    half_nw = int(nw / 2)
    ns = int(stride / dz)

    old = well.Log[log_name]
    new = well.Log[log_name].copy()

    if log_name in ['k', 'k_brine', 'k_gas', 'k_oil', 'mu', 'mu_brine', 'mu_oil', 'mu_gas']:  # Harmonic
        for i in range(half_nw, well.Log[log_name].shape[0], ns):
            new[(i - half_nw):(i + half_nw + 1)] = scipy.stats.hmean(old[(i - half_nw):(i + half_nw + 1)], nan_policy='omit')

    elif log_name in ['Facies', 'Facies_brine', 'Facies_gas', 'Facies_oil']:  # most-of
        if do_facies_upscale:
            for i in range(half_nw, well.Log[log_name].shape[0], ns):
                uniq, pos = np.unique(list(old[(i - half_nw):(i + half_nw + 1)]), return_inverse=True)
                counts = np.bincount(pos)
                maxpos = counts.argmax()
                new[(i - half_nw):(i + half_nw + 1)] = uniq[maxpos]
        else:
            return new

    else:  # Default: arithmetic mean
        for i in range(half_nw, well.Log[log_name].shape[0], ns):
            new[(i - half_nw):(i + half_nw + 1)] = np.mean(old[(i - half_nw):(i + half_nw + 1)])
    
    # propogate the original nan
    nan_mask = np.isnan(old)
    result = np.where(nan_mask, np.nan, new)

    return result

def _upscale_acoustic_log(well, suffix, window=40, stride=20):
    k, mu = _get_bulk_and_shear_modulus(well.Log['Vp' + suffix],
                                       well.Log['Vs' + suffix],
                                       well.Log['RHOB' + suffix])

    well.add_log('k' + suffix, k)
    well.add_log('mu' + suffix, mu)

    k_upscale = _upscale_non_acoustic_log(well, 'k' + suffix, window, stride)
    mu_upscale = _upscale_non_acoustic_log(well, 'mu' + suffix, window, stride)
    rhob_upscale = _upscale_non_acoustic_log(well, 'RHOB' + suffix, window, stride)

    vp_upscale = np.sqrt((k_upscale + (4.0 / 3.0) * mu_upscale) / (rhob_upscale * 1000))
    vs_upscale = np.sqrt(mu_upscale / (rhob_upscale * 1000))

    return vp_upscale, vs_upscale, rhob_upscale

def _get_bulk_and_shear_modulus(vp, vs, rhob):
    mu = (vs ** 2) * rhob * 1000
    k = (vp ** 2) * rhob * 1000 - (4 * mu) / 3

    mu = np.where(mu > 0, mu, np.nan)
    k = np.where(k > 0, k, np.nan)
    return k, mu

def _accumulate_suffix(column_names):
    suffixes = set()
    for column in column_names:
        if column.startswith('Facies'):
            suffix = column[6:] # "_fluid(s)"
            suffixes.add(suffix)
    return suffixes
