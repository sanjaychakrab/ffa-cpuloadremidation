#!/bin/bash
# please read README.cpuloadremidation
if [ -z $(ps -ef |grep startffa.sh |grep -v grep |awk '{print $2}') ]
 then
  echo 'FFA is not running.'
else 
 ps -ef |grep startffa.sh |grep -v grep |awk '{print " killing pid# " $2}'
 ps -ef |grep startffa.sh |grep -v grep |awk '{print  $2}' |xargs kill -9
fi
