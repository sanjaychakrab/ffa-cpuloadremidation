#!/usr/bin/python -tt
# please read README.cpuloadremidation
import re, string, os
## check cores
def cores():
 try:
	with open ("/proc/cpuinfo", 'r') as f:
	 for ln in f:
	  if 'cpu cores' in ln:
	   cores = ln
	   content = ln.split()
	   Numbercores = (content)[3]
	   break
	f.close()
 except:
	return " Something wrong in finding in cpuinfo "
 return Numbercores
