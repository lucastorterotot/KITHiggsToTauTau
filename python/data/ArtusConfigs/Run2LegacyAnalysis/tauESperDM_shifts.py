#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import os

def build_config(nickname, **kwargs):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))


  # define frequently used conditions
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isData = datasetsHelper.isData(nickname) and (not isEmbedded)
  #isTTbar = re.search("TT(To|_|Jets)", nickname)
  #isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
  #isWjets = re.search("W.?JetsToLNu", nickname)
  year = datasetsHelper.base_dict[nickname]["year"]

  tauES_uncertainties = {
    2016 : {
      "TauEnergyCorrectionOneProngPtDependant": {"down": [0.994 - 0.01, 0.991 - 0.03], "up": [0.994 + 0.01, 0.991 + 0.03]},
      "TauEnergyCorrectionOneProngPiZerosPtDependant": {"down": [0.995 - 0.009, 0.995 - 0.03], "up": [0.995 + 0.009, 0.995 + 0.03]},
      "TauEnergyCorrectionThreeProngPtDependant": {"down": [1.0 - 0.011, 1.0 - 0.03], "up": [1.0 + 0.011, 1.0 + 0.03]},
      # "TauEnergyCorrectionThreeProngPiZerosPtDependant": {"down": [1.0 - 0.011, 1.0 - 0.011], "up": [1.0 + 0.011, 1.0 + 0.011]},
    },
    2017: {
      "TauEnergyCorrectionOneProngPtDependant": {"down": [1.007 - 0.008, 1.004 - 0.03], "up": [1.007 + 0.008, 1.004 + 0.03]},
      "TauEnergyCorrectionOneProngPiZerosPtDependant": {"down": [0.998 - 0.008, 0.998 - 0.03], "up": [0.998 + 0.008, 0.998 + 0.03]},
      "TauEnergyCorrectionThreeProngPtDependant": {"down": [1.001 - 0.009, 1.001 - 0.03], "up": [1.001 + 0.009, 1.001 + 0.03]},
      # "TauEnergyCorrectionThreeProngPiZerosPtDependant": {"down": [0.999 - 0.01, 0.999 - 0.01], "up": [0.999 + 0.01, 0.999 + 0.01]},
    },
    2018: {
      "TauEnergyCorrectionOneProngPtDependant": {"down": [0.987 - 0.011, 0.984 - 0.03], "up": [0.987 + 0.011, 0.984 + 0.03]},
      "TauEnergyCorrectionOneProngPiZerosPtDependant": {"down": [0.995 - 0.009, 0.995 - 0.03], "up": [0.995 + 0.009, 0.995 + 0.03]},
      "TauEnergyCorrectionThreeProngPtDependant": {"down": [0.988 - 0.008, 0.988 - 0.03], "up": [0.988 + 0.008, 0.988 + 0.03]},
      # "TauEnergyCorrectionThreeProngPiZerosPtDependant": {"down": [0.988 - 0.008, 0.988 - 0.008], "up" [0.988 + 0.008,  0.988 + 0.008]},
    }
  }

  tauES_uncertainties_embedded = {
    2016 : {
      "TauEnergyCorrectionOneProng" : {"down" : 0.9934, "up" : 1.0026},
      "TauEnergyCorrectionOneProngPiZeros" : {"down" : 0.9953, "up" : 1.000},
      "TauEnergyCorrectionThreeProng" : {"down" : 0.9823, "up" : 0.9907},
      "TauEnergyCorrectionThreeProngPiZeros" : {"down" : 0.9823, "up" : 0.9907},
    },
    2017: {
      "TauEnergyCorrectionOneProng" : {"down" : 0.9954, "up" : 1.0038},
      "TauEnergyCorrectionOneProngPiZeros" : {"down" : 0.9859, "up" : 0.9932},
      "TauEnergyCorrectionThreeProng" : { "down" : 0.9879, "up" : 0.9969},
      "TauEnergyCorrectionThreeProngPiZeros" : { "down" : 0.9879, "up" : 0.9969},
    },
    2018: {
      "TauEnergyCorrectionOneProng" : {"down" : 0.9928, "up" : 1.0006},
      "TauEnergyCorrectionOneProngPiZeros" : {"down" : 0.9912, "up" : 0.998},
      "TauEnergyCorrectionThreeProng" : { "down" : 0.9894, "up" : 0.9958},
      "TauEnergyCorrectionThreeProngPiZeros" : {"down" : 0.9894, "up" : 0.9958},
    }
  }

  ## fill config:
  # includes
  includes = [
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)

  # explicit configuration
  if not isData and not isEmbedded:
    config["tauEsOneProngUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngUp"]["TauEnergyCorrectionOneProngPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionOneProngPtDependant"]["up"]

    config["tauEsOneProngDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngDown"]["TauEnergyCorrectionOneProngPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionOneProngPtDependant"]["down"]

    config["tauEsOneProngOnePiZeroUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngOnePiZeroUp"]["TauEnergyCorrectionOneProngPiZerosPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionOneProngPiZerosPtDependant"]["up"]

    config["tauEsOneProngOnePiZeroDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngOnePiZeroDown"]["TauEnergyCorrectionOneProngPiZerosPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionOneProngPiZerosPtDependant"]["down"]


    config["tauEsThreeProngUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngUp"]["TauEnergyCorrectionThreeProngPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionThreeProngPtDependant"]["up"]

    config["tauEsThreeProngDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngDown"]["TauEnergyCorrectionThreeProngPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionThreeProngPtDependant"]["down"]


    # config["tauEsThreeProngOnePiZeroUp"] = {
    #  "JetEnergyCorrectionUncertaintyShift" : [0.0]
    # }
    # # config["tauEsThreeProngOnePiZeroUp"]["TauEnergyCorrectionThreeProngPiZeros"] = tauES_uncertainties[year]["TauEnergyCorrectionThreeProngPiZeros"]["up"]
    # config["tauEsThreeProngOnePiZeroUp"]["TauEnergyCorrectionThreeProngPiZerosPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionThreeProngPiZerosPtDependant"]["up"]

    # config["tauEsThreeProngOnePiZeroDown"] = {
    #  "JetEnergyCorrectionUncertaintyShift" : [0.0]
    # }
    # #config["tauEsThreeProngOnePiZeroDown"]["TauEnergyCorrectionThreeProngPiZeros"] = tauES_uncertainties[year]["TauEnergyCorrectionThreeProngPiZeros"]["down"]
    # config["tauEsThreeProngOnePiZeroDown"]["TauEnergyCorrectionThreeProngPiZerosPtDependant"] = tauES_uncertainties[year]["TauEnergyCorrectionThreeProngPiZerosPtDependant"]["down"]
  elif isEmbedded:
    config["tauEsOneProngUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngUp"]["TauEnergyCorrectionOneProng"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionOneProng"]["up"]

    config["tauEsOneProngDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngDown"]["TauEnergyCorrectionOneProng"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionOneProng"]["down"]


    config["tauEsOneProngOnePiZeroUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngOnePiZeroUp"]["TauEnergyCorrectionOneProngPiZeros"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionOneProngPiZeros"]["up"]

    config["tauEsOneProngOnePiZeroDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngOnePiZeroDown"]["TauEnergyCorrectionOneProngPiZeros"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionOneProngPiZeros"]["down"]


    config["tauEsThreeProngUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngUp"]["TauEnergyCorrectionThreeProng"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionThreeProng"]["up"]

    config["tauEsThreeProngDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngDown"]["TauEnergyCorrectionThreeProng"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionThreeProng"]["down"]

    config["tauEsThreeProngOnePiZeroUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngOnePiZeroUp"]["TauEnergyCorrectionThreeProngPiZeros"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionThreeProngPiZeros"]["up"]

    config["tauEsThreeProngOnePiZeroDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngOnePiZeroDown"]["TauEnergyCorrectionThreeProngPiZeros"] = tauES_uncertainties_embedded[year]["TauEnergyCorrectionThreeProngPiZeros"]["down"]

  return config
