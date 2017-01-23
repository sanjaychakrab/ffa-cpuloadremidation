#!/usr/bin/python -tt
# please read README.cpuloadremidation
import sys,os,shutil

config_dir = "/var/tmp/ffa/config"
config_file = "ffa_conf"
try:
 if os.path.exists(config_dir):
  #os.removedirs(config_dir)
  shutil.rmtree(config_dir)
  print "FFA setup removed."
 else:
  print "no FFA setup found."
except: 
 print "Something wrong VALUEERROR"
