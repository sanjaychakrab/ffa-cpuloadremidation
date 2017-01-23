#!/usr/sbin/python -tt
# please read README.cpuloadremidation
import string,os
def fnormal():
 try:
	with open ("/var/tmp/ffa/config/ffa_conf", 'r') as file:
	 for ln in file:
	  if 'Normal' in ln:
	   returnthisvalue = ln
	   ncpu= ln.split("=")[1]
	   Nload = float(ncpu)
	   break
	file.close()
        return Nload

 except:
	return "No FFA setup configured."

################
def highload():
 try:   
        with open ("/var/tmp/ffa/config/ffa_conf", 'r') as file:
         for ln in file:
          if 'High' in ln:
           returnthisvalue = ln
           h= ln.split("=")[1]
           Highload = float(h)
           break
        file.close()
        return Highload

 except:
        return "No FFA setup configured for High load."

#############
def maxload():
 try:   
        with open ("/var/tmp/ffa/config/ffa_conf", 'r') as file:
         for ln in file:
          if 'Max' in ln:
           returnthisvalue = ln
           m= ln.split("=")[1]
           maxload = float(m)
           break
        file.close()
        return maxload

 except:
        return "No FFA setup configured for Max load. ."


	   
	   
