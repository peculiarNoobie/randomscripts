import pygetwindow as gw
import pyautogui

class WindowInfo:
    def __init__(self, title, left, top, width, height):
        """Container of instance variables to be use to format and arrange the scraped data"""
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height
    
    def __str__(self):
        """Returns Window Info output format that has been scraped from Scraper when the class is called to print"""
        return f"Title: {self.title}\nLeft: {self.left}\nTop: {self.top}\nWidth: {self.width}\nHeight: {self.height}\n"

class Scraper:
    def __init__(self):
        """Scrape window information"""
        self.windows = [] #the main data container of all the windows and its information
        blocklist = ['TEST1.py - Godmode - Visual Studio Code','Cortana', 'Setup', 'Program Manager', 'Microsoft Text Input Application', 'Settings'] #Program that are system generated and cannot be minimized or on the background processes that are default not minimized
        all_titles = gw.getAllTitles() 
        for window_title in all_titles:
            if window_title == '' or window_title in blocklist: 
                pass  
            else:
                window = gw.getWindowsWithTitle(window_title)[0] # only use to detect if minimized or not. This is called to determine the place of window in pc memory of the window title.
                if window.isMinimized:
                    pass  
                else:
                    self.windows.append(WindowInfo(window.title, window.left, window.top, window.width, window.height))

    def get_window_info(self, title): 
        """to be use in determining a specific title query used only for debugging."""
        for window_info in self.windows:
            if window_info.title == title:
                return window_info


# Example usage
if __name__ == "__main__":
    window_manager = Scraper()

    for window_info in window_manager.windows:
        print(window_info)

#    title_to_query = "PH SOC Josh dashboard (TEST) - GMO GlobalSign JIRA - Google Chrome"
#    info = window_manager.get_window_info(title_to_query)
#    if info:
#        print(f"Information for '{title_to_query}':\n{info}")
#    else:
#        print(f"Window with title '{title_to_query}' not found.")