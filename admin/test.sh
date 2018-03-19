#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
export HANLP_STATIC_ROOT=$baseDir/../data
export HANLP_JAR_PATH=$baseDir/../data/hanlp-portable-1.6.0.jar

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
python tests/test_hanlp.py
