import os, platform, time, sys
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
 
print('\033[1;91m[◽\033[1;91m] \033[1;92mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
ranaxd = platform.architecture()[0]
if ranaxd == '64bit':
 print('\033[1;91m[◽\033[1;91m] \033[1;92mYour Device is 64bit')
 import MOHAMED
elif ranaxd == '32bit':
 print('\033[1;91m[◽\033[1;91m] \033[1;92mYour Devive is 32bit')
 print('\033[1;91m[◽\033[1;91m] \033[1;92THIS TOOL IS 64 bit')
 
