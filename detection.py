#!/usr/bin/python -tt
# please read README.cpuloadremidation

'''
	dectection checks the issue and return the finding
'''
import commands, os, string, random, signal

# detect high load
value =''
def checkload():

	try:
    		#perform a ps command and assign results to a list
    		output = commands.getoutput("ps aux | sort -nrk 3,3 | head -n 1")
    		proginfo = string.split(output)
    		#print  'This is the process', proinfo
    		#print  'This is the process'
    		OWNER = proginfo[0]
    		CPU_in_percent = proginfo[2]
		#print CPU_in_percent
    		psvalue = proginfo[1]
    		value = '{}'.format (psvalue)
    		pstatus = value.strip()
    		pid = int(pstatus)
    		#print 'pid number', pid
		print 'Process status file creating in /var/tmp/', pid
    		wpids = open ("/var/tmp/" + str(pid) ,'w')
    		rpids = open ("/proc/" + str(pid) + "/status", 'r')
    		for line in rpids: wpids.write ("%s" %line) 
    		wpids.close()
    		rpids.close()
		value = pid
	except:
        	print "Not able to detect high load process."
	#return str(pid)
	print 'from detection pid #..', value
	return value

#print checkload()
#checkload()

# detect 

# detect
