from .qi_well import *

def load_dummy_well():
    parent_path = './ YOUR DATA PATH' 
    log_path = parent_path + '/ YOUR DATA PATH'
    dev_path = parent_path + '/ YOUR DATA PATH'
    top_path = parent_path + '/ YOUR DATA PATH'
    WELL_NAME = 'YOUR WELL NAME'

    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    # DO NOT CHANGE THIS
    remap = {
        MD_COL : 'MD',
        RHOB_COL : 'RHOB',
        PHIE_COL : 'PHIE',
        VSH_COL : 'Vsh',
        SWE_COL  : 'Sw',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    at151x = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at151x.load_deviation(dev_path, KB=26, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at151x.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)

    at151x.set_facies_config("FIELD NAME HERE")
    at151x.preprocess_acoustic_logs()
    
    return WELL_NAME, at151x

def load_all_wells():
    db = {}
    functions_list = [load_dummy_well]

    for f in functions_list:

        name, well = f()
        
        db[name] = well

    return db

#load_arthit_wells()