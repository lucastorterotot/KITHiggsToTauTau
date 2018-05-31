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
  
  config["PlotlevelFilterExpressionQuantities"] = [
    "rerunDiscriminationByIsolationMVAOldDMrun2v1VVLoose2017_1",
    "rerunDiscriminationByIsolationMVAOldDMrun2v1VVLoose2017_2"
  ]
  config["PlotlevelFilterExpression"] = "rerunDiscriminationByIsolationMVAOldDMrun2v1VVLoose2017_1 > 0.5 && rerunDiscriminationByIsolationMVAOldDMrun2v1VVLoose2017_2 > 0.5"
  
  return config
