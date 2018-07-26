import os, re
import commands
import math, time
import sys
from ROOT import TObject, TFile, TH1, TH1F
#from Analysis.ALPHA.samples import sample
#from array import array

LUMI = 35900 #in pb-1 (2016)

path = '/beegfs/desy/user/hezhiyua/qcd_data/Skim/'
#fName = 'QCD_HT100To200_1j_skimed.root'
#fName = 'QCD_HT50To100_1j_skimed.root'
fName = 'QCD_HT200To300_1j_skimed.root'

fName = path + fName

file1 = TFile( fName , "UPDATE" )
#file1.cd('ntuple;1')
if '50To100' in fName:
    xs = 246300000
elif '100To200' in fName:
    xs = 28060000
elif '200To300' in fName:
    xs = 1710000

tree = file1.Get("tree44")
nevents = tree.GetEntries()
#weight = LUMI * xs / float(nevents)
weight = 1#/float(nevents)

tree.SetWeight(weight)
tree.AutoSave()
print 'Weight:'
print weight
