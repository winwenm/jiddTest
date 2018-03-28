#!/bin/bash
#git pull
python -m coverage run allTest.py
python -m coverage xml -o coverage.xml
cp -r ./coverage.xml /Users/WinWen/.jenkins/workspace/testReport/coverage.xml
cp -r ./xmlReports /Users/WinWen/.jenkins/workspace/testReport/xmlReports