#!/usr/bin/python3.4 -tt
# please read README.cpuloadremidation
import os
import subprocess 
import shlex
def callload1():
     
	try:
         f = open( "/proc/loadavg" )
         contents = f.read().split()
         #contents = f.read().split(" ")
         #print(contents)
         #x, y = contents
         #print(x)
         #print(y)

         f.close()
        except:
         return "Cannot open uptime file: /proc/uptime"

     	firstsec =  float(contents[0])
     	#secondvalue = float(contents[1])
     #aprint "First value :"
     #print(total_seconds)
	return firstsec	
