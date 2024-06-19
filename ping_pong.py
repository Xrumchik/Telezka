import os
import subprocess
from time import *
failed_count=0

def ping_host(host):
    global failed_count
    response = os.system("ping -c 1 " + host)
    if response == 0:
        print(f"Connection to {host} is OK!")
        failed_count=0
    else:
        print(f"Connection to {host} failed!")
        failed_count+=1



def set_wifi(state):
    if state.lower() == "on":
        subprocess.call(["sudo", "ifconfig", "wlan0", "up"])
    elif state.lower() == "off":
        subprocess.call(["sudo", "ifconfig", "wlan0", "down"])
    else:
        raise ValueError("Invalid state. Use 'on' or 'off'.")




while True:
    host = "google.com"  
    ping_host(host)
    sleep(1) #мб надо убрать, а мб нет
    if failed_count>5:
        set_wifi("off")
        sleep(10)
        set_wifi("on")
        sleep(15)
        failed_count=0
