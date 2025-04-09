from .qi_well import *

def load_bk_del_1():
    parent_path = './data/Bongkot/BK-DEL-1/' 
    log_path = parent_path + 'bk-del-1.las'
    dev_path = parent_path + 'bk-del-1_dev.csv'
    top_path = parent_path + 'bk-del-1_marker_ed.txt'
    WELL_NAME = 'BK-DEL-1'
    # Column name as specified in .las file
    MD_COL = 'DEPTH'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'

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

    bkdel1 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bkdel1.load_deviation(dev_path, KB=32, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bkdel1.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bkdel1.set_facies_config("Bongkot")
    bkdel1.preprocess_acoustic_logs()
    
    return WELL_NAME, bkdel1


def load_bk_del_18c():
    parent_path = './data/Bongkot/BK-DEL-18C/' 
    log_path = parent_path + 'bk-del-18c.las'
    dev_path = parent_path + 'bk-del-18c_dev.csv'
    top_path = parent_path + 'bk-del-18c_marker_ed.txt'

    WELL_NAME = 'BK-DEL-18C'
    # Column name as specified in .las file
    MD_COL = 'DEPTH'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'

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
    
    bkdel18c = QIWell(WELL_NAME, log_path, remap)
    
    bkdel18c.load_deviation(dev_path, KB=32, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bkdel18c.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bkdel18c.set_facies_config("Bongkot")
    bkdel18c.preprocess_acoustic_logs()

    return WELL_NAME, bkdel18c


def load_bk_del_40():
    parent_path = './data/Bongkot/BK-DEL-40/' 
    log_path = parent_path + 'bk-del-40.las'
    dev_path = parent_path + 'bk-del-40_dev.csv'
    top_path = parent_path + 'bk-del-40_marker_ed.txt'
    
    WELL_NAME = 'BK-DEL-40'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'

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

    bkdel40 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bkdel40.load_deviation(dev_path, KB=32.35, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bkdel40.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bkdel40.set_facies_config("Bongkot")
    bkdel40.preprocess_acoustic_logs()
    
    return WELL_NAME, bkdel40


def load_tny_5():
    parent_path = './data/Bongkot/TNY-5/' 
    log_path = parent_path + 'tny-5.las'
    dev_path = parent_path + 'tny-5_dev.csv'
    top_path = parent_path + 'tny-5_marker_ed.txt'
    WELL_NAME = 'TNY-5'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'

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

    tny5 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    tny5.load_deviation(dev_path, KB=30, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    tny5.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tny5.set_facies_config("Bongkot")
    tny5.preprocess_acoustic_logs()
    
    return WELL_NAME, tny5


def load_pk_2x():
    parent_path = './data/Bongkot/PIKUL-2X/' 
    log_path = parent_path + 'pikul-2x.las'
    dev_path = parent_path + 'pikul-2x_dev.csv'
    top_path = parent_path + 'pikul-2x_marker_ed.txt'

    WELL_NAME = 'PIKUL-2X'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'

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

    pk2x = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    pk2x.load_deviation(dev_path, KB=26.8, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    pk2x.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    pk2x.set_facies_config("Bongkot")
    pk2x.preprocess_acoustic_logs()
    
    return WELL_NAME, pk2x


def load_bk20k():
    parent_path = './data/Bongkot/BK-20-K/' 
    log_path = parent_path + 'bk-20-k.las'
    dev_path = parent_path + 'bk-20-k_dev.csv'
    top_path = parent_path + 'bk-20-k_marker_ed.txt'

    WELL_NAME = 'BK-20-K'
    # Column name as specified in .las file
    MD_COL = 'DEPTH'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    bk20k = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bk20k.load_deviation(dev_path, KB=28, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bk20k.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bk20k.set_facies_config("Bongkot")
    bk20k.preprocess_acoustic_logs()
    
    return WELL_NAME, bk20k


def load_tny1x():
    parent_path = './data/Bongkot/TNY-1X/' 
    log_path = parent_path + 'TNY_1X.las'
    dev_path = parent_path + 'tny-1x_dev.las'
    top_path = parent_path + 'tny-1x_marker_ed.txt'
    WELL_NAME = 'TNY-1X'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    tny1x = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    tny1x.load_deviation(dev_path, KB=25, col_MD=1, col_X=6, col_Y=8, col_TVD=4, separator=None, n_header=41, preview=False)
    tny1x.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tny1x.set_facies_config("Bongkot")
    tny1x.preprocess_acoustic_logs()
    
    return WELL_NAME, tny1x


def load_bk29g():
    parent_path = './data/Bongkot/BK-29-G/' 
    log_path = parent_path + 'bk-29-g.las'
    dev_path = parent_path + 'bk-29-g_dev.csv'
    top_path = parent_path + 'bk-29-g_marker_ed.txt'
    WELL_NAME = 'BK-29-G'
    # Column name as specified in .las file
    MD_COL = 'DEPTH'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    bk29g = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bk29g.load_deviation(dev_path, KB=38, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bk29g.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bk29g.set_facies_config("Bongkot")
    bk29g.preprocess_acoustic_logs()
    
    return WELL_NAME, bk29g


def load_bk8d():
    parent_path = './data/Bongkot/BK-8-D/' 
    log_path = parent_path + 'bk-8-d.las'
    dev_path = parent_path + 'bk-8-d_dev.csv'
    top_path = parent_path + 'bk-8-d_marker_ed.txt'
    WELL_NAME = 'BK-8-D'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    bk8d = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bk8d.load_deviation(dev_path, KB=28, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bk8d.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bk8d.set_facies_config("Bongkot")
    bk8d.preprocess_acoustic_logs()
    
    return WELL_NAME, bk8d


def load_bkdel22():
    parent_path = './data/Bongkot/BK-DEL-22/' 
    log_path = parent_path + 'bk-del-22.las'
    dev_path = parent_path + 'bk-del-22_dev.csv'
    top_path = parent_path + 'bk-del-22_marker_ed.txt'
    WELL_NAME = 'BK-DEL-22'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    bkdel22 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bkdel22.load_deviation(dev_path, KB=26.8, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bkdel22.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bkdel22.set_facies_config("Bongkot")
    bkdel22.preprocess_acoustic_logs()
    
    return WELL_NAME, bkdel22


def load_bkdel36():
    parent_path = './data/Bongkot/BK-DEL-36/' 
    log_path = parent_path + 'bk-del-36.las'
    dev_path = parent_path + 'bk-del-36_dev.csv'
    top_path = parent_path + 'bk-del-36_marker_ed.txt'
    WELL_NAME = 'BK-DEL-36'
    # Column name as specified in .las file
    MD_COL = 'DEPTH'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    bkdel36 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bkdel36.load_deviation(dev_path, KB=32.4, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bkdel36.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bkdel36.set_facies_config("Bongkot")
    bkdel36.preprocess_acoustic_logs()
    
    return WELL_NAME, bkdel36


def load_bkdel37():
    parent_path = './data/Bongkot/BK-DEL-37/' 
    log_path = parent_path + 'bk-del-37.las'
    dev_path = parent_path + 'bk-del-37_dev.csv'
    top_path = parent_path + 'bk-del-37_marker_ed.txt'
    WELL_NAME = 'BK-DEL-37'
    # Column name as specified in .las file
    MD_COL = 'DEPTH'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    bkdel37 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    bkdel37.load_deviation(dev_path, KB=32.2, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    bkdel37.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    bkdel37.set_facies_config("Bongkot")
    bkdel37.preprocess_acoustic_logs()
    
    return WELL_NAME, bkdel37


def load_tc2x():
    parent_path = './data/Bongkot/TONCHAN-2X/' 
    log_path = parent_path + 'tonchan-2x.las'
    dev_path = parent_path + 'tonchan-2x_dev.las'
    top_path = parent_path + 'tonchan-2x_marker_ed.txt'
    WELL_NAME = 'TONCHAN-2X'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    tc2x = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    tc2x.load_deviation(dev_path, KB=30, col_MD=1, col_X=6, col_Y=8, col_TVD=4, separator=None, n_header=41, preview=False)
    tc2x.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tc2x.set_facies_config("Bongkot")
    tc2x.preprocess_acoustic_logs()
    
    return WELL_NAME, tc2x


def load_ts7():
    parent_path = './data/Bongkot/TONSAK-7/' 
    log_path = parent_path + 'tonsak-7.las'
    dev_path = parent_path + 'tonsak-7_dev.las'
    top_path = parent_path + 'tonsak-7_marker_ed.txt'
    WELL_NAME = 'TONSAK-7'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    ts7 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    ts7.load_deviation(dev_path, KB=32, col_MD=1, col_X=6, col_Y=8, col_TVD=4, separator=None, n_header=41, preview=False)
    ts7.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    ts7.set_facies_config("Bongkot")
    ts7.preprocess_acoustic_logs()
    
    return WELL_NAME, ts7


def load_tsn2():
    parent_path = './data/Bongkot/TONSON-2/' 
    log_path = parent_path + 'tonson-2.las'
    dev_path = parent_path + 'tonson-2_dev.las'
    top_path = parent_path + 'tonson-2_marker_ed.txt'
    WELL_NAME = 'TONSON-2'
    # Column name as specified in .las file
    MD_COL = 'DEPT'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
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

    tsn2 = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    tsn2.load_deviation(dev_path, KB=32, col_MD=1, col_X=6, col_Y=8, col_TVD=4, separator=None, n_header=41, preview=False)
    tsn2.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tsn2.set_facies_config("Bongkot")
    tsn2.preprocess_acoustic_logs()
    
    return WELL_NAME, tsn2


def load_tr2x():
    parent_path = './data/Bongkot/TR-2X/' 
    log_path = parent_path + 'tr-2x.las'
    dev_path = parent_path + 'tr-2x_dev.csv'
    top_path = parent_path + 'tr-2x_marker_ed.txt'
    WELL_NAME = 'TR-2X'
    # Column name as specified in .las file
    MD_COL = 'DEPTH'
    GR_COL = 'GR'
    RHOB_COL = 'RHOB'
    PHIE_COL = 'PHIE'
    VSH_COL = 'VSH'
    SWE_COL = 'SWE'
    DTC_COL = 'DT'
    DTS_COL = 'DTSM'
    LITHO_COL = 'LITHO'
    FLUID_COL = 'NET'
    
    # END OF USER'S SETTING
    #######################
    
    remap = {
        MD_COL : 'MD',
        GR_COL : 'GR',
       RHOB_COL : 'RHOB',
       PHIE_COL : 'PHIE',
        VSH_COL : 'Vsh',
       SWE_COL  : 'Sw',
       DTC_COL : 'DTC',
       DTS_COL : 'DTS',
       LITHO_COL : 'LITHO',
       FLUID_COL : 'FLUID'
    }

    tr2x = QIWell(WELL_NAME, log_path, remap)

    # Load tops and deviation
    tr2x.load_deviation(dev_path, KB=30, col_MD=4, col_X=1, col_Y=2, col_TVD=9, separator=',', n_header=1, preview=False)
    tr2x.load_geological_tops(top_path, col_name=1, col_depth=2, separator='\t', n_header=1)
    tr2x.set_facies_config("Bongkot")
    tr2x.preprocess_acoustic_logs()
    
    return WELL_NAME, tr2x



def load_bk_wells():
    db = {}
    functions_list = [load_bk_del_1, load_bk_del_18c, load_bk_del_40, load_tny_5, load_pk_2x, load_bk20k, load_tny1x, load_bk29g, load_bk8d, 
                      load_bkdel22, load_bkdel36, load_bkdel37, load_tc2x, load_ts7, load_tsn2, load_tr2x]

    for f in functions_list:

        name, well = f()
        db[name] = well

    return db

#load_bongkot_wells()