import pyautogui as p
import time as t
from win10toast import ToastNotifier

def toast(message):
	toaster = ToastNotifier()
	toaster.show_toast(message)

def job():
    # call(['python', 'testgql.py'])
    toast("YOU HAVE 15 seconds to check each picture")
    
p.click(650,21)
p.hotkey("f5")
t.sleep(5)
p.click(button='right', x=532, y=307)
p.click(592,326)
t.sleep(5)
p.hotkey("ctrl", "tab")
p.hotkey("ctrl", "tab")
t.sleep(5)
p.click(598,241)
t.sleep(3)
job()
t.sleep(15)
p.hotkey("esc")
t.sleep(3)
p.scroll(100)
t.sleep(4)
p.hotkey("a")
t.sleep(5)
p.write("sheryl")
t.sleep(5)
p.hotkey("enter")
t.sleep(5)
p.click(984,612)
t.sleep(5)
p.write('Hi Mam Sheryl Patalen,\nIt is a false positive. The difference between the lighting in the room was the main issue that the cctv detected.\nRequesting for your review\n\nThank you!\nRegards,')
t.sleep(5)
p.hotkey("alt", "s")
t.sleep(5)
p.hotkey("ctrl", "w")
