#!/usr/bin/python -tt
# please read README.cpuloadremidation
import re, string, os
## check cores
def total():
 c = 0
 try:
	with open ("/proc/cpuinfo", 'r') as f:
	 for ln in f:
	  if 'processor' in ln:
	   c = c + 1 
	f.close()
 except:
	return " Something wrong in finding in cpuinfo "
 return c
