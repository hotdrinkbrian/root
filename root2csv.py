import ROOT
import pandas
import root_numpy
import numpy as np
from ROOT import TDirectory, TFile, gFile, TBranch, TTree

infname_sig = '/home/hezhiyua/desktop/test/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8.root'
infname_bkg = '/home/hezhiyua/desktop/test/VBFHToBB_M-125_13TeV_powheg_pythia8.root'

fs = TFile(infname_sig,"r")
fb = TFile(infname_bkg,"r")

tree_sig = fs.Get('reconstruction;1').Get('tree')
tree_bkg = fb.Get('reconstruction;1').Get('tree')
#set up DataFrames
df_sig = pandas.DataFrame(root_numpy.tree2array(tree_sig, branches=["Jet1.pt","Jet1.cm","Jet1.phf","Jet1.chf","Jet1.muf","Jet1.nhf","Jet1.nm","Jet1.elf","Jet1.chm","nGenBquarks"]))
df_bkg = pandas.DataFrame(root_numpy.tree2array(tree_bkg, branches=["Jet1.pt","Jet1.cm","Jet1.phf","Jet1.chf","Jet1.muf","Jet1.nhf","Jet1.nm","Jet1.elf","Jet1.chm","nGenBquarks"]))

df_sig.to_csv('/home/hezhiyua/scp/sig.csv')
df_bkg.to_csv('/home/hezhiyua/scp/bkg.csv')
