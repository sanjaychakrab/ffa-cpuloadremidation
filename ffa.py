#!/usr/bin/python -tt
# please read README.cpuloadremidation
r"""
This module is needs to run to check the system helth ( curretnly CPU only) and remediate is it reaches the threshold.
"""

import datetime,os,sys,shutil

from findload1sec import callload1
from extractcpuvalue import fnormal
from extractcpuvalue import highload
from extractcpuvalue import maxload

from detection import checkload
from operation import killhighloadpid
##log file

config_dir = "/var/tmp/ffa/config"
Log_file = "ffa_logs"

def check_ffa_setup():
 print 'from check_ffa_setup'
 try:
  if not os.path.exists(config_dir):
      print "Please run ffaintall.py"
      import sys; sys.exit(1)
 except:
  print "FFA SetupError "




def compare(current, normal, high, maxhigh ):
	if current <= normal:
	  statement = "OK ... The current load is   %1.2f . The normal load is, %1.2f"  %(current, normal) 
          #print statement
	  
          op = 'OK'
	elif current > normal and current < maxhigh:
	  statement = "WARM ... The current load is   %1.2f . The high load (not max) is, %1.2f" %(current, high ) 
	  print statement
	  op = 'WARM'
	elif current >= maxhigh:#   and current  >= maxhigh:
	  statement = "HOT ... The current load is   %1.2f . The Max load is, %1.2f" %(current, maxhigh )
          print statement
          op = 'FIRE'	  
	else:
	 print 'Something wrong in compare'
	 op = 'ERROR'
	#return { op, statement }
	os.chdir(config_dir)
  	logs = open(Log_file, "a")
  	logs.write (statement)
	logs.write("\n")
  	logs.close()

	return op
	
def action(status):
	if status in ('OK'):
	   result = "No action needed.. %s " %(status)
	elif status in ('WARM'):
	   result = "No action taken yet status is .. %s" %(status)
	   output = checkload()
	   print output
	elif status in ('FIRE'):
	   result = " FirstAid applying ..%s" %(status)
	   print result
	   killhighloadpid(checkload())

	else:
	   result = status
	return result
	

def main():
  if not os.path.exists(config_dir):
   print "Please run python ffainstall.py"
   #import sys; sys.exit(1)
   sys.exit(1)
  TIME = str(datetime.datetime.now())
  #START =  "FFA findings at .. " ( datetime.datetime.now())
  START =  "FFA findings at .. " + (TIME) + "\n"
  current =  callload1()
  fstn =  fnormal()
  fsth =  highload()
  fstm =  maxload()
  status =  ("Currently:  %2.2f , the normal : %2.2f , the high : %2.2f , the max : %2.2f"  % (current, fstn, fsth, fstm))
  #print status
  STATUS = action(compare(current, fstn, fsth, fstm)) + "\n"

  os.chdir(config_dir)
  logs = open(Log_file, "a")
  logs.write (START)
  logs.write (STATUS)
  logs.close()
if __name__ == '__main__':
  main()
