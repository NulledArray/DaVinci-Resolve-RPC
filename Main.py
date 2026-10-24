#!/usr/bin/python3

import time
import re
# import pygetwindow as gw #X11 Only. Wayland Fix is WIP.
from pypresence import Presence
import psutil
import sys
import os

if os.name == "nt":

    resolve_path = "C:\\ProgramData\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules"

elif sys.platform == "darwin":

    resolve_path = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules"

elif sys.platform.startswith("linux"):

    resolve_path = "/opt/resolve/Developer/Scripting/Modules"

sys.path.append(resolve_path)

import DaVinciResolveScript as dvr  # DVR scripting API

clientid = ""  # replace this with your Discord Application Client ID

rpc = Presence(clientid)
rpc.connect()

start_time = int(time.time())

rlv = dvr.scriptapp("Resolve")
if rlv is None:
    print("Couldnt connect to DaVinci Resolve")
    exit()

prcjmanager = rlv.GetProjectManager()  # project manager


def davincirunning():
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            name = proc.info['name'] or ''
            exe = proc.info['exe'] or ''
            cmdline = proc.info['cmdline'] or []

            # Check the process name
            if name.lower() == 'resolve':
                return True

            # Check the executable filename
            if exe and os.path.basename(exe).lower() == 'resolve':
                return True

            # Check the executable used to launch the process
            if cmdline and os.path.basename(cmdline[0]).lower() == 'resolve':
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False


def projectname():  # this will get the current project name, if there is no project open it will return "Unknown Project"
    try:
        prcj = prcjmanager.GetCurrentProject()
        return prcj.GetName() if prcj else "Unknown Project"
    except:
        return "Unknown Project"


def prduct():  # this will get the product name, such as DaVinci Resolve Studio or DaVinci Resolve
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


def update_presence():
    try:
        rlv.GetVersionString()  # raises/returns None if Resolve is gone
    except Exception:
        return False
    current_project_name = projectname()
    productname = prduct()
    version_str = version()
    page = currentpage()

    rpc.update(
        state=f"Editing: {current_project_name}",
        details=f"{productname} {version_str}",
        start=start_time,
        large_image="main2",
        large_text=f"Current Page: {page}",
    )
    return True


def main():
    print("Discord RPC loaded")

    try:
        while True:

            if not davincirunning():
                print("DaVinci Resolve closed. Exiting...")
                break

            if not update_presence():
                print("Lost connection to DaVinci Resolve. Exiting...")
                break

            time.sleep(1)

    except KeyboardInterrupt:
        print("RPC stopped by user.")

    finally:
        print("Cleaning up Discord RPC...")

        try:
            rpc.clear()
        except Exception:
            pass

        try:
            rpc.close()
        except Exception:
            pass

        print("Discord RPC closed.")


if __name__ == "__main__":
    main()