
import pyautogui as p
import time as t
import keyboard


print("Running the amazing program...")
while True:
    
    if keyboard.is_pressed('`'):
        print("pause")
        t.sleep(60)
    else:
        p.click(2533, 414)
        p.hotkey("f5")
        t.sleep(900)
        p.click(3314, 418)
        t.sleep(900)




    