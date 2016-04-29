#!/usr/bin/env python

import subprocess
import time
import sys

desktopfile = sys.argv[-1]

def read_currentlauncher():
    # reads the current launcher contents
    get_launcheritems = subprocess.Popen([
        "gsettings", "get", "com.canonical.Unity.Launcher", "favorites"
        ], stdout=subprocess.PIPE)
    return get_launcheritems.communicate()[0].decode("utf-8")

def set_launcher(llist):
    # sets a defined unity launcher list
    current_launcher = str(llist).replace(", ", ",")
    subprocess.Popen([
        "gsettings", "set", "com.canonical.Unity.Launcher", "favorites",
        current_launcher,
        ])

def refresh_icon(desktopfile):
    current_launcher = read_currentlauncher()
    current_launcher_temp = eval(current_launcher)
    item = [item for item in current_launcher_temp if desktopfile in item][0]
    index = current_launcher_temp.index(item)
    current_launcher_temp.pop(index)
    set_launcher(current_launcher_temp)
    time.sleep(2)
    set_launcher(current_launcher)

refresh_icon(desktopfile)
