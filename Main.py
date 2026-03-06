import time
import re
import pygetwindow as gw
from pypresence import Presence
import psutil
import sys
import os

if os.name == "nt":
    resolve_path = "C:\\ProgramData\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules"
elif os.name == "posix":
    resolve_path = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules"

sys.path.append(resolve_path)

import DaVinciResolveScript as dvr #DVR scripting API 


clientid = ""  #replace this with your Discord Application Client ID 

rpc = Presence(clientid)
rpc.connect()

start_time = int(time.time())

rlv = dvr.scriptapp("Resolve")
if rlv is None:
    print("Couldnt connect to DaVinci Resolve")
    exit()

prcjmanager = rlv.GetProjectManager() #project manager

def davincirunning():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] and any(name in proc.info['name'].lower()for name in ['resolve', 'davinci', 'bmdbridge']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def projectname():#this will get the current project name, if there is no project open it will return "Unknown Project"
    try:
        prcj = prcjmanager.GetCurrentProject()
        return prcj.GetName() if prcj else "Unknown Project"
    except:
        return "Unknown Project"

def prduct(): #this will get the product name, such as DaVinci Resolve Studio or DaVinci Resolve
    try:
        return rlv.GetProductName()
    except:
        return "Unknown Product Name"

def version():
    try: 
        return rlv.GetVersionString()
    except:
        return "Unknown Version"
    
def currentpage():
    try: 
        return rlv.GetCurrentPage()
    except:
        return "Unknown Page"

def rpc():
    projectname = projectname()
    productname = prduct()
    version = version()
    page = currentpage()
    
    rpc.update(
        state=f"Editing: {projectname}",
        details=f"{productname} {version}",
        start=start_time,
        large_image="main2",
        large_text=f"Current Page: {page}",
    )


def main():
    print("Discord RPC loaded")
    while True:
        if not davincirunning():
            print("DaVinci Resolve closed. Exiting...")
            break

        if not rpc():
            time.sleep(2)
            if not davincirunning():
                print("DaVinci Resolve connection lost. Exiting...")
                break

        time.sleep(1)

    try: 
        rpc.close()
    except:
        pass
        
if __name__ == "__main__":
    main()