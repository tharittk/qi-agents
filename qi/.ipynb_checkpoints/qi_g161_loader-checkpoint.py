
from qi_well import *

def load_ba18():
    parent_path = './data/G161/BA18/'
    log_path = parent_path + 'BA18.las'
    dev_path = parent_path + 'BA18'
    top_path = parent_path + 'BA18_Marker_mMD.txt'
    WELL_NAME = 'BA-18'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }

    ba18 =  QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    ba18.load_deviation(dev_path, KB=28.65, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    ba18.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    ba18.set_facies_config("G161")

    ba18.preprocess_acoustic_logs()
    return WELL_NAME, ba18

def load_ba18s():
    parent_path = './data/G161/BA18S/'
    log_path = parent_path + 'BA18S.las'
    dev_path = parent_path + 'BA18S'
    top_path = parent_path + 'BA18S_Marker_mMD.txt'
    WELL_NAME = 'BA-18S'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }

    ba18s =  QIWell(WELL_NAME, log_path, remap)

    ba18s.load_deviation(dev_path, KB=28.65, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    ba18s.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    ba18s.set_facies_config("G161")

    ba18s.preprocess_acoustic_logs()


    return WELL_NAME, ba18s

def load_pd09():
    parent_path = './data/G161/PD09/'

    log_path = parent_path + 'PD09.las'
    dev_path = parent_path + 'PD09'
    top_path = parent_path + 'PD09_Marker_mMD.txt'
    WELL_NAME = 'PD-09'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    pd09 = QIWell(WELL_NAME, log_path, remap)
    pd09.load_deviation(dev_path, KB=28.65, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pd09.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pd09.set_facies_config("G161")

    pd09.preprocess_acoustic_logs()

    return WELL_NAME, pd09

def load_pk11():
    parent_path = './data/G161/PK11/'

    log_path = parent_path + 'PK11.las'
    dev_path = parent_path + 'PK11'
    top_path = parent_path + 'PK11_Marker_mMD.txt'
    WELL_NAME = 'PK-11'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }

    pk11 =  QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    pk11.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pk11.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pk11.set_facies_config("G161")

    pk11.preprocess_acoustic_logs()
    return WELL_NAME, pk11

def load_pk12():
    parent_path = './data/G161/PK12/'

    log_path = parent_path + 'PK12.las'
    dev_path = parent_path + 'PK12'
    top_path = parent_path + 'PK12_Marker_mMD.txt'
    WELL_NAME = 'PK-12'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    pk12 = QIWell(WELL_NAME, log_path, remap)
    pk12.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pk12.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pk12.set_facies_config("G161")

    pk12.preprocess_acoustic_logs()

    return WELL_NAME, pk12

def load_pk13():
    parent_path = './data/G161/PK13/'

    log_path = parent_path + 'PK13.las'
    dev_path = parent_path + 'PK13'
    top_path = parent_path + 'PK13_Marker_mMD.txt'
    WELL_NAME = 'PK-13'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    pk13 = QIWell(WELL_NAME, log_path, remap)
    pk13.load_deviation(dev_path, KB=28.96, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pk13.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pk13.set_facies_config("G161")

    pk13.preprocess_acoustic_logs()

    return WELL_NAME, pk13

def load_pl21():
    parent_path = './data/G161/PL21/'

    log_path = parent_path + 'PL21.las'
    dev_path = parent_path + 'PL21'
    top_path = parent_path + 'PL21_Marker_mMD.txt'
    WELL_NAME = 'PL-21'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    pl21 = QIWell(WELL_NAME, log_path, remap)
    pl21.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pl21.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pl21.set_facies_config("G161")

    pl21.preprocess_acoustic_logs()

    return WELL_NAME, pl21

def load_pl22():
    parent_path = './data/G161/PL22/'

    log_path = parent_path + 'PL22.las'
    dev_path = parent_path + 'PL22'
    top_path = parent_path + 'PL22_Marker_mMD.txt'
    WELL_NAME = 'PL-22'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    pl22 = QIWell(WELL_NAME, log_path, remap)
    pl22.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pl22.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pl22.set_facies_config("G161")

    pl22.preprocess_acoustic_logs()

    return WELL_NAME, pl22

def load_pl24():
    parent_path = './data/G161/PL24/'

    log_path = parent_path + 'PL24.las'
    dev_path = parent_path + 'PL24'
    top_path = parent_path + 'PL24_Marker_mMD.txt'
    WELL_NAME = 'PL-24'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
    DTC_COL : 'DTC',
    DTS_COL : 'DTS',
    RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
    SWE_COL  : 'Sw',
    LITHO_COL : 'LITHO',
    FLUID_COL : 'FLUID'
    }
    pl24 = QIWell(WELL_NAME, log_path, remap)
    pl24.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pl24.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pl24.set_facies_config("G161")

    pl24.preprocess_acoustic_logs()

    return WELL_NAME, pl24

def load_pm08():
    parent_path = './data/G161/PM08/'

    log_path = parent_path + 'PM08.las'
    dev_path = parent_path + 'PM08'
    top_path = parent_path + 'PM08_Marker_mMD.txt'
    WELL_NAME = 'PM-08'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    pm08 = QIWell(WELL_NAME, log_path, remap)
    pm08.load_deviation(dev_path, KB=27.74, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    pm08.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pm08.set_facies_config("G161")

    pm08.preprocess_acoustic_logs()

    return WELL_NAME, pm08

def load_sa33():
    parent_path = './data/G161/SA33/'

    log_path = parent_path + 'SA33.las'
    dev_path = parent_path + 'SA33'
    top_path = parent_path + 'SA33_Marker_mMD.txt'
    WELL_NAME = 'SA-33'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    sa33 = QIWell(WELL_NAME, log_path, remap)
    sa33.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    sa33.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    sa33.set_facies_config("G161")

    sa33.preprocess_acoustic_logs()

    return WELL_NAME, sa33

def load_sa34():
    parent_path = './data/G161/SA34/'

    log_path = parent_path + 'SA34.las'
    dev_path = parent_path + 'SA34'
    top_path = parent_path + 'SA34_Marker_mMD.txt'
    WELL_NAME = 'SA-34'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    sa34 = QIWell(WELL_NAME, log_path, remap)
    sa34.load_deviation(dev_path, KB=28.65, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    sa34.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    sa34.set_facies_config("G161")

    sa34.preprocess_acoustic_logs()

    return WELL_NAME, sa34

def load_tr18():
    parent_path = './data/G161/TR18/'

    log_path = parent_path + 'TR18.las'
    dev_path = parent_path + 'TR18'
    top_path = parent_path + 'TR18_Marker_mMD.txt'
    WELL_NAME = 'TR-18'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }

    tr18 = QIWell(WELL_NAME, log_path, remap)
    tr18.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    tr18.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tr18.set_facies_config("G161")

    tr18.preprocess_acoustic_logs()

    return WELL_NAME, tr18

def load_tr19():
    parent_path = './data/G161/TR19/'

    log_path = parent_path + 'TR19.las'
    dev_path = parent_path + 'TR19'
    top_path = parent_path + 'TR19_Marker_mMD.txt'
    WELL_NAME = 'TR-19'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    tr19 = QIWell(WELL_NAME, log_path, remap)
    tr19.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    tr19.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tr19.set_facies_config("G161")

    tr19.preprocess_acoustic_logs()

    return WELL_NAME, tr19

def load_tr20():
    parent_path = './data/G161/TR20/'

    log_path = parent_path + 'TR20.las'
    dev_path = parent_path + 'TR20'
    top_path = parent_path + 'TR20_Marker_mMD.txt'
    WELL_NAME = 'TR-20'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    DTC_COL = 'DTC'
    DTS_COL = 'DTS'
    RHOB_COL = 'RHOB'
    VSH_COL = 'VSH'
    PHIE_COL = 'PHIE'
    SWE_COL = 'SWE'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'FLUID'

    remap = {
        MD_COL : 'MD',
        DTC_COL : 'DTC',
        DTS_COL : 'DTS',
        RHOB_COL : 'RHOB',
        VSH_COL : 'Vsh',
        PHIE_COL : 'PHIE',
        SWE_COL  : 'Sw',
        LITHO_COL : 'LITHO',
        FLUID_COL : 'FLUID'
    }
    tr20 = QIWell(WELL_NAME, log_path, remap)
    tr20.load_deviation(dev_path, KB=26.82, col_MD=1, col_X=2, col_Y=3, col_TVD=5, separator=None, n_header=20, preview=False)
    tr20.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tr20.set_facies_config("G161")

    tr20.preprocess_acoustic_logs()

    return WELL_NAME, tr20

def load_g161_wells():
    db = {}
    functions_list = [load_ba18, load_ba18s, load_pd09, load_pk11, load_pk12, load_pk13,
                      load_pl21, load_pl22, load_pl24, load_pm08, load_sa33, load_sa34, load_tr18, load_tr19, load_tr20]

    for f in functions_list:

        name, well = f()
        db[name] = well

    return db

def load_exp_wells():
    db = {}
    functions_list = [load_ba18]
    for f in functions_list:

        name, well = f()
        db[name] = well

    return db