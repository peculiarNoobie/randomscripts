import os
from subprocess import call
import time
import webbrowser
from dotenv import load_dotenv

load_dotenv()
chrome_path= os.getenv('chromeS')
chrome= os.getenv('chrome_path')
#SERBESA

def mainScreen():
    os.system('cls')
    os.system('type importantFiles\homeTitle.txt')
    print("\n\n")
    print("Opening SOC related websites...")
    time.sleep(2)
    open()
    print("\n\n\tThank you for using PHsoc script.\n\tB Y E !")
    time.sleep(5)
   
    
def open():
	
    #links of necessary for SOC monitoring
	email_soc = 'https://outlook.office.com/mail/security-operations-center@globalsign.com/'
	soc_tix = 'https://intranet.internal.globalsign.com/jira/issues/?filter=21087'
	soc_dashboard = 'https://intranet.internal.globalsign.com/jira/secure/Dashboard.jspa?selectPageId=14301'
	spreadsheet_block = 'https://globalsign-my.sharepoint.com/:x:/p/ruben_annemans/ERicBaCm2K9PjcrjhO5W3RoBGHHvIydRi8FQwm6U_GXVxQ?e=KHzoYL&ovuser=8fff67c1-8281-4635-b62f-93106cb7a9a8%2Cjoshua.garcia%40globalsign.com&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzAxMDEwMDkxMyIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D'
	virus_total = 'https://www.virustotal.com/gui/home/upload'
	urlscan = 'https://urlscan.io/result/fc4f174a-7e50-496d-9dc0-12bf07cdd413/'
	soc_process = 'https://intranet.internal.globalsign.com/confluence/display/PA/SOC+Processes'
	#chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
	
    #starting Chrome browser
	os.startfile(chrome, "open")

    #opening the links in the open browser
	webbrowser.get(chrome_path).open(email_soc)
	webbrowser.get(chrome_path).open(soc_process)
	webbrowser.get(chrome_path).open(urlscan)
	webbrowser.get(chrome_path).open(virus_total)
	webbrowser.get(chrome_path).open(spreadsheet_block)
	webbrowser.get(chrome_path).open(soc_dashboard)
	webbrowser.get(chrome_path).open(soc_tix)
	
if __name__ == '__main__':
	mainScreen()