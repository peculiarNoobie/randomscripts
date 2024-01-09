#!/usr/bin/env python3
import pygetwindow as gw
import pyautogui

class WindowInfo:
    """This class is just a container and formats the scraped data."""
    
    def __init__(self, title, left, top, width, height):
        """Container of instance variables to be use to format"""
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height
    
    def __str__(self):
        """Returns Window Info output format that has been scraped from Scraper when the class is called to print\nThis also make the format in readable form."""
        return f"Title: {self.title}\nLeft: {self.left}\nTop: {self.top}\nWidth: {self.width}\nHeight: {self.height}\n"

class Scraper: 
    """This class Scraper() is use to scrape all the windows that are not minimized."""
    
    def __init__(self):
        """Scrape window information\n\tThis class scrape information, then use the class WindowInfo for formating it into strings (__str__) then store it in self.windows instance of Scrape class.\nself.windows stores "formated" instances (ex. title, left, etc.) of the class WindowInfo in the list. This means each window's information is stored here with each specific informations.\nBlocklist are lists of windows that are not necessary to be use in the program."""
        self.windows = []

        #Feel Free to put the programs here in blocklist that you don't need to scrape. [ex. default programs work in background that still detected by pygetwindow module]
        blocklist = ['Cortana', 'Microsoft Text Input Application', 'Settings', 'Program Manager'] 

        all_titles = gw.getAllTitles() 
        for window_title in all_titles:
            window = gw.getWindowsWithTitle(window_title)[0] #This line is used to detect if minimized or not. This is called to determine the place of window in pc memory of the window title.
            if window_title == '' or window_title in blocklist or window.isMinimized:
                pass  
            else:
                self.windows.append(WindowInfo(window.title, window.left, window.top, window.width, window.height))

    def get_window_info(self, title): 
        """**For Debugging Purposes Only** However it can also be use as a tool if needed to be use in determining a specific title query used only for debugging."""
        for window_info in self.windows:
            if window_info.title == title:
                return window_info

class Save:
    """This Class saves the scraped data\n\t(mainly self.windows instance of Scrape Class)The saved file is stored in a file called window. It can be seen in the same folder of this program or on the folder where this program run.\nYou could also change the file name just make sure to change to read file in the class Main."""
    def __init__(self):
        """Creates an instance from Scraping tool and also call the save method"""
        self.scrapeInfo = Scraper()
        self.savetooltxt()
    
    def savetooltxt(self):
        """Saves the tools in a file called setup"""
        with open("window.txt", "w") as file:
            for windowInfo in self.scrapeInfo.windows:
                file.write(str(windowInfo).replace("\n", "\t") + "\n")

class Main: 
    """This class is the main program.\n\tThe use of this class is to create a dictionary type of the scraped data for other programs to use.\nProgrammer thinks that this may organize things more than a lists or in human readable form where the class WindowInfo creates it in string.\n\tParts:\n\tPrimary key: Window Titles\n\tValues: Left, Top, Width, Height values\n\t        (its a nested dictionary) Keys are the category of its value."""
    dict = {}

    def __init__(self): #instantiate the main and important program to run.
        """This just simply instantiate the program."""
        self.scrapeInfo_file = self.readinfo()


    def readinfo(self):
        """This reads the file and fill up the dictionary with keys and values."""
        """***Note that the first window in the dictionary is the active widow which the user last clicked before the program run.***"""
        with open("window.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                information = {}
                part = line.split("\t")
                infor = []
                for info in part:
                    if info == '\n':
                        pass
                    else:    
                        infor.append(info.split(": ")[1])
                information["Left"] = infor[1]
                information["Top"] = infor[2]
                information["Width"] = infor[3]
                information["Height"] = infor[4]
                Main.dict[infor[0]] = information
            #window_info.append(WindowInfo(info[0], info[1], info[2], info[3]))
    
    def __str__(self):
        """Returns the dictionary with keys and values that may be used in later programs as a module or classes"""
        return str(Main.dict) 



# Example usage
if __name__ == "__main__":
    window_manager = Scraper()

    for window_info in window_manager.windows:
        print(window_info)
    
    print("\n\n")
    
    Save()
    another_instance = Main()
    print(another_instance)
