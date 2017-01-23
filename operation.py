#!/usr/bin/python -tt
# please read README.cpuloadremidation

'''

    #Time started:\t\t", proginfo[4]
    #for i in proginfo: print i
'''
#import commands, os, string, path
#import commands, os, string, random, psutil
import commands, os, string, random, signal

# operation kill the pid

def killhighloadpid(pid):

    try:
    	print 'Killing this pid ', pid
    	os.kill(int(pid), signal.SIGTERM)
    
    except:
    	return "There was a problem with operation ."
    return " %s(pidvalue) Termeintaed"

# operation 

# operation
