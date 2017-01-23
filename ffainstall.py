#!/usr/bin/python -tt
# please read README.cpuloadremidation
#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys,os,shutil
###
#local modules
#from cpusiblings import siblings
from cpucores import cores
from cputotal import total
###
config_dir = "/var/tmp/ffa/config"
config_file = "ffa_conf"

__version__ = "1.01"
__author__ = "Sanjay Chakraborty <sanjaycphilly@gmail.com>"
# sre exception
#error = sre_compile.error
####
if os.geteuid() != 0:
 print " You need to be super user."
 exit(0)
######
STARTFFA = "#!/bin/bash" +'\n' + "while true; do `/usr/bin/which python` ffa.py;  sleep 10;  done &" + '\n'


def createffasetupdirectory():
 try:
  if not os.path.exists(config_dir):
   os.makedirs(config_dir)
   print "ffa directory created"
  else:
   print "ffa setup file found."

 except:
  print "Usinng old ffa drectory"
#################

##main 
def main():
# config_dir = "/var/tmp/ffa/config"
# config_file = "ffa_conf"
 HEADING1 = "FFA configuration setting goes here. NO MODIFICATION BY HAND"
 MR1 = 'cpuload remidation'
##cpu core
 
 cups = int(total())
 acrs = int(cores())
 totcc = cups * acrs
 hi = int((totcc * .5) + totcc)
 mx  = int(totcc * 2)
 cns = ("Number of CPU =  %d" % (cups))
 crs = ("Number of cores =  %d" % (acrs))
 load = ("Normal CPU load can be = {} " . format (totcc))
 high = ("High CPU load   = {} ". format (hi))
 max = ("Max threashold CPU load = {} " . format (mx))

 createffasetupdirectory()
 os.chdir(config_dir)
 config = open(config_file, "w")
 config.write (HEADING1)
 config.write ('\n')
 config.write (MR1)
 config.write ('\n')
 config.write (cns)
 config.write ('\n')
 config.write (crs)
 config.write ('\n')
 config.write (load)
 config.write ('\n')
 config.write (high)
 config.write ('\n')
 config.write (max)
 config.write ('\n')
 
 config.close()
	#stat.S_IROTH


if __name__ == '__main__':
 main()
