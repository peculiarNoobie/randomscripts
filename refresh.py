
import pyautogui as p
import time as t
import keyboard


print("Running the amazing program...")
while True:
    
    if keyboard.is_pressed('`'):
        print("pause")
        t.sleep(60)
    else:
        p.click(2839, -271)
        p.hotkey("f5")
        t.sleep(900)




    