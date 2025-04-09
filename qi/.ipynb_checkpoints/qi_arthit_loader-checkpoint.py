from .qi_well import *

def load_at151x():
    parent_path = './data/Arthit/Arthit-15-1X/' 
    log_path = parent_path + 'ARTHIT_15_1X.las'
    dev_path = parent_path + 'Arthit-15-1X_dev.csv'
    top_path = parent_path + 'Arthit-15-1X_marker_ed.txt'
    WELL_NAME = 'Arthit-15-1X'
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

    at151x.set_facies_config("Arthit")
    at151x.preprocess_acoustic_logs()
    
    return WELL_NAME, at151x

def load_at168():
    parent_path = './data/Arthit/Arthit-16-8/' 
    log_path = parent_path + 'ARTHIT_16_8.las'
    dev_path = parent_path + 'Arthit-16-8_dev.csv'
    top_path = parent_path + 'Arthit-16-8_marker_ed.txt'
    WELL_NAME = 'Arthit-16-8'
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
    at168 =  QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at168.load_deviation(dev_path, KB=26, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at168.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at168.set_facies_config("Arthit")

    at168.preprocess_acoustic_logs()
    return WELL_NAME, at168


def load_at152x():
    parent_path = './data/Arthit/Arthit-15-2X/' 
    log_path = parent_path + 'ARTHIT_15_2X.las'
    dev_path = parent_path + 'Arthit-15-2X_dev.csv'
    top_path = parent_path + 'Arthit-15-2X_marker_ed.txt'

    WELL_NAME = 'Arthit-15-2X'
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

    # END OF USER'S SETTING
    #######################

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

    at152x = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at152x.load_deviation(dev_path, KB=26.3, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at152x.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at152x.set_facies_config("Arthit")
    at152x.preprocess_acoustic_logs()
    
    return WELL_NAME, at152x


def load_at1531():
    parent_path = './data/Arthit/Arthit-15-31/' 
    log_path = parent_path + 'ARTHIT_15_31.las'
    dev_path = parent_path + 'Arthit-15-31_dev.csv'
    top_path = parent_path + 'Arthit-15-31_marker_ed.txt'

    WELL_NAME = 'Arthit-15-31'
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

    # END OF USER'S SETTING
    #######################

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

    at1531 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at1531.load_deviation(dev_path, KB=35.8, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at1531.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at1531.set_facies_config("Arthit")
    at1531.preprocess_acoustic_logs()
    
    return WELL_NAME, at1531


def load_at1420():
    parent_path = './data/Arthit/Arthit-14-20/' 
    log_path = parent_path + 'ARTHIT_14_20.las'
    dev_path = parent_path + 'Arthit-14-20_dev.csv'
    top_path = parent_path + 'Arthit-14-20_marker_ed.txt'

    WELL_NAME = 'Arthit-14-20'
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

    # END OF USER'S SETTING
    #######################

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

    at1420 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at1420.load_deviation(dev_path, KB=35.8, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at1420.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at1420.set_facies_config("Arthit")
    at1420.preprocess_acoustic_logs()

    return WELL_NAME, at1420


def load_at1421st():
    parent_path = './data/Arthit/Arthit-14-21-ST/' 
    log_path = parent_path + 'ARTHIT_14_21_ST.las'
    dev_path = parent_path + 'Arthit-14-21_ST_dev.csv'
    top_path = parent_path + 'Arthit-14-21_ST_marker_ed.txt'

    WELL_NAME = 'Arthit-14-21-ST'
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
    
    # END OF USER'S SETTING
    #######################
    
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

    at1421st = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at1421st.load_deviation(dev_path, KB=35.8, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at1421st.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at1421st.set_facies_config("Arthit")
    at1421st.preprocess_acoustic_logs()
    
    return WELL_NAME, at1421st



def load_at1424():
    parent_path = './data/Arthit/Arthit-14-24/' 
    log_path = parent_path + 'ARTHIT_14_24.las'
    dev_path = parent_path + 'Arthit-14-24_dev.csv'
    top_path = parent_path + 'Arthit-14-24_marker_ed.txt'

    WELL_NAME = 'Arthit-14-24'
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
    
    # END OF USER'S SETTING
    #######################
    
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


    at1424 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at1424.load_deviation(dev_path, KB=35.8, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at1424.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at1424.set_facies_config("Arthit")
    at1424.preprocess_acoustic_logs()
    
    return WELL_NAME, at1424


def load_at1527():
    parent_path = './data/Arthit/Arthit-15-27/' 
    log_path = parent_path + 'ARTHIT_15_27.las'
    dev_path = parent_path + 'Arthit-15-27_dev.csv'
    top_path = parent_path + 'Arthit-15-27_marker_ed.txt'

    WELL_NAME = 'Arthit-15-27'
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
    
    # END OF USER'S SETTING
    #######################
    
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


    at1527 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at1527.load_deviation(dev_path, KB=35.8, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at1527.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at1527.set_facies_config("Arthit")
    at1527.preprocess_acoustic_logs()
    
    return WELL_NAME, at1527
    

def load_at1610():
    parent_path = './data/Arthit/Arthit-16-10/' 
    log_path = parent_path + 'ARTHIT_16_10.las'
    dev_path = parent_path + 'Arthit-16-10_dev.csv'
    top_path = parent_path + 'Arthit-16-10_marker_ed.txt'

    WELL_NAME = 'Arthit-16-10'
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
    
    # END OF USER'S SETTING
    #######################
    
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


    at1610 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at1610.load_deviation(dev_path, KB=35.8, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at1610.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at1610.set_facies_config("Arthit")
    at1610.preprocess_acoustic_logs()
    
    return WELL_NAME, at1610




def load_at1611():
    parent_path = './data/Arthit/Arthit-16-11/' 
    log_path = parent_path + 'ARTHIT_16_11.las'
    dev_path = parent_path + 'Arthit-16-11_dev.csv'
    top_path = parent_path + 'Arthit-16-11_marker_ed.txt'

    WELL_NAME = 'Arthit-16-11'
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
    
    # END OF USER'S SETTING
    #######################
    
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


    at1611 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    at1611.load_deviation(dev_path, KB=35.8, col_MD=1, col_X=7, col_Y=8, col_TVD=5, separator=',', n_header=1, preview=False)
    at1611.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    at1611.set_facies_config("Arthit")
    at1611.preprocess_acoustic_logs()
    
    return WELL_NAME, at1611



def load_arthit_wells():
    db = {}
    functions_list = [load_at152x, load_at1531, load_at151x, load_at168, load_at1420, load_at1421st, load_at1424, load_at1527, load_at1610, load_at1611]

    for f in functions_list:

        name, well = f()
        
        # TODO: To Upper here for Arthit

        db[name] = well

    return db

#load_arthit_wells()