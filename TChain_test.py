from __future__ import division
from ROOT import ROOT, gROOT, TDirectory, TFile, gFile, TBranch, TLeaf, TTree
from ROOT import TText, TPaveLabel, TLatex, TGraphErrors, TLine, gPad
from ROOT import TH1, TH1F, TH2F, TChain, TCanvas, TLegend, gStyle
from array import array
import math
from timeit import default_timer as timer

start= timer()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Settings~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gStyle.SetOptStat(0)
path0 = '/beegfs/desy/user/hezhiyua/workdir/'
path1 = "/beegfs/desy/user/hezhiyua/workdir/fplot/p/"

chn = TChain('tree44')#TChain('Jet1s')

chn.Add( path0 + "QCD_HT50To100_1j_skimed.root" )
chn.Add( path0 + "QCD_HT100To200_1j_skimed.root" )
#chn.Add("")

chn.Draw("Jet1s.pt")



import time
time.sleep(8)
