# DaVinci Resolve Discord RPC

Display your DaVinci Resolve editing activity on Discord with rich presence integration!

## Overview

[Modded by NulledArray]
This is a Modified version of the original DaVinci Resolve Discord RPC project, designed to provide real-time updates of your video editing work on Discord.
The Original Main.py doesn't actually work on Linux, so this version has been modified to fix the issues and provide a 
seamless experience.
Don't forget to update the Client ID in `Main.py` before using autostart functionality.

This version works both in the Linux Terminal and the Python Scripting Engine of DaVinci Resolve.

The Linux Path for the DaVinci Resolve Scripting API is usually now: 
$HOME/.local/share/DaVinciResolve/Fusion/Scripts/Utility

Place both files into that Folder, then run Davinci Resolve, Next click on "Workspace" and then "Scripts" and then 
"Main".

The DiscordRPC will also now Flush and clear the status when you close DaVinci Resolve, so you don't have to worry about it being stuck in your Discord status.

---

Don't forget to add these lines to your .bashrc or .profile
# DaVinci Resolve Python Scripting API
export RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting"
export RESOLVE_SCRIPT_LIB="/opt/resolve/libs/Fusion/fusionscript.so"
export PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"

---

This project enables Discord Rich Presence (RPC) integration with DaVinci Resolve, allowing you to showcase your video editing work as your Discord status. It uses the DaVinci Resolve Python scripting API to fetch project information and displays it on your Discord profile in real-time.

## Features

- Display current DaVinci Resolve project name on Discord
- Show product information (DaVinci Resolve vs Studio)
- Real-time status updates
- Cross-platform support (Windows, macOS, Linux)
- Seamless Discord integration

## Requirements

- **Python 3.6+** (64-bit)
- **DaVinci Resolve** (with scripting support enabled)
- **Discord** (running and signed in)
- **Python Packages:**
  - `pypresence` - Discord RPC client
  - `pygetwindow` - Window management
  - `psutil` - Process monitoring

## Installation

### 1. Install Dependencies

```bash
pip install pygetwindow pypresence psutil
```

### 2. Set up DaVinci Resolve Scripting

DaVinci Resolve scripting requires the proper environment setup:

**Windows:**
```
RESOLVE_SCRIPT_API=%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting
PYTHONPATH=%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules\
```

**macOS:**
```
RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
```

**Linux:**
```
RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting"
PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
```

### 3. Create a Discord Application

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Copy your **Client ID**
4. In the sidebar, go to "Rich Presence" → "Art Assets"
5. Add images if desired
6. Keep the Developer Portal open for later

## Configuration

### Update Client ID (Required Before Autostart)

Open `Main.py` and replace the empty `clientid` variable with your Discord Application Client ID:

```python
clientid = "YOUR_CLIENT_ID_HERE"  # Replace with your Discord Application Client ID
```

**Important:** If you plan to use autostart, update the Client ID in `Main.py` before copying the files to the DaVinci Resolve scripts directory.

## Usage

### Option 1: Autostart with DaVinci Resolve (Recommended)

For the script to automatically launch when DaVinci Resolve starts, place the files in DaVinci Resolve's scripts directory:

**Windows:**
```
Copy Main.py and RPC.scriptlib to:
C:\Users\<YourUsername>\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Utility\
```

**macOS:**
```
Copy Main.py and RPC.scriptlib to:
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility/
```

**Linux:**
```
Copy Main.py and RPC.scriptlib to:
~/.Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility/
```

Once placed, the script will:
1. Automatically launch when you open DaVinci Resolve
2. Connect to the DaVinci Resolve instance
3. Authenticate with Discord
4. Display your editing activity on your Discord profile
5. Continuously update your status as you work

### Option 2: Manual Execution

Alternatively, run the script manually from the command line:

```bash
python Main.py
```

### Stopping the Script

Press `Ctrl+C` in the terminal to stop the RPC connection (when running manually).

## How It Works

1. **DaVinci Resolve Connection:** Uses the official DaVinci Resolve Python scripting API to access project information
2. **Process Monitoring:** Checks if DaVinci Resolve is running using process monitoring
3. **Discord RPC:** Sends updates to Discord using the PyPresence library
4. **Real-time Updates:** Continuously fetches and pushes status information

## Project Structure

- `Main.py` - Main application script
- `RPC.scriptlib` - Supporting library files
- `API Documention.txt` - DaVinci Resolve API documentation reference

## Troubleshooting

### "Couldn't connect to DaVinci Resolve"
- Ensure DaVinci Resolve is running
- Check that scripting is enabled in Resolve preferences
- Verify Python path environment variables are set correctly

### Discord Status Not Showing
- Confirm you're signed into Discord
- Check that the Client ID is correct in `Main.py`
- Verify the Discord application has Rich Presence enabled
- Restart Discord and the Python script

### Module Not Found Errors
- Reinstall dependencies: `pip install --upgrade pygetwindow pypresence psutil`
- Ensure PYTHONPATH includes the DaVinci Resolve modules

## Supported Platforms

- ✅ Windows
- ✅ macOS
- ✅ Linux

## Requirements & Notes

- DaVinci Resolve must be running while the script executes
- An active Discord connection is required
- The script requires sufficient permissions to access DaVinci Resolve API
- For autostart functionality, ensure all Python dependencies are installed before placing files in the DaVinci Resolve scripts directory
- The Discord app must be running on your system for RPC to work
- See `API Documention.txt` for more information about the DaVinci Resolve scripting API