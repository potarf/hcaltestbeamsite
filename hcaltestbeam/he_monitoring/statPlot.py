#!/usr/bin/env python
#######################################################################
#  statPlot.py							      #
#								      #
#  Parse an ngfec_auto log file and plots stats as a function of time #
#								      #
#######################################################################

import sys
from argparse import ArgumentParser
import ROOT
from pprint import pprint
from ROOT import TGraph, TMultiGraph, TH1D, TLegend, TCanvas, TPad, gStyle, kRed, kCyan, kGreen, kBlack
ROOT.gROOT.SetBatch(True)

COLORS = [kRed, kCyan, kGreen, kBlack]
MARKERS = [21, 22, 29, 33] 

parser = ArgumentParser()
parser.add_argument("log", help="log file from ngfec_auto")
args = parser.parse_args()


readings = []
minT = 9999.0
maxT = -9999.0
minH = 101.0
maxH = -1.0
with open(args.log, "r") as f:
    for line in f:
	data = line.split()
	entry = {}
	entry["date"] = data[0]
	entry["time"] = data[1]
	entry["temp"] = [float(data[i]) for i in xrange(2, 6)]
	entry["hum"]  = [float(data[i]) for i in xrange(6, 10)]
	minT = min(minT, min(entry["temp"]))
	maxT = max(maxT, max(entry["temp"]))
	minH = min(minH, min(entry["hum"]))
	maxH = max(maxH, max(entry["hum"]))
	readings.append(entry)

#pprint(readings)
#print "Min,Max temp = (%f, %f)" % (minT, maxT)
#print "Max humidity =", maxH
#sys.exit()

# Stat options
# e: entries 
# m: mean
# r: std dev
gStyle.SetOptStat("emr")
date = readings[0]["date"]

tempG = []
humG = []

tempMG = TMultiGraph()
humMG = TMultiGraph()


for i in range(len(readings[0]["temp"])):
    tempG.append(TGraph())
    tempG[i].SetLineColor(COLORS[i])
    tempG[i].SetLineWidth(2)
    tempG[i].SetMarkerStyle(MARKERS[i])
    tempG[i].SetMarkerSize(2)
    tempG[i].SetMarkerColor(COLORS[i])

    humG.append(TGraph())
    humG[i].SetLineColor(COLORS[i])
    humG[i].SetLineWidth(2)
    humG[i].SetMarkerStyle(MARKERS[i])
    humG[i].SetMarkerSize(2)
    humG[i].SetMarkerColor(COLORS[i])


tempH = TH1D("Temp", "RM Temperatures (^{o}C)", 20, minT - 0.1, maxT + 0.1)
tempH.SetFillColor(kRed)

humH = TH1D("Humidity", "RBX Humidity (%)", 20, -0.5, maxH + 0.5)
humH.SetFillColor(kCyan)

for i,entry in enumerate(readings):
    for rm in range(4):
	# Update temp and humidity graphs
	temp = entry["temp"][rm]
	tempG[rm].SetPoint(i, i, temp)
	hum = entry["hum"][rm]
	humG[rm].SetPoint(i, i, hum)
	tempH.Fill(temp)
	humH.Fill(hum)


# Graph temps
c = TCanvas("c", "c", 1200, 1200)
l = TLegend(0.85, 0.8, 0.99, 0.99)
pad = TPad("p","p", 0.05, 0.05, 1.0, 1.0)
pad.cd()
for rm in range(4):
    l.AddEntry(tempG[rm], "RM%d" % (rm+1), "pl")
    tempMG.Add(tempG[rm])
tempMG.Draw("alp")
pad.Update()
tempMG.SetTitle("RBX Temperature (^{o}C);Time;Temp (^{o}C)")
l.Draw()
c.cd()
pad.Draw()


# Set up x axis labels
tempMG.GetXaxis().SetNdivisions(len(readings))
date = "" 
for i in range(len(readings)):
    # If new date, print date and time
    if date != readings[i]["date"]:
        date = readings[i]["date"]
	tempMG.GetXaxis().SetBinLabel(tempMG.GetXaxis().FindBin(i), "#splitline{%s}{%s}"%(date, readings[i]["time"]))
    else:
	tempMG.GetXaxis().SetBinLabel(tempMG.GetXaxis().FindBin(i), readings[i]["time"])


tempMG.GetXaxis().SetTitleOffset(2.4)
tempMG.GetYaxis().SetTitleOffset(2.1)
pad.Update()
c.SaveAs("Temp_graphs.jpg")


c.Clear()
pad = TPad("p","p", 0.05,0.0, 1.0, 1.0)
pad.cd()
tempH.SetTitle("RM Temperatures (^{o}C)")
tempH.GetXaxis().SetTitle("Temp (^{o}C)")
tempH.GetYaxis().SetTitle("Entries")
#tempH.GetXaxis().SetNdivisions(len(temps))
tempH.Draw("HIST")
c.cd()
pad.Draw()
c.SaveAs("Temp_histo.jpg")


# Graph humidities
c.Clear()
l = TLegend(0.85, 0.8, 0.99, 0.99)
pad = TPad("p","p", 0.05, 0.05, 1.0, 1.0)
pad.cd()
for rm in range(4):
    l.AddEntry(humG[rm], "RM%d" % (rm+1), "pl")
    humMG.Add(humG[rm])
humMG.Draw("alp")
pad.Update()
humMG.SetTitle("RBX Humidity (%);Time;Humidity (%)")
l.Draw()
c.cd()
pad.Draw()


# Set up x axis labels
humMG.GetXaxis().SetNdivisions(len(readings))
date = "" 
for i in range(len(readings)):
    # If new date, print date and time
    if date != readings[i]["date"]:
        date = readings[i]["date"]
	humMG.GetXaxis().SetBinLabel(humMG.GetXaxis().FindBin(i), "#splitline{%s}{%s}"%(date, readings[i]["time"]))
    else:
	humMG.GetXaxis().SetBinLabel(humMG.GetXaxis().FindBin(i), readings[i]["time"])


humMG.GetXaxis().SetTitleOffset(2.4)
humMG.GetYaxis().SetTitleOffset(2.1)
pad.Update()
c.SaveAs("Hum_graphs.jpg")


c.Clear()
pad = TPad("p","p", 0.05,0.0, 1.0, 1.0)
pad.cd()
humH.SetTitle("RM Humidities (%)")
humH.GetXaxis().SetTitle("Humidity (%)")
humH.GetYaxis().SetTitle("Entries")
humH.Draw("HIST")
c.cd()
pad.Draw()
c.SaveAs("Hum_histo.jpg")
"""
graph(readings, humG, "RBX Humidity (%)", "Time", "Humidity (%)", "Hum")

"""


def graph(dataReadings, vals, title, xTitle, yTitle, outF):
    mg = TMultiGraph()
    c = TCanvas("c", "c", 1200, 1200)
    l = TLegend(0.85, 0.8, 0.99, 0.99)
    pad = TPad("p","p", 0.05, 0.05, 1.0, 1.0)
    pad.cd()
    for rm in range(len(vals)):
	l.AddEntry(tempG[rm], "RM%d" % (rm+1), "pl")
	mg.Add(tempG[rm])
    mg.Draw("alp")
    pad.Update()
    mg.SetTitle(title + ";" + xTitle + ";" + yTitle)
    l.Draw()
    c.cd()
    pad.Draw()
    
    mg.GetXaxis().SetNdivisions(len(dataReadings))
    date = "" 
    for i in range(len(dataReadings)):
	# If new date, print date and time
	if date != dataReadings[i]["date"]:
	    date = dataReadings[i]["date"]
	    mg.GetXaxis().SetBinLabel(mg.GetXaxis().FindBin(i), "#splitline{%s}{%s}"%(date, dataReadings[i]["time"]))
	else:
	    mg.GetXaxis().SetBinLabel(mg.GetXaxis().FindBin(i), dataReadings[i]["time"])


    mg.GetXaxis().SetTitleOffset(2.4)
    mg.GetYaxis().SetTitleOffset(2.1)
    pad.Update()
    c.SaveAs(outF + "_graph.jpg")
