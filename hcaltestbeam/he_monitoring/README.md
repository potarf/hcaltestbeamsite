# HE_Monitoring
Monitor HE temperature and humidity for the building 904 burn-in.

To be run from hcal904daq02. First source the following scripts:

source ~hcalsw/bin/env.sh ;
source ~hcalsw/bin/getHCHostname.sh

Query the ngccm server with commands listed in a text file (commandList.txt for example). Then pass this file as an argument to ngfec_auto.py to record the output and create some plots of the results:

./ngfec_auto.py commandList.txt

The paresd output will be stored in statLog.txt. To make plots of all the values in the log pass this log file as an argument to statPlot.py

./statPlot.py statLog.txt
