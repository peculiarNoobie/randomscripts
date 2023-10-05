import pygetwindow as gw
import win32gui
import pyautogui as ag
import time

# Find a specific window by its title
def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    return title

window = gw.getWindowsWithTitle('PH SOC Josh dashboard (TEST) - GMO GlobalSign JIRA - Google Chrome')[0]
mema = gw.getWindowsWithTitle(get_active_window_title())[0]
phinf = gw.getWindowsWithTitle('PH Infra Monitoring Overview - Dashboards - Grafana - Google Chrome')[0]
zabbix = gw.getWindowsWithTitle('ZABBIX-PROD: Dashboard - Google Chrome')[0]
atlasovr = gw.getWindowsWithTitle('Atlas Overview - Grafana - Google Chrome')[0]
zabbixph = gw.getWindowsWithTitle('Zabbix PH - Grafana - Google Chrome')[0]
dssops = gw.getWindowsWithTitle('DSS Operations - Grafana - Google Chrome')[0]
sk = gw.getWindowsWithTitle('Swiss Knife | Initial')[0]

# Get window properties
# print("Window Title:", window.title)
# print("Window Size:", window.size)
# print("Window Location:", window.left, window.top)

time.sleep(5)
# Move the window to a new location (x, y coordinates)
###
window.moveTo(1914, -408) # 1PHSOC DASHBOARD size (bit large on top)
window.resizeTo(1933, 322) 
# 2Website that I just want or any windows that I use for myself (partnered in large on top dashboard)
# window.moveTo(1908, -188) # 2Website that I want partner with FIT
###

#swiss knife 
sk.moveTo(1464, 395)
sk.resizeTo(343, 195)

# Resize the window (width, height)
mema.moveTo(1908, -94)
mema.resizeTo(1939, 893)
###
# window.resizeTo(1933, 226) #PH Dashboard fit
# window.resizeTo(1939, 987) # partnered website I want


######

#atlasoverview
atlasovr.moveTo(637, 545)
atlasovr.resizeTo(695, 545)
#zabixph
zabbixph.moveTo(1317, 545)
zabbixph.resizeTo(610, 575)
#dssOps
dssops.moveTo(-7, 545)
dssops.resizeTo(660, 545)
#zabix
zabbix.moveTo(1317, 30)
zabbix.resizeTo(610, 605)
#phINFRAmon
phinf.moveTo(-7, 30)
phinf.resizeTo(1339, 605)

######


# Maximize the wi1914ndow
# window.maximize()

# Minimize the window
# window.minimize()

# Restore the window (if it was minimized or maximized)
# window.restore()

# Close the window
# window.close()

# Activate a window
# gw.getWindowsWithTitle('Another Window Title')[0].activate()

# Take a screenshot of the window
# screenshot = ag.screenshot(region=(window.left, window.top, window.width, window.height))
# screenshot.save('window_screenshot.png')

# List all open windows
windows = gw.getAllTitles()
print("Open Windows:", windows)