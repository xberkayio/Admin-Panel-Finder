@echo off
echo Installing required Python libraries...

python.exe -m pip install --upgrade pip
pip install urllib3 httpx requests

echo Libraries installed successfully.
pause
