import pytz
import winsound
import schedule
import pyperclip
import webbrowser
import os
import signal
import time
import sys	
from subprocess import call
from win10toast import ToastNotifier
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
chrome_path= os.getenv('chromeS')
chrome= os.getenv('chrome_path')
def clear():
    os.system('cls')

def toast(message):
	toaster = ToastNotifier()
	toaster.show_toast(message)

def main_screen(shift_selected):
	clear()
	print(f"Globalsign Infrastructure Philippines\n")
	# print(f"Please wait for the beep sound for the next CF reporting.\n")
	print("Global Date and Time\n")
	print(shift_selected, "Shift")
	UTC = pytz.timezone('Etc/UTC')
	UTC_time = datetime.now(UTC)
	uk = pytz.timezone('Europe/London')
	uk_time = datetime.now(uk)
	sg = pytz.timezone('Singapore')
	sg_time = datetime.now(sg)
	tky = pytz.timezone('Asia/Tokyo')
	tky_time = datetime.now(tky)
	usa = pytz.timezone('America/New_York')
	usa_time = datetime.now(usa)
	print("-----------------------------------------------------")
	print(UTC_time.strftime("GMT/UTC:        %b-%d-%Y %I:%M %p\n"))
	print(sg_time.strftime("Singapore:      %b-%d-%Y %I:%M %p\n"))
	print(tky_time.strftime("Tokyo:          %b-%d-%Y %I:%M %p\n"))
	print(uk_time.strftime("UK:             %b-%d-%Y %I:%M %p\n"))
	print(usa_time.strftime("New Hampshire:  %b-%d-%Y %I:%M %p\n"))
	print("-----------------------------------------------------")

def sound():
    frequency = 500  # Set Frequency To 2500 Hertz
    duration = 1200  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def handler(signum, frame):
    print('', signum)

def job():
    # call(['python', 'testgql.py'])
    toast("Weekly GCC Reset")
    os.system('C:/Users/joshua.garcia/AppData/Local/Microsoft/Teams/Update.exe --processStart "Teams.exe"')
    sg = pytz.timezone('Singapore')
    sg_time = datetime.now(sg)
    pyperclip.copy(sg_time.strftime("@JP Infra\nThe weekly restart for GSGAS05/06 and GSAPI10/11/12/13 at %Y/%m/%d is starting. If you encounter any problem for above server, please let us know. Also, it should not generate any alert, but if it does so, please let us know."))
    gcc1 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-gcc-1st-restart/'
    gcc2 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-gcc-2nd-restart/'
    gcc3 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-api-ssl-1st-restart/'
    gcc4 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-api-ssl-2nd-restart/'

    fort_path= 'C:/Program Files/Fortinet/FortiClient/FortiClient.exe'
    os.startfile(fort_path, "open")
    time.sleep(7)
    os.startfile(chrome, "open")
    webbrowser.get(chrome_path).open_new(gcc1)
    webbrowser.get(chrome_path).open_new(gcc2)
    webbrowser.get(chrome_path).open_new(gcc3)
    webbrowser.get(chrome_path).open_new(gcc4)


def apac():
	# job()
	schedule.every().friday.at("08:43").do(job)
	
	while True:
		schedule.run_pending()
		time.sleep(5)
			
def main():
	signal.signal(signal.SIGINT, handler)

	apac()

if __name__ == '__main__':
	main()