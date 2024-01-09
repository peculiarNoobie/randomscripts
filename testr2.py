#!/usr/bin/env python3
from testr import Main
import pygetwindow as gw
import win32gui
import pyautogui as ag
import time
import ast
   

class Choice:
    dicti = Main()
    d = eval(str(dicti))
    print("choose what windows do you want to remove")
    print(d.keys())
    userinput = input("Enter the number of element: (multiple must separated by space) ")
    lis = []
    lis = userinput.split(" ") 
    lis = list(map(int, lis))
    print(lis)
    for x in range(len(lis)):
        print(list(d.keys())[lis[x]])


if __name__ == "__main__":
    Choice()