import sys
from time import time, sleep
from datetime import datetime

from re import search, escape
import os
import subprocess
import pexpect

def progress(i = 0, n = 0, name = None, k = 50): # i: iterator, k: total length of progress bar, n: total number of events
	stdstore = sys.stdout
	sys.stdout = sys.__stdout__
	if i == n:
		print " \t[" + "="*k + "]" + "\t{0:.2f}%".format(100)
		print "\033[J\033[F"
		sys.stdout = stdstore
	else:
		if i%4 == 0:
			print " \t[" + "="*(i*k/n) + "-" + " "*(k-1-i*k/n) + "]" + "\t{0:.2f}%".format(100.*i/n)
		if (i+1)%4 == 0:
			print " \t[" + "="*(i*k/n) + "/" + " "*(k-1-i*k/n) + "]" + "\t{0:.2f}%".format(100.*i/n)
		if (i+2)%4 == 0:
			print " \t[" + "="*(i*k/n) + "|" + " "*(k-1-i*k/n) + "]" + "\t{0:.2f}%".format(100.*i/n)
		if (i+3)%4 == 0:
			print " \t[" + "="*(i*k/n) + "\\" + " "*(k-1-i*k/n) + "]" + "\t{0:.2f}%".format(100.*i/n)
		print "\033[J",
		sys.stdout = stdstore
		print "\t\t" + str(name)
		sys.stdout = sys.__stdout__
		print "\033[F"*2,
		sys.stdout = stdstore

cmds_default = ["quit"]

def send_commands(cmds=cmds_default, script=False, raw=False, progbar=False, port = 4342, control_hub = "hcal904daq02"):
	# Arguments and variables
	output = []
	raw_output = ""
	if control_hub != False and port:		# Potential bug if "port=0" ... (Control_hub should be allowed to be None.)
		## Parse commands:
		if isinstance(cmds, str):
			cmds = [cmds]
		if not script:
			if "quit" not in cmds:
				cmds.append("quit")
		else:
			cmds = [c for c in cmds if c != "quit"]		# "quit" can't be in a ngFEC script.
			cmds_str = ""
			for c in cmds:
				cmds_str += "{0}\n".format(c)
			file_script = "ngfec_script"
			with open(file_script, "w") as out:
				out.write(cmds_str)
		
		# Prepare the ngfec arguments:
		ngfec_cmd = 'ngFEC.exe -z -c -p {0}'.format(port)
		if control_hub != None:
			ngfec_cmd += " -H {0}".format(control_hub)
		
		# Send the ngfec commands:
#		print ngfec_cmd
		p = pexpect.spawn(ngfec_cmd)#, timeout=100, maxread=20000)
#		print p.pid
		if not script:
			for i, c in enumerate(cmds):
#				print c
				p.sendline(c)
				if c != "quit":
					if progbar:
						progress(i, len(cmds), cmds[i].split()[1])
					t0 = time()
					p.expect("{0}\s?#((\s|E)[^\r^\n]*)".format(escape(c)))
					t1 = time()
#					print [p.match.group(0)]
					output.append({
						"cmd": c,
						"result": p.match.group(1).strip().replace("'", ""),
						"times": [t0, t1],
					})
					raw_output += p.before + p.after
		else:
			#p.sendline("< {0}".format(file_script))
			p.send("< {0}".format(file_script))
			p.send("\n")
			for i, c in enumerate(cmds):
				# Deterimine how long to wait until the first result is expected:
				if i == 0:
					timeout = max([30, int(0.0075*len(cmds))])
#					print i, c, timeout
				else:
					timeout = 30		# pexpect default
#					print i, c, timeout
#				print i, c, timeout
				
				# Send commands:
				if progbar:
					progress(i, len(cmds), cmds[i].split()[1])
				t0 = time()
				p.expect("{0}\s?#((\s|E)[^\r^\n]*)".format(escape(c)), timeout=timeout)
				t1 = time()
				#print "pexpect output0: ",[p.match.group(0)]
				output.append({
					"cmd": c,
					"result": p.match.group(1).strip().replace("'", ""),
					"times": [t0, t1],
				})
				raw_output += p.before + p.after
			#p.sendline("quit")
			p.send("quit")
			p.send("\n")
		if progbar:
			progress()
		p.expect(pexpect.EOF)
		raw_output += p.before
		#output[-1]["result"] += p.before
		#print "raw_output = ",raw_output
#		sleep(1)		# I need to make sure the ngccm process is killed.
		p.close()
#		print "closed"
		if raw:
			return raw_output
		else:
			return output

