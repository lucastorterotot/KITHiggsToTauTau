#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_list():
  quantities_list = [
    "run",
    "lumi",
    "evt",
   # "m_vis",
    "pt_t", "pt_p",
    "eta_t", "eta_p",
    "phi_t", "phi_p",
    "iso_t",
    "id_p",
    "m_ll",
    "trg_singlemuon_24",
    "trg_singlemuon_27",
    "trg_crossmuon_mu20tau27",
    "trg_monitor_mu20tau27",
    "trg_monitor_mu24tau35_medium_tightID",
    "trg_monitor_mu24tau35_tight",
    "trg_monitor_mu24tau35_tight_tightID",
    "trg_singletau_leading",
    "trg_singletau_trailing",
    "metPt",
    "mt", #transverse mass of muon and met
    "againstElectronVLooseMVA6_p",
    "againstElectronLooseMVA6_p",
    "againstElectronMediumMVA6_p",
    "againstElectronTightMVA6_p",
    "againstElectronVTightMVA6_p",
    "againstMuonLoose3_p",
    "againstMuonTight3_p",
    "byIsolationMVArun2017v2DBoldDMwLTraw2017_p",
    "byVVLooseIsolationMVArun2017v2DBoldDMwLT2017_p",
    "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_p",
    "byLooseIsolationMVArun2017v2DBoldDMwLT2017_p",
    "byMediumIsolationMVArun2017v2DBoldDMwLT2017_p",
    "byTightIsolationMVArun2017v2DBoldDMwLT2017_p",
    "byVTightIsolationMVArun2017v2DBoldDMwLT2017_p",
    "byVVTightIsolationMVArun2017v2DBoldDMwLT2017_p",
    "byIsolationMVArun2017v1DBoldDMwLTraw2017_p",
    "byVVLooseIsolationMVArun2017v1DBoldDMwLT2017_p",
    "byVLooseIsolationMVArun2017v1DBoldDMwLT2017_p",
    "byLooseIsolationMVArun2017v1DBoldDMwLT2017_p",
    "byMediumIsolationMVArun2017v1DBoldDMwLT2017_p",
    "byTightIsolationMVArun2017v1DBoldDMwLT2017_p",
    "byVTightIsolationMVArun2017v1DBoldDMwLT2017_p",
    "byVVTightIsolationMVArun2017v1DBoldDMwLT2017_p",
    "decayModeFinding_p",
    "decayMode_p",
    "isOS",
    ]

  return quantities_list
