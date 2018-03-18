#!/bin/sh

owner=$1
project=$2
user=$3
password=$4

mkdir -p "${project}/diffs"
echo "RequestPullList"
python3 python/RequestPullList.py https://api.github.com $owner $project $user $password
echo "RequestDiffList"
python3 python/RequestDiffList.py $owner $project $user $password
echo "GetDiffs"
python3 python/GetDiffs.py $project $user $password
echo "ExtractChangedSymbols"
python3 python/ExtractChangedSymbols.py $project
