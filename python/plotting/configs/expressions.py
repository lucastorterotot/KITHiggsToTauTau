
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import Artus.HarryPlotter.utility.expressions as expressions
import os
from string import strip


class ExpressionsDict(expressions.ExpressionsDict):
	def __init__(self, additional_expressions=None):
		super(ExpressionsDict, self).__init__(additional_expressions=additional_expressions)

		self.expressions_dict["integral"] = "0.5"

		# blinding (of data)
		for channel in ["tt", "mt", "et", "em", "mm", "ee"]:
			pass # self.expressions_dict["blind_"+channel+"_svfitMass"] = "((svfitMass<100.0)+(svfitMass>200.0))"

		# category cuts
		self.expressions_dict["cat_inclusive"] = "1.0"
		self.expressions_dict["cat_0jet"] = "njetspt20 < 1"
		self.expressions_dict["cat_1jet"] = "(njetspt20 > 0)*(njetspt20 < 2)"
		self.expressions_dict["cat_2jet"] = "njetspt20 > 1"

		# Z->tautau categories
		for channel in ["tt", "mt", "et", "em", "mm", "ee"]:
			self.expressions_dict["catZtt13TeV_"+channel+"_inclusive"] = "1.0"
			self.expressions_dict["catZtt13TeV_"+channel+"_2jet_inclusive"] = "(njetspt30>1)"
			self.expressions_dict["catZtt13TeV_"+channel+"_1jet_inclusive"] = "(njetspt30>0)*(njetspt30<2)"
			self.expressions_dict["catZtt13TeV_"+channel+"_0jet_inclusive"] = "(njetspt30<1)"

		# H->tautau categories
		for channel in ["tt", "mt", "et", "em", "mm", "ee"]:
			pt_var = "pt_2" if channel in ["mt", "et", "em"] else "pt_1"
			pt_cut = "35.0" if channel in ["mt", "et", "tt"] else "35.0"
		#CP-studies
			self.expressions_dict["catHtt13TeV_"+channel+"_CP_mt"] = "(genPhiStarCP>-10) * (TauMProngEnergy >= 0.44 && TauPProngEnergy >= 0.44)*(decayMode_2 < 5)"
			self.expressions_dict["catHtt13TeV_"+channel+"_CP_et"] = "(genPhiStarCP>-10) * (TauMProngEnergy >= 0.44 && TauPProngEnergy >= 0.44)*(decayMode_2 < 5)"
			self.expressions_dict["catHtt13TeV_"+channel+"_CP_em"] = "(genPhiStarCP>-10) * (TauMProngEnergy >= 0.44 && TauPProngEnergy >= 0.44)"
			self.expressions_dict["catHtt13TeV_"+channel+"_CP_tt"] = "(genPhiStarCP>-10) * (TauMProngEnergy >= 0.55 && TauPProngEnergy >= 0.55)"
					
			self.expressions_dict["catHtt13TeV_"+channel+"_inclusive"] = "(1.0)"
			self.expressions_dict["catHtt13TeV_"+channel+"_inclusivemt40"] = "(1.0)"
			self.expressions_dict["catHtt13TeV_"+channel+"_2jet_inclusive"] = "(njetspt30>1)"
			self.expressions_dict["catHtt13TeV_"+channel+"_2jet_vbf"] = self.expressions_dict["catHtt13TeV_"+channel+"_2jet_inclusive"]+"*(mjj>200.0)*(jdeta>2.0)"
			self.expressions_dict["catHtt13TeV_"+channel+"_1jet_inclusive"] = ("(! ({vbf}))".format(
					vbf=self.expressions_dict["catHtt13TeV_"+channel+"_2jet_vbf"]
			))+"*(njetspt30>0)"
			self.expressions_dict["catHtt13TeV_"+channel+"_1jet_high"] = self.expressions_dict["catHtt13TeV_"+channel+"_1jet_inclusive"]+("*({pt_var}>{pt_cut})".format(pt_var=pt_var, pt_cut=pt_cut))
			self.expressions_dict["catHtt13TeV_"+channel+"_1jet_low"] = self.expressions_dict["catHtt13TeV_"+channel+"_1jet_inclusive"]+("*({pt_var}<={pt_cut})".format(pt_var=pt_var, pt_cut=pt_cut))
			self.expressions_dict["catHtt13TeV_"+channel+"_0jet_inclusive"] = ("(! ({vbf}))*(! ({onejet}))".format(
					vbf=self.expressions_dict["catHtt13TeV_"+channel+"_2jet_vbf"],
					onejet=self.expressions_dict["catHtt13TeV_"+channel+"_1jet_inclusive"]
			))
			self.expressions_dict["catHtt13TeV_"+channel+"_0jet_high"] = self.expressions_dict["catHtt13TeV_"+channel+"_0jet_inclusive"]+("*({pt_var}>{pt_cut})".format(pt_var=pt_var, pt_cut=pt_cut))
			self.expressions_dict["catHtt13TeV_"+channel+"_0jet_low"] = self.expressions_dict["catHtt13TeV_"+channel+"_0jet_inclusive"]+("*({pt_var}<={pt_cut})".format(pt_var=pt_var, pt_cut=pt_cut))

		for channel in ["et","mt","tt","em"]:
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_inclusive"] = "(1.0)"
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_inclusivemt40"] = "(1.0)"
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_nobtag"] = "(nbtag==0)"
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_btag"] = "(njets<=1)*(nbtag>=1)"
		for channel in ["et","mt","tt"]:
			pt_var = "pt_2" if channel in ["mt", "et"] else "pt_1"
			pt_cut_nobtag_high = "60.0" if channel in ["mt", "et"] else "80.0"
			pt_cut_nobtag_medium = "45.0" if channel in ["mt", "et"] else "60.0"
			pt_cut_nobtag_low = "30.0" if channel in ["mt", "et"] else "45.0"
			pt_cut_btag_high = "45.0" if channel in ["mt", "et"] else "60.0"
			pt_cut_btag_low = "30.0" if channel in ["mt", "et"] else "45.0"
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_nobtag_high"] = self.expressions_dict["catHttMSSM13TeV_"+channel+"_nobtag"]+"*({pt_var}>{pt_cut})".format(pt_var=pt_var, pt_cut=pt_cut_nobtag_high)
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_nobtag_medium"] = self.expressions_dict["catHttMSSM13TeV_"+channel+"_nobtag"]+"*({pt_var}<={pt_cut_1})*({pt_var}>{pt_cut_2})".format(pt_var=pt_var, pt_cut_1=pt_cut_nobtag_high, pt_cut_2=pt_cut_nobtag_medium)
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_nobtag_low"] = self.expressions_dict["catHttMSSM13TeV_"+channel+"_nobtag"]+"*({pt_var}<={pt_cut_1})*({pt_var}>{pt_cut_2})".format(pt_var=pt_var, pt_cut_1=pt_cut_nobtag_medium, pt_cut_2=pt_cut_nobtag_low)
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_btag_high"] = self.expressions_dict["catHttMSSM13TeV_"+channel+"_btag"]+"*({pt_var}>{pt_cut})".format(pt_var=pt_var, pt_cut=pt_cut_btag_high)
			self.expressions_dict["catHttMSSM13TeV_"+channel+"_btag_low"] = self.expressions_dict["catHttMSSM13TeV_"+channel+"_btag"]+"*({pt_var}<={pt_cut_1})*({pt_var}>{pt_cut_2})".format(pt_var=pt_var, pt_cut_1=pt_cut_btag_high, pt_cut_2=pt_cut_btag_low)

		# MVA Htt categories
		import Artus.Utility.jsonTools as jsonTools
		for channel in ["tt", "mt", "et", "em"]:
			for classic in ["0jet_high", "0jet_low", "1jet_high", "1jet_low", "2jet_vbf"]:
				self.expressions_dict["{channel}_{classic}".format(channel=channel, classic=classic)] = self.expressions_dict["catHtt13TeV_{channel}_{classic}".format(channel=channel, classic=classic)]
		#========================================Copy here!========================================
			expressions_path = os.path.expandvars("$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/mva_configs/%s_expressions.cfg"%channel)
			if not os.path.exists(expressions_path):
				continue
			self.expressions_dict["%s_inclusive"%(channel)] = "(1.0)"
			with open(expressions_path, "r") as exps:
				regular_name = ""
				for line in exps:
					#log.info(line)
					vbf, name, values = map(strip, line.split(" : "))
					values = map(float, values.split(" "))
					values.pop(0)
					values.pop(-1)
					if vbf == "regular_name":
						self.expressions_dict["%s_%s_signal"%(channel,name)] = "(%f <= %s)"%(values[1], name)
						self.expressions_dict["%s_%s_mixed"%(channel,name)] = "(%f <= %s && %s < %f)"%(values[0], name, name, values[1])
						self.expressions_dict["%s_%s_bkg"%(channel,name)] = "(%s < %f)"%(name, values[0])
						regular_name= name
						continue
					elif vbf == "vbf_tagger":
						if regular_name == "":
							log.fatal("Please check if cuts in file %s are in correct order"%expressions_path)
							sys.exit()
						self.expressions_dict["{channel}_{vbf_tagger}_{mva_name}_tagged_signal".format(
							channel=channel, vbf_tagger=name, mva_name=regular_name)]=self.expressions_dict["{channel}_{reg_name}_signal".format(channel=channel, reg_name=regular_name)]+"*({upper} <= {vbf_tagger})".format(upper=values[0], vbf_tagger=name)
						self.expressions_dict["{channel}_{vbf_tagger}_{mva_name}_not_tagged_signal".format(
							channel=channel, vbf_tagger=name, mva_name=regular_name)]=self.expressions_dict["{channel}_{reg_name}_signal".format(channel=channel, reg_name=regular_name)]+"*({lower} > {vbf_tagger})".format(lower=values[0], vbf_tagger=name)
			expressions_path = os.path.expandvars("$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/mva_configs/%s_shift_expressions.cfg"%channel)
			if not os.path.exists(expressions_path):
				continue
			shifts_dict = jsonTools.JsonDict(expressions_path)
			self.expressions_dict.update(shifts_dict)
		#========================================Copy here!=======================================
		self.expressions_dict["cat_OneProng"] = "(decayMode_2 == 0)"
		self.expressions_dict["catOneProng"] = self.expressions_dict["cat_OneProng"]
		for channel in ["mt", "et"]:
			self.expressions_dict["catOneProng_"+channel] = self.expressions_dict["catOneProng"]

		self.expressions_dict["cat_OneProngPiZeros"] = "(decayMode_2 >= 1)*(decayMode_2 <= 2)"
		self.expressions_dict["catOneProngPiZeros"] = self.expressions_dict["cat_OneProngPiZeros"]
		for channel in ["mt", "et"]:
			self.expressions_dict["catOneProngPiZeros_"+channel] = self.expressions_dict["catOneProngPiZeros"]

		self.expressions_dict["cat_ThreeProng"] = "(decayMode_2 == 10)"
		self.expressions_dict["catThreeProng"] =self.expressions_dict["cat_ThreeProng"]
		for channel in ["mt", "et"]:
			self.expressions_dict["catThreeProng_"+channel] = self.expressions_dict["catThreeProng"]

		self.expressions_dict["cat_AllDMs"] = "(decayMode_2 >= 0)*(decayMode_2 <= 10)"
		self.expressions_dict["catAllDMs"] =self.expressions_dict["cat_AllDMs"]
		for channel in ["mt", "et"]:
			self.expressions_dict["catAllDMs_"+channel] = self.expressions_dict["catAllDMs"]

		self.expressions_dict["cat_AllDMsNotOneProng"] = "(decayMode_2 >= 1)*(decayMode_2 <= 10)"
		self.expressions_dict["catAllDMsNotOneProng"] =self.expressions_dict["cat_AllDMsNotOneProng"]
		for channel in ["mt", "et"]:
			self.expressions_dict["catAllDMsNotOneProng_"+channel] = self.expressions_dict["catAllDMsNotOneProng"]

		replacements = {
			"0jet" : "zerojet",
			"1jet" : "onejet",
			"2jet" : "twojet",
		}
		for short_expression, long_expression in self.expressions_dict.items():
			if any([replacement in short_expression for replacement in replacements.keys()]):
				new_short_expression = short_expression
				for replacement in replacements.iteritems():
					new_short_expression = new_short_expression.replace(*replacement)
				self.expressions_dict[new_short_expression] = long_expression
