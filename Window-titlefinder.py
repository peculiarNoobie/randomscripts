import win32gui
import time
                                                        

# Function to get the active window's title
def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    return title

print("click the window you want to determine")
time.sleep(8)

# Get the title of the active window
active_window_title = get_active_window_title()

# Print the title
print("Active Window Title:", active_window_title)
time.sleep(7)