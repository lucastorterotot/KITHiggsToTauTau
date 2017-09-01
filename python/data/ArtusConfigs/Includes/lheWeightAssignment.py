#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import copy
import Artus.Utility.jsonTools as jsonTools
#import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import importlib
#import os

def build_config(nickname):
  config = jsonTools.JsonDict()
  #datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  
  
  ## fill config:
  # includes
  includes = [
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  if re.search("DYJetsToLL.*amcatnlo|TT", nickname):
    config["GenEventInfoMetadataNames"] = [
        "1001:muR1p0_muF1p0_weight",
        "1002:muR1p0_muF2p0_weight",
        "1003:muR1p0_muF0p5_weight",
        "1004:muR2p0_muF1p0_weight",
        "1005:muR2p0_muF2p0_weight",
        "1006:muR2p0_muF0p5_weight",
        "1007:muR0p5_muF1p0_weight",
        "1008:muR0p5_muF2p0_weight",
        "1009:muR0p5_muF0p5_weight",
        "2001:NNPDF30_nlo_as_0118_1_weight",
        "2002:NNPDF30_nlo_as_0118_2_weight",
        "2003:NNPDF30_nlo_as_0118_3_weight",
        "2004:NNPDF30_nlo_as_0118_4_weight",
        "2005:NNPDF30_nlo_as_0118_5_weight",
        "2006:NNPDF30_nlo_as_0118_6_weight",
        "2007:NNPDF30_nlo_as_0118_7_weight",
        "2008:NNPDF30_nlo_as_0118_8_weight",
        "2009:NNPDF30_nlo_as_0118_9_weight",
        "2010:NNPDF30_nlo_as_0118_10_weight",
        "2011:NNPDF30_nlo_as_0118_11_weight",
        "2012:NNPDF30_nlo_as_0118_12_weight",
        "2013:NNPDF30_nlo_as_0118_13_weight",
        "2014:NNPDF30_nlo_as_0118_14_weight",
        "2015:NNPDF30_nlo_as_0118_15_weight",
        "2016:NNPDF30_nlo_as_0118_16_weight",
        "2017:NNPDF30_nlo_as_0118_17_weight",
        "2018:NNPDF30_nlo_as_0118_18_weight",
        "2019:NNPDF30_nlo_as_0118_19_weight",
        "2020:NNPDF30_nlo_as_0118_20_weight",
        "2021:NNPDF30_nlo_as_0118_21_weight",
        "2022:NNPDF30_nlo_as_0118_22_weight",
        "2023:NNPDF30_nlo_as_0118_23_weight",
        "2024:NNPDF30_nlo_as_0118_24_weight",
        "2025:NNPDF30_nlo_as_0118_25_weight",
        "2026:NNPDF30_nlo_as_0118_26_weight",
        "2027:NNPDF30_nlo_as_0118_27_weight",
        "2028:NNPDF30_nlo_as_0118_28_weight",
        "2029:NNPDF30_nlo_as_0118_29_weight",
        "2030:NNPDF30_nlo_as_0118_30_weight",
        "2031:NNPDF30_nlo_as_0118_31_weight",
        "2032:NNPDF30_nlo_as_0118_32_weight",
        "2033:NNPDF30_nlo_as_0118_33_weight",
        "2034:NNPDF30_nlo_as_0118_34_weight",
        "2035:NNPDF30_nlo_as_0118_35_weight",
        "2036:NNPDF30_nlo_as_0118_36_weight",
        "2037:NNPDF30_nlo_as_0118_37_weight",
        "2038:NNPDF30_nlo_as_0118_38_weight",
        "2039:NNPDF30_nlo_as_0118_39_weight",
        "2040:NNPDF30_nlo_as_0118_40_weight",
        "2041:NNPDF30_nlo_as_0118_41_weight",
        "2042:NNPDF30_nlo_as_0118_42_weight",
        "2043:NNPDF30_nlo_as_0118_43_weight",
        "2044:NNPDF30_nlo_as_0118_44_weight",
        "2045:NNPDF30_nlo_as_0118_45_weight",
        "2046:NNPDF30_nlo_as_0118_46_weight",
        "2047:NNPDF30_nlo_as_0118_47_weight",
        "2048:NNPDF30_nlo_as_0118_48_weight",
        "2049:NNPDF30_nlo_as_0118_49_weight",
        "2050:NNPDF30_nlo_as_0118_50_weight",
        "2051:NNPDF30_nlo_as_0118_51_weight",
        "2052:NNPDF30_nlo_as_0118_52_weight",
        "2053:NNPDF30_nlo_as_0118_53_weight",
        "2054:NNPDF30_nlo_as_0118_54_weight",
        "2055:NNPDF30_nlo_as_0118_55_weight",
        "2056:NNPDF30_nlo_as_0118_56_weight",
        "2057:NNPDF30_nlo_as_0118_57_weight",
        "2058:NNPDF30_nlo_as_0118_58_weight",
        "2059:NNPDF30_nlo_as_0118_59_weight",
        "2060:NNPDF30_nlo_as_0118_60_weight",
        "2061:NNPDF30_nlo_as_0118_61_weight",
        "2062:NNPDF30_nlo_as_0118_62_weight",
        "2063:NNPDF30_nlo_as_0118_63_weight",
        "2064:NNPDF30_nlo_as_0118_64_weight",
        "2065:NNPDF30_nlo_as_0118_65_weight",
        "2066:NNPDF30_nlo_as_0118_66_weight",
        "2067:NNPDF30_nlo_as_0118_67_weight",
        "2068:NNPDF30_nlo_as_0118_68_weight",
        "2069:NNPDF30_nlo_as_0118_69_weight",
        "2070:NNPDF30_nlo_as_0118_70_weight",
        "2071:NNPDF30_nlo_as_0118_71_weight",
        "2072:NNPDF30_nlo_as_0118_72_weight",
        "2073:NNPDF30_nlo_as_0118_73_weight",
        "2074:NNPDF30_nlo_as_0118_74_weight",
        "2075:NNPDF30_nlo_as_0118_75_weight",
        "2076:NNPDF30_nlo_as_0118_76_weight",
        "2077:NNPDF30_nlo_as_0118_77_weight",
        "2078:NNPDF30_nlo_as_0118_78_weight",
        "2079:NNPDF30_nlo_as_0118_79_weight",
        "2080:NNPDF30_nlo_as_0118_80_weight",
        "2081:NNPDF30_nlo_as_0118_81_weight",
        "2082:NNPDF30_nlo_as_0118_82_weight",
        "2083:NNPDF30_nlo_as_0118_83_weight",
        "2084:NNPDF30_nlo_as_0118_84_weight",
        "2085:NNPDF30_nlo_as_0118_85_weight",
        "2086:NNPDF30_nlo_as_0118_86_weight",
        "2087:NNPDF30_nlo_as_0118_87_weight",
        "2088:NNPDF30_nlo_as_0118_88_weight",
        "2089:NNPDF30_nlo_as_0118_89_weight",
        "2090:NNPDF30_nlo_as_0118_90_weight",
        "2091:NNPDF30_nlo_as_0118_91_weight",
        "2092:NNPDF30_nlo_as_0118_92_weight",
        "2093:NNPDF30_nlo_as_0118_93_weight",
        "2094:NNPDF30_nlo_as_0118_94_weight",
        "2095:NNPDF30_nlo_as_0118_95_weight",
        "2096:NNPDF30_nlo_as_0118_96_weight",
        "2097:NNPDF30_nlo_as_0118_97_weight",
        "2098:NNPDF30_nlo_as_0118_98_weight",
        "2099:NNPDF30_nlo_as_0118_99_weight",
        "2100:NNPDF30_nlo_as_0118_00_weight",
        "2101:NNPDF30_nlo_as_0117_weight",
        "2102:NNPDF30_nlo_as_0119_weight",
        "3001:CT10nlo_1_weight",
        "3002:CT10nlo_2_weight",
        "3003:CT10nlo_3_weight",
        "3004:CT10nlo_4_weight",
        "3005:CT10nlo_5_weight",
        "3006:CT10nlo_6_weight",
        "3007:CT10nlo_7_weight",
        "3008:CT10nlo_8_weight",
        "3009:CT10nlo_9_weight",
        "3010:CT10nlo_10_weight",
        "3011:CT10nlo_11_weight",
        "3012:CT10nlo_12_weight",
        "3013:CT10nlo_13_weight",
        "3014:CT10nlo_14_weight",
        "3015:CT10nlo_15_weight",
        "3016:CT10nlo_16_weight",
        "3017:CT10nlo_17_weight",
        "3018:CT10nlo_18_weight",
        "3019:CT10nlo_19_weight",
        "3020:CT10nlo_20_weight",
        "3021:CT10nlo_21_weight",
        "3022:CT10nlo_22_weight",
        "3023:CT10nlo_23_weight",
        "3024:CT10nlo_24_weight",
        "3025:CT10nlo_25_weight",
        "3026:CT10nlo_26_weight",
        "3027:CT10nlo_27_weight",
        "3028:CT10nlo_28_weight",
        "3029:CT10nlo_29_weight",
        "3030:CT10nlo_30_weight",
        "3031:CT10nlo_31_weight",
        "3032:CT10nlo_32_weight",
        "3033:CT10nlo_33_weight",
        "3034:CT10nlo_34_weight",
        "3035:CT10nlo_35_weight",
        "3036:CT10nlo_36_weight",
        "3037:CT10nlo_37_weight",
        "3038:CT10nlo_38_weight",
        "3039:CT10nlo_39_weight",
        "3040:CT10nlo_40_weight",
        "3041:CT10nlo_41_weight",
        "3042:CT10nlo_42_weight",
        "3043:CT10nlo_43_weight",
        "3044:CT10nlo_44_weight",
        "3045:CT10nlo_45_weight",
        "3046:CT10nlo_46_weight",
        "3047:CT10nlo_47_weight",
        "3048:CT10nlo_48_weight",
        "3049:CT10nlo_49_weight",
        "3050:CT10nlo_50_weight",
        "3051:CT10nlo_51_weight",
        "3052:CT10nlo_52_weight",
        "3053:CT10nlo_53_weight",
        "3054:CT10nlo_as_0117_weight",
        "3055:CT10nlo_as_0119_weight",
        "4001:MMHT2014nlo68clas118_1_weight",
        "4002:MMHT2014nlo68clas118_2_weight",
        "4003:MMHT2014nlo68clas118_3_weight",
        "4004:MMHT2014nlo68clas118_4_weight",
        "4005:MMHT2014nlo68clas118_5_weight",
        "4006:MMHT2014nlo68clas118_6_weight",
        "4007:MMHT2014nlo68clas118_7_weight",
        "4008:MMHT2014nlo68clas118_8_weight",
        "4009:MMHT2014nlo68clas118_9_weight",
        "4010:MMHT2014nlo68clas118_10_weight",
        "4011:MMHT2014nlo68clas118_11_weight",
        "4012:MMHT2014nlo68clas118_12_weight",
        "4013:MMHT2014nlo68clas118_13_weight",
        "4014:MMHT2014nlo68clas118_14_weight",
        "4015:MMHT2014nlo68clas118_15_weight",
        "4016:MMHT2014nlo68clas118_16_weight",
        "4017:MMHT2014nlo68clas118_17_weight",
        "4018:MMHT2014nlo68clas118_18_weight",
        "4019:MMHT2014nlo68clas118_19_weight",
        "4020:MMHT2014nlo68clas118_20_weight",
        "4021:MMHT2014nlo68clas118_21_weight",
        "4022:MMHT2014nlo68clas118_22_weight",
        "4023:MMHT2014nlo68clas118_23_weight",
        "4024:MMHT2014nlo68clas118_24_weight",
        "4025:MMHT2014nlo68clas118_25_weight",
        "4026:MMHT2014nlo68clas118_26_weight",
        "4027:MMHT2014nlo68clas118_27_weight",
        "4028:MMHT2014nlo68clas118_28_weight",
        "4029:MMHT2014nlo68clas118_29_weight",
        "4030:MMHT2014nlo68clas118_30_weight",
        "4031:MMHT2014nlo68clas118_31_weight",
        "4032:MMHT2014nlo68clas118_32_weight",
        "4033:MMHT2014nlo68clas118_33_weight",
        "4034:MMHT2014nlo68clas118_34_weight",
        "4035:MMHT2014nlo68clas118_35_weight",
        "4036:MMHT2014nlo68clas118_36_weight",
        "4037:MMHT2014nlo68clas118_37_weight",
        "4038:MMHT2014nlo68clas118_38_weight",
        "4039:MMHT2014nlo68clas118_39_weight",
        "4040:MMHT2014nlo68clas118_40_weight",
        "4041:MMHT2014nlo68clas118_41_weight",
        "4042:MMHT2014nlo68clas118_42_weight",
        "4043:MMHT2014nlo68clas118_43_weight",
        "4044:MMHT2014nlo68clas118_44_weight",
        "4045:MMHT2014nlo68clas118_45_weight",
        "4046:MMHT2014nlo68clas118_46_weight",
        "4047:MMHT2014nlo68clas118_47_weight",
        "4048:MMHT2014nlo68clas118_48_weight",
        "4049:MMHT2014nlo68clas118_49_weight",
        "4050:MMHT2014nlo68clas118_50_weight",
        "4051:MMHT2014nlo68clas118_51_weight",
        "4052:MMHT2014nlo_asmzsmallrange_52_weight",
        "4053:MMHT2014nlo_asmzsmallrange_53_weight",
        "4054:MMHT2014nlo_asmzsmallrange_54_weight",
        "4055:MMHT2014nlo_asmzsmallrange_55_weight",
        "4056:MMHT2014nlo_asmzsmallrange_56_weight"
    ]
  elif re.search("DYJetsToLL.*madgraph", nickname):
    config["GenEventInfoMetadataNames"] = [
        "1:muR1p0_muF1p0_weight",
        "2:muR1p0_muF2p0_weight",
        "3:muR1p0_muF0p5_weight",
        "4:muR2p0_muF1p0_weight",
        "5:muR2p0_muF2p0_weight",
        "6:muR2p0_muF0p5_weight",
        "7:muR0p5_muF1p0_weight",
        "8:muR0p5_muF2p0_weight",
        "9:muR0p5_muF0p5_weight",
        "10:NNPDF30_lo_as_0130_0_weight",
        "11:NNPDF30_lo_as_0130_1_weight",
        "12:NNPDF30_lo_as_0130_2_weight",
        "13:NNPDF30_lo_as_0130_3_weight",
        "14:NNPDF30_lo_as_0130_4_weight",
        "15:NNPDF30_lo_as_0130_5_weight",
        "16:NNPDF30_lo_as_0130_6_weight",
        "17:NNPDF30_lo_as_0130_7_weight",
        "18:NNPDF30_lo_as_0130_8_weight",
        "19:NNPDF30_lo_as_0130_9_weight",
        "20:NNPDF30_lo_as_0130_10_weight",
        "21:NNPDF30_lo_as_0130_11_weight",
        "22:NNPDF30_lo_as_0130_12_weight",
        "23:NNPDF30_lo_as_0130_13_weight",
        "24:NNPDF30_lo_as_0130_14_weight",
        "25:NNPDF30_lo_as_0130_15_weight",
        "26:NNPDF30_lo_as_0130_16_weight",
        "27:NNPDF30_lo_as_0130_17_weight",
        "28:NNPDF30_lo_as_0130_18_weight",
        "29:NNPDF30_lo_as_0130_19_weight",
        "30:NNPDF30_lo_as_0130_20_weight",
        "31:NNPDF30_lo_as_0130_21_weight",
        "32:NNPDF30_lo_as_0130_22_weight",
        "33:NNPDF30_lo_as_0130_23_weight",
        "34:NNPDF30_lo_as_0130_24_weight",
        "35:NNPDF30_lo_as_0130_25_weight",
        "36:NNPDF30_lo_as_0130_26_weight",
        "37:NNPDF30_lo_as_0130_27_weight",
        "38:NNPDF30_lo_as_0130_28_weight",
        "39:NNPDF30_lo_as_0130_29_weight",
        "40:NNPDF30_lo_as_0130_30_weight",
        "41:NNPDF30_lo_as_0130_31_weight",
        "42:NNPDF30_lo_as_0130_32_weight",
        "43:NNPDF30_lo_as_0130_33_weight",
        "44:NNPDF30_lo_as_0130_34_weight",
        "45:NNPDF30_lo_as_0130_35_weight",
        "46:NNPDF30_lo_as_0130_36_weight",
        "47:NNPDF30_lo_as_0130_37_weight",
        "48:NNPDF30_lo_as_0130_38_weight",
        "49:NNPDF30_lo_as_0130_39_weight",
        "50:NNPDF30_lo_as_0130_40_weight",
        "51:NNPDF30_lo_as_0130_41_weight",
        "52:NNPDF30_lo_as_0130_42_weight",
        "53:NNPDF30_lo_as_0130_43_weight",
        "54:NNPDF30_lo_as_0130_44_weight",
        "55:NNPDF30_lo_as_0130_45_weight",
        "56:NNPDF30_lo_as_0130_46_weight",
        "57:NNPDF30_lo_as_0130_47_weight",
        "58:NNPDF30_lo_as_0130_48_weight",
        "59:NNPDF30_lo_as_0130_49_weight",
        "60:NNPDF30_lo_as_0130_50_weight",
        "61:NNPDF30_lo_as_0130_51_weight",
        "62:NNPDF30_lo_as_0130_52_weight",
        "63:NNPDF30_lo_as_0130_53_weight",
        "64:NNPDF30_lo_as_0130_54_weight",
        "65:NNPDF30_lo_as_0130_55_weight",
        "66:NNPDF30_lo_as_0130_56_weight",
        "67:NNPDF30_lo_as_0130_57_weight",
        "68:NNPDF30_lo_as_0130_58_weight",
        "69:NNPDF30_lo_as_0130_59_weight",
        "70:NNPDF30_lo_as_0130_60_weight",
        "71:NNPDF30_lo_as_0130_61_weight",
        "72:NNPDF30_lo_as_0130_62_weight",
        "73:NNPDF30_lo_as_0130_63_weight",
        "74:NNPDF30_lo_as_0130_64_weight",
        "75:NNPDF30_lo_as_0130_65_weight",
        "76:NNPDF30_lo_as_0130_66_weight",
        "77:NNPDF30_lo_as_0130_67_weight",
        "78:NNPDF30_lo_as_0130_68_weight",
        "79:NNPDF30_lo_as_0130_69_weight",
        "80:NNPDF30_lo_as_0130_70_weight",
        "81:NNPDF30_lo_as_0130_71_weight",
        "82:NNPDF30_lo_as_0130_72_weight",
        "83:NNPDF30_lo_as_0130_73_weight",
        "84:NNPDF30_lo_as_0130_74_weight",
        "85:NNPDF30_lo_as_0130_75_weight",
        "86:NNPDF30_lo_as_0130_76_weight",
        "87:NNPDF30_lo_as_0130_77_weight",
        "88:NNPDF30_lo_as_0130_78_weight",
        "89:NNPDF30_lo_as_0130_79_weight",
        "90:NNPDF30_lo_as_0130_80_weight",
        "91:NNPDF30_lo_as_0130_81_weight",
        "92:NNPDF30_lo_as_0130_82_weight",
        "93:NNPDF30_lo_as_0130_83_weight",
        "94:NNPDF30_lo_as_0130_84_weight",
        "95:NNPDF30_lo_as_0130_85_weight",
        "96:NNPDF30_lo_as_0130_86_weight",
        "97:NNPDF30_lo_as_0130_87_weight",
        "98:NNPDF30_lo_as_0130_88_weight",
        "99:NNPDF30_lo_as_0130_89_weight",
        "100:NNPDF30_lo_as_0130_90_weight",
        "101:NNPDF30_lo_as_0130_91_weight",
        "102:NNPDF30_lo_as_0130_92_weight",
        "103:NNPDF30_lo_as_0130_93_weight",
        "104:NNPDF30_lo_as_0130_94_weight",
        "105:NNPDF30_lo_as_0130_95_weight",
        "106:NNPDF30_lo_as_0130_96_weight",
        "107:NNPDF30_lo_as_0130_97_weight",
        "108:NNPDF30_lo_as_0130_98_weight",
        "109:NNPDF30_lo_as_0130_99_weight",
        "110:NNPDF30_lo_as_0130_100_weight",
        "111:NNPDF30_lo_as_0130_nf_4_0_weight",
        "112:NNPDF30_lo_as_0130_nf_4_1_weight",
        "113:NNPDF30_lo_as_0130_nf_4_2_weight",
        "114:NNPDF30_lo_as_0130_nf_4_3_weight",
        "115:NNPDF30_lo_as_0130_nf_4_4_weight",
        "116:NNPDF30_lo_as_0130_nf_4_5_weight",
        "117:NNPDF30_lo_as_0130_nf_4_6_weight",
        "118:NNPDF30_lo_as_0130_nf_4_7_weight",
        "119:NNPDF30_lo_as_0130_nf_4_8_weight",
        "120:NNPDF30_lo_as_0130_nf_4_9_weight",
        "121:NNPDF30_lo_as_0130_nf_4_10_weight",
        "122:NNPDF30_lo_as_0130_nf_4_11_weight",
        "123:NNPDF30_lo_as_0130_nf_4_12_weight",
        "124:NNPDF30_lo_as_0130_nf_4_13_weight",
        "125:NNPDF30_lo_as_0130_nf_4_14_weight",
        "126:NNPDF30_lo_as_0130_nf_4_15_weight",
        "127:NNPDF30_lo_as_0130_nf_4_16_weight",
        "128:NNPDF30_lo_as_0130_nf_4_17_weight",
        "129:NNPDF30_lo_as_0130_nf_4_18_weight",
        "130:NNPDF30_lo_as_0130_nf_4_19_weight",
        "131:NNPDF30_lo_as_0130_nf_4_20_weight",
        "132:NNPDF30_lo_as_0130_nf_4_21_weight",
        "133:NNPDF30_lo_as_0130_nf_4_22_weight",
        "134:NNPDF30_lo_as_0130_nf_4_23_weight",
        "135:NNPDF30_lo_as_0130_nf_4_24_weight",
        "136:NNPDF30_lo_as_0130_nf_4_25_weight",
        "137:NNPDF30_lo_as_0130_nf_4_26_weight",
        "138:NNPDF30_lo_as_0130_nf_4_27_weight",
        "139:NNPDF30_lo_as_0130_nf_4_28_weight",
        "140:NNPDF30_lo_as_0130_nf_4_29_weight",
        "141:NNPDF30_lo_as_0130_nf_4_30_weight",
        "142:NNPDF30_lo_as_0130_nf_4_31_weight",
        "143:NNPDF30_lo_as_0130_nf_4_32_weight",
        "144:NNPDF30_lo_as_0130_nf_4_33_weight",
        "145:NNPDF30_lo_as_0130_nf_4_34_weight",
        "146:NNPDF30_lo_as_0130_nf_4_35_weight",
        "147:NNPDF30_lo_as_0130_nf_4_36_weight",
        "148:NNPDF30_lo_as_0130_nf_4_37_weight",
        "149:NNPDF30_lo_as_0130_nf_4_38_weight",
        "150:NNPDF30_lo_as_0130_nf_4_39_weight",
        "151:NNPDF30_lo_as_0130_nf_4_40_weight",
        "152:NNPDF30_lo_as_0130_nf_4_41_weight",
        "153:NNPDF30_lo_as_0130_nf_4_42_weight",
        "154:NNPDF30_lo_as_0130_nf_4_43_weight",
        "155:NNPDF30_lo_as_0130_nf_4_44_weight",
        "156:NNPDF30_lo_as_0130_nf_4_45_weight",
        "157:NNPDF30_lo_as_0130_nf_4_46_weight",
        "158:NNPDF30_lo_as_0130_nf_4_47_weight",
        "159:NNPDF30_lo_as_0130_nf_4_48_weight",
        "160:NNPDF30_lo_as_0130_nf_4_49_weight",
        "161:NNPDF30_lo_as_0130_nf_4_50_weight",
        "162:NNPDF30_lo_as_0130_nf_4_51_weight",
        "163:NNPDF30_lo_as_0130_nf_4_52_weight",
        "164:NNPDF30_lo_as_0130_nf_4_53_weight",
        "165:NNPDF30_lo_as_0130_nf_4_54_weight",
        "166:NNPDF30_lo_as_0130_nf_4_55_weight",
        "167:NNPDF30_lo_as_0130_nf_4_56_weight",
        "168:NNPDF30_lo_as_0130_nf_4_57_weight",
        "169:NNPDF30_lo_as_0130_nf_4_58_weight",
        "170:NNPDF30_lo_as_0130_nf_4_59_weight",
        "171:NNPDF30_lo_as_0130_nf_4_60_weight",
        "172:NNPDF30_lo_as_0130_nf_4_61_weight",
        "173:NNPDF30_lo_as_0130_nf_4_62_weight",
        "174:NNPDF30_lo_as_0130_nf_4_63_weight",
        "175:NNPDF30_lo_as_0130_nf_4_64_weight",
        "176:NNPDF30_lo_as_0130_nf_4_65_weight",
        "177:NNPDF30_lo_as_0130_nf_4_66_weight",
        "178:NNPDF30_lo_as_0130_nf_4_67_weight",
        "179:NNPDF30_lo_as_0130_nf_4_68_weight",
        "180:NNPDF30_lo_as_0130_nf_4_69_weight",
        "181:NNPDF30_lo_as_0130_nf_4_70_weight",
        "182:NNPDF30_lo_as_0130_nf_4_71_weight",
        "183:NNPDF30_lo_as_0130_nf_4_72_weight",
        "184:NNPDF30_lo_as_0130_nf_4_73_weight",
        "185:NNPDF30_lo_as_0130_nf_4_74_weight",
        "186:NNPDF30_lo_as_0130_nf_4_75_weight",
        "187:NNPDF30_lo_as_0130_nf_4_76_weight",
        "188:NNPDF30_lo_as_0130_nf_4_77_weight",
        "189:NNPDF30_lo_as_0130_nf_4_78_weight",
        "190:NNPDF30_lo_as_0130_nf_4_79_weight",
        "191:NNPDF30_lo_as_0130_nf_4_80_weight",
        "192:NNPDF30_lo_as_0130_nf_4_81_weight",
        "193:NNPDF30_lo_as_0130_nf_4_82_weight",
        "194:NNPDF30_lo_as_0130_nf_4_83_weight",
        "195:NNPDF30_lo_as_0130_nf_4_84_weight",
        "196:NNPDF30_lo_as_0130_nf_4_85_weight",
        "197:NNPDF30_lo_as_0130_nf_4_86_weight",
        "198:NNPDF30_lo_as_0130_nf_4_87_weight",
        "199:NNPDF30_lo_as_0130_nf_4_88_weight",
        "200:NNPDF30_lo_as_0130_nf_4_89_weight",
        "201:NNPDF30_lo_as_0130_nf_4_90_weight",
        "202:NNPDF30_lo_as_0130_nf_4_91_weight",
        "203:NNPDF30_lo_as_0130_nf_4_92_weight",
        "204:NNPDF30_lo_as_0130_nf_4_93_weight",
        "205:NNPDF30_lo_as_0130_nf_4_94_weight",
        "206:NNPDF30_lo_as_0130_nf_4_95_weight",
        "207:NNPDF30_lo_as_0130_nf_4_96_weight",
        "208:NNPDF30_lo_as_0130_nf_4_97_weight",
        "209:NNPDF30_lo_as_0130_nf_4_98_weight",
        "210:NNPDF30_lo_as_0130_nf_4_99_weight",
        "211:NNPDF30_lo_as_0130_nf_4_100_weight",
        "212:NNPDF30_lo_as_0118_0_weight",
        "213:NNPDF23_lo_as_0130_qed_0_weight",
        "214:NNPDF23_lo_as_0130_qed_1_weight",
        "215:NNPDF23_lo_as_0130_qed_2_weight",
        "216:NNPDF23_lo_as_0130_qed_3_weight",
        "217:NNPDF23_lo_as_0130_qed_4_weight",
        "218:NNPDF23_lo_as_0130_qed_5_weight",
        "219:NNPDF23_lo_as_0130_qed_6_weight",
        "220:NNPDF23_lo_as_0130_qed_7_weight",
        "221:NNPDF23_lo_as_0130_qed_8_weight",
        "222:NNPDF23_lo_as_0130_qed_9_weight",
        "223:NNPDF23_lo_as_0130_qed_10_weight",
        "224:NNPDF23_lo_as_0130_qed_11_weight",
        "225:NNPDF23_lo_as_0130_qed_12_weight",
        "226:NNPDF23_lo_as_0130_qed_13_weight",
        "227:NNPDF23_lo_as_0130_qed_14_weight",
        "228:NNPDF23_lo_as_0130_qed_15_weight",
        "229:NNPDF23_lo_as_0130_qed_16_weight",
        "230:NNPDF23_lo_as_0130_qed_17_weight",
        "231:NNPDF23_lo_as_0130_qed_18_weight",
        "232:NNPDF23_lo_as_0130_qed_19_weight",
        "233:NNPDF23_lo_as_0130_qed_20_weight",
        "234:NNPDF23_lo_as_0130_qed_21_weight",
        "235:NNPDF23_lo_as_0130_qed_22_weight",
        "236:NNPDF23_lo_as_0130_qed_23_weight",
        "237:NNPDF23_lo_as_0130_qed_24_weight",
        "238:NNPDF23_lo_as_0130_qed_25_weight",
        "239:NNPDF23_lo_as_0130_qed_26_weight",
        "240:NNPDF23_lo_as_0130_qed_27_weight",
        "241:NNPDF23_lo_as_0130_qed_28_weight",
        "242:NNPDF23_lo_as_0130_qed_29_weight",
        "243:NNPDF23_lo_as_0130_qed_30_weight",
        "244:NNPDF23_lo_as_0130_qed_31_weight",
        "245:NNPDF23_lo_as_0130_qed_32_weight",
        "246:NNPDF23_lo_as_0130_qed_33_weight",
        "247:NNPDF23_lo_as_0130_qed_34_weight",
        "248:NNPDF23_lo_as_0130_qed_35_weight",
        "249:NNPDF23_lo_as_0130_qed_36_weight",
        "250:NNPDF23_lo_as_0130_qed_37_weight",
        "251:NNPDF23_lo_as_0130_qed_38_weight",
        "252:NNPDF23_lo_as_0130_qed_39_weight",
        "253:NNPDF23_lo_as_0130_qed_40_weight",
        "254:NNPDF23_lo_as_0130_qed_41_weight",
        "255:NNPDF23_lo_as_0130_qed_42_weight",
        "256:NNPDF23_lo_as_0130_qed_43_weight",
        "257:NNPDF23_lo_as_0130_qed_44_weight",
        "258:NNPDF23_lo_as_0130_qed_45_weight",
        "259:NNPDF23_lo_as_0130_qed_46_weight",
        "260:NNPDF23_lo_as_0130_qed_47_weight",
        "261:NNPDF23_lo_as_0130_qed_48_weight",
        "262:NNPDF23_lo_as_0130_qed_49_weight",
        "263:NNPDF23_lo_as_0130_qed_50_weight",
        "264:NNPDF23_lo_as_0130_qed_51_weight",
        "265:NNPDF23_lo_as_0130_qed_52_weight",
        "266:NNPDF23_lo_as_0130_qed_53_weight",
        "267:NNPDF23_lo_as_0130_qed_54_weight",
        "268:NNPDF23_lo_as_0130_qed_55_weight",
        "269:NNPDF23_lo_as_0130_qed_56_weight",
        "270:NNPDF23_lo_as_0130_qed_57_weight",
        "271:NNPDF23_lo_as_0130_qed_58_weight",
        "272:NNPDF23_lo_as_0130_qed_59_weight",
        "273:NNPDF23_lo_as_0130_qed_60_weight",
        "274:NNPDF23_lo_as_0130_qed_61_weight",
        "275:NNPDF23_lo_as_0130_qed_62_weight",
        "276:NNPDF23_lo_as_0130_qed_63_weight",
        "277:NNPDF23_lo_as_0130_qed_64_weight",
        "278:NNPDF23_lo_as_0130_qed_65_weight",
        "279:NNPDF23_lo_as_0130_qed_66_weight",
        "280:NNPDF23_lo_as_0130_qed_67_weight",
        "281:NNPDF23_lo_as_0130_qed_68_weight",
        "282:NNPDF23_lo_as_0130_qed_69_weight",
        "283:NNPDF23_lo_as_0130_qed_70_weight",
        "284:NNPDF23_lo_as_0130_qed_71_weight",
        "285:NNPDF23_lo_as_0130_qed_72_weight",
        "286:NNPDF23_lo_as_0130_qed_73_weight",
        "287:NNPDF23_lo_as_0130_qed_74_weight",
        "288:NNPDF23_lo_as_0130_qed_75_weight",
        "289:NNPDF23_lo_as_0130_qed_76_weight",
        "290:NNPDF23_lo_as_0130_qed_77_weight",
        "291:NNPDF23_lo_as_0130_qed_78_weight",
        "292:NNPDF23_lo_as_0130_qed_79_weight",
        "293:NNPDF23_lo_as_0130_qed_80_weight",
        "294:NNPDF23_lo_as_0130_qed_81_weight",
        "295:NNPDF23_lo_as_0130_qed_82_weight",
        "296:NNPDF23_lo_as_0130_qed_83_weight",
        "297:NNPDF23_lo_as_0130_qed_84_weight",
        "298:NNPDF23_lo_as_0130_qed_85_weight",
        "299:NNPDF23_lo_as_0130_qed_86_weight",
        "300:NNPDF23_lo_as_0130_qed_87_weight",
        "301:NNPDF23_lo_as_0130_qed_88_weight",
        "302:NNPDF23_lo_as_0130_qed_89_weight",
        "303:NNPDF23_lo_as_0130_qed_90_weight",
        "304:NNPDF23_lo_as_0130_qed_91_weight",
        "305:NNPDF23_lo_as_0130_qed_92_weight",
        "306:NNPDF23_lo_as_0130_qed_93_weight",
        "307:NNPDF23_lo_as_0130_qed_94_weight",
        "308:NNPDF23_lo_as_0130_qed_95_weight",
        "309:NNPDF23_lo_as_0130_qed_96_weight",
        "310:NNPDF23_lo_as_0130_qed_97_weight",
        "311:NNPDF23_lo_as_0130_qed_98_weight",
        "312:NNPDF23_lo_as_0130_qed_99_weight",
        "313:NNPDF23_lo_as_0130_qed_100_weight",
        "314:NNPDF23_lo_as_0119_qed_0_weight",
        "315:cteq6l1_0_weight",
        "316:MMHT2014lo68cl_0_weight",
        "317:MMHT2014lo68cl_1_weight",
        "318:MMHT2014lo68cl_2_weight",
        "319:MMHT2014lo68cl_3_weight",
        "320:MMHT2014lo68cl_4_weight",
        "321:MMHT2014lo68cl_5_weight",
        "322:MMHT2014lo68cl_6_weight",
        "323:MMHT2014lo68cl_7_weight",
        "324:MMHT2014lo68cl_8_weight",
        "325:MMHT2014lo68cl_9_weight",
        "326:MMHT2014lo68cl_10_weight",
        "327:MMHT2014lo68cl_11_weight",
        "328:MMHT2014lo68cl_12_weight",
        "329:MMHT2014lo68cl_13_weight",
        "330:MMHT2014lo68cl_14_weight",
        "331:MMHT2014lo68cl_15_weight",
        "332:MMHT2014lo68cl_16_weight",
        "333:MMHT2014lo68cl_17_weight",
        "334:MMHT2014lo68cl_18_weight",
        "335:MMHT2014lo68cl_19_weight",
        "336:MMHT2014lo68cl_20_weight",
        "337:MMHT2014lo68cl_21_weight",
        "338:MMHT2014lo68cl_22_weight",
        "339:MMHT2014lo68cl_23_weight",
        "340:MMHT2014lo68cl_24_weight",
        "341:MMHT2014lo68cl_25_weight",
        "342:MMHT2014lo68cl_26_weight",
        "343:MMHT2014lo68cl_27_weight",
        "344:MMHT2014lo68cl_28_weight",
        "345:MMHT2014lo68cl_29_weight",
        "346:MMHT2014lo68cl_30_weight",
        "347:MMHT2014lo68cl_31_weight",
        "348:MMHT2014lo68cl_32_weight",
        "349:MMHT2014lo68cl_33_weight",
        "350:MMHT2014lo68cl_34_weight",
        "351:MMHT2014lo68cl_35_weight",
        "352:MMHT2014lo68cl_36_weight",
        "353:MMHT2014lo68cl_37_weight",
        "354:MMHT2014lo68cl_38_weight",
        "355:MMHT2014lo68cl_39_weight",
        "356:MMHT2014lo68cl_40_weight",
        "357:MMHT2014lo68cl_41_weight",
        "358:MMHT2014lo68cl_42_weight",
        "359:MMHT2014lo68cl_43_weight",
        "360:MMHT2014lo68cl_44_weight",
        "361:MMHT2014lo68cl_45_weight",
        "362:MMHT2014lo68cl_46_weight",
        "363:MMHT2014lo68cl_47_weight",
        "364:MMHT2014lo68cl_48_weight",
        "365:MMHT2014lo68cl_49_weight",
        "366:MMHT2014lo68cl_50_weight",
        "367:MMHT2014lo_asmzsmallrange_0_weight",
        "368:MMHT2014lo_asmzsmallrange_1_weight",
        "369:MMHT2014lo_asmzsmallrange_2_weight",
        "370:HERAPDF15LO_EIG_0_weight",
        "371:HERAPDF15LO_EIG_1_weight",
        "372:HERAPDF15LO_EIG_2_weight",
        "373:HERAPDF15LO_EIG_3_weight",
        "374:HERAPDF15LO_EIG_4_weight",
        "375:HERAPDF15LO_EIG_5_weight",
        "376:HERAPDF15LO_EIG_6_weight",
        "377:HERAPDF15LO_EIG_7_weight",
        "378:HERAPDF15LO_EIG_8_weight",
        "379:HERAPDF15LO_EIG_9_weight",
        "380:HERAPDF15LO_EIG_10_weight",
        "381:HERAPDF15LO_EIG_11_weight",
        "382:HERAPDF15LO_EIG_12_weight",
        "383:HERAPDF15LO_EIG_13_weight",
        "384:HERAPDF15LO_EIG_14_weight",
        "385:HERAPDF15LO_EIG_15_weight",
        "386:HERAPDF15LO_EIG_16_weight",
        "387:HERAPDF15LO_EIG_17_weight",
        "388:HERAPDF15LO_EIG_18_weight",
        "389:HERAPDF15LO_EIG_19_weight",
        "390:HERAPDF15LO_EIG_20_weight",
        "391:NNPDF30_nlo_as_0118_0_weight",
        "392:NNPDF23_nlo_as_0119_0_weight",
        "393:CT10nlo_0_weight",
        "394:CT10nlo_1_weight",
        "395:CT10nlo_2_weight",
        "396:CT10nlo_3_weight",
        "397:CT10nlo_4_weight",
        "398:CT10nlo_5_weight",
        "399:CT10nlo_6_weight",
        "400:CT10nlo_7_weight",
        "401:CT10nlo_8_weight",
        "402:CT10nlo_9_weight",
        "403:CT10nlo_10_weight",
        "404:CT10nlo_11_weight",
        "405:CT10nlo_12_weight",
        "406:CT10nlo_13_weight",
        "407:CT10nlo_14_weight",
        "408:CT10nlo_15_weight",
        "409:CT10nlo_16_weight",
        "410:CT10nlo_17_weight",
        "411:CT10nlo_18_weight",
        "412:CT10nlo_19_weight",
        "413:CT10nlo_20_weight",
        "414:CT10nlo_21_weight",
        "415:CT10nlo_22_weight",
        "416:CT10nlo_23_weight",
        "417:CT10nlo_24_weight",
        "418:CT10nlo_25_weight",
        "419:CT10nlo_26_weight",
        "420:CT10nlo_27_weight",
        "421:CT10nlo_28_weight",
        "422:CT10nlo_29_weight",
        "423:CT10nlo_30_weight",
        "424:CT10nlo_31_weight",
        "425:CT10nlo_32_weight",
        "426:CT10nlo_33_weight",
        "427:CT10nlo_34_weight",
        "428:CT10nlo_35_weight",
        "429:CT10nlo_36_weight",
        "430:CT10nlo_37_weight",
        "431:CT10nlo_38_weight",
        "432:CT10nlo_39_weight",
        "433:CT10nlo_40_weight",
        "434:CT10nlo_41_weight",
        "435:CT10nlo_42_weight",
        "436:CT10nlo_43_weight",
        "437:CT10nlo_44_weight",
        "438:CT10nlo_45_weight",
        "439:CT10nlo_46_weight",
        "440:CT10nlo_47_weight",
        "441:CT10nlo_48_weight",
        "442:CT10nlo_49_weight",
        "443:CT10nlo_50_weight",
        "444:CT10nlo_51_weight",
        "445:CT10nlo_52_weight",
        "446:MMHT2014nlo68cl_0_weight"
    ]
  

  return config