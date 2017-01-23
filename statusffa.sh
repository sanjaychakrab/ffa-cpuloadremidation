#!/bin/bash
# please read README.cpuloadremidation
if [ -z $(ps -ef |grep startffa.sh |grep -v grep |awk '{print $2}') ]
 then
  echo 'FFA is not running.'
else 
 echo -e "\033[31mFFA\e[0m enable"
 ps -ef |grep startffa.sh |grep -v grep |awk '{print " running and daemon pid# " $2}'
fi
