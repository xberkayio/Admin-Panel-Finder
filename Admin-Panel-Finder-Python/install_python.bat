@echo off
echo Welcome to the Python installer!

set "pythonInstallerLink=https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe"
set "pythonInstallerFileName=python-3.11.7-amd64.exe"

set "downloadPath=%CD%"

echo Downloading Python...
curl -o "%downloadPath%\%pythonInstallerFileName%" "%pythonInstallerLink%"

echo Installing Python...
start /wait "" "%downloadPath%\%pythonInstallerFileName%" /quiet InstallAllUsers=1 PrependPath=1

echo Python has been installed. Have a great day!
pause
