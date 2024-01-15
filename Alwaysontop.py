import pygetwindow as gw
import pyautogui as ag
import win32gui
import win32con
import time 

def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    return title

print("select your window")
time.sleep(5)

# Define the title of the application you want to manipulate
app_title = get_active_window_title()

# Find the window by its title
hwnd = win32gui.FindWindow(None, app_title)

if hwnd:
    # Check if the window is currently set to be always on top
    is_always_on_top = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOPMOST

    # Set transparency (0 = fully transparent, 255 = opaque)
    transparency = 255  # Adjust the value as needed (0-255) 
    #Recommended
    # MS Teams = 240
    # Youtube (Picture-in-Picture) = 100

    # Toggle the "Always on Top" setting
    if is_always_on_top:
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & ~win32con.WS_EX_LAYERED)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"Removed 'Always on Top' setting for '{app_title}'.")
    else:
        print(f"Set '{app_title}' to 'Always on Top'.")
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, transparency, win32con.LWA_ALPHA)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"Set transparency for '{app_title}' to {transparency}.")

    # Set the window's transparency

else:
    print(f"Window with title '{app_title}' not found.")
