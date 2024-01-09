import pytz
import winsound
import schedule
import webbrowser
import os
import signal
import time
import sys
import pyperclip
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

def open_csv():
	currentTime = datetime.now()
	pathOut = os.getcwd()
	timeF = currentTime.strftime('%Y.%m.%d_%H%M')
	fileName = str(timeF) + '_output.csv'
	os.system(fileName)

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
	print("TSA Keywords")
	print(f" AATL: aatl-timestamp.globalsign.com/tsa/v4v5effk07zor410rew22z")
	print(f" AATL2: aatl-timestamp.globalsign.com/tsa/aohfewat2389535fnasgnlg5m23")
	print(f" ATLAS: timestamp.atlas.globalsign.com/timestamp")
	print(f" JNJ: timestamp.jnj.com/tsa/aohfewat2389535fnasgnlg5m23")
	print(f" R6: timestamp.globalsign.com/tsa/r6advanced1")
	print(f" RFC: rfc3161timestamp.globalsign.com/advanced")
	print(f" TST: timestamp.globalsign.com/tsa/advanced")
	print("-----------------------------------------------------")

    

def choose_option():
	print("Please select a shift:\n")

def sound():
    frequency = 500  # Set Frequency To 2500 Hertz
    duration = 1200  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def handler(signum, frame):
    print('', signum)

def logout():
	toast("Don't forget to Log Out!")
	sprout = 'https://globalsign.hrhub.ph/Login.aspx'
	webbrowser.open_new_tab(sprout)
	time.sleep(5)
	sys.exit()
	
def monitor():
	
	gs_status = 'https://status.globalsign.com/'
	email_infra = 'https://outlook.office.com/mail/sys_monitor@globalsign.com/'
	grafana_ph = 'https://monitoring.hvca.globalsign.com/d/uMJNcedWz/zabbix-ph?orgId=1&refresh=30s'
	site247 = 'https://www.site24x7.com/app/client#/home/monitors'
	cf = 'https://www.cloudflarestatus.com/'
	issuer = 'https://monitoring.hvca.globalsign.com/d/Yuz5VnZVz/expired-issuer-errors?orgId=1&from=now-9h&to=now'
	sg_zabbix = 'https://sgzabbix.globalsign.com:65443/'
	informatica = 'https://dm-us.informaticacloud.com/identity-service/home'
	kibana = 'https://monitoring.hvca.globalsign.com:4443/app/kibana#/home?_g=()'
	atlas = 'https://monitoring.hvca.globalsign.com/d/zCnJcebGk/atlas-overview?orgId=1&refresh=1m'
	dss = 'https://monitoring.hvca.globalsign.com/d/jPF-t-cMk/dss-operations?orgId=1'
	overview_reporting = 'https://cdn-monitoring-poc.staging.globalsign.com/d/HML6oGNVz/ph-infra-monitoring-overview-report?orgId=1&refresh=1m'
	cf_rep = 'https://cdn-monitoring-poc.staging.globalsign.com/d/nYkfb_IVz/cloudflare-reporting?orgId=1&refresh=1m&from=now-6h&to=now'

	#chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
	os.startfile(chrome, "open")
	webbrowser.get(chrome_path).open(gs_status)
	webbrowser.get(chrome_path).open(email_infra)
	webbrowser.get(chrome_path).open(grafana_ph)
	webbrowser.get(chrome_path).open(issuer)
	webbrowser.get(chrome_path).open(site247)
	webbrowser.get(chrome_path).open(cf)
	webbrowser.get(chrome_path).open(sg_zabbix)
	webbrowser.get(chrome_path).open(kibana)
	webbrowser.get(chrome_path).open(informatica)
	webbrowser.get(chrome_path).open(atlas)
	webbrowser.get(chrome_path).open(dss)
	webbrowser.get(chrome_path).open(overview_reporting)
	webbrowser.get(chrome_path).open(cf_rep)

def cf_reporting():
	toast("Please send MSOCSP to Global Infra!")
	cf = 'https://cdn-monitoring-poc.staging.globalsign.com/d/nYkfb_IVz/cloudflare-reporting?orgId=1&refresh=1m&from=now-6h&to=now'

	#chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
	os.startfile(chrome, "open")

	webbrowser.get(chrome_path).open(cf)

def job():
    # call(['python', 'testgql.py'])
    toast("Monitoring Overview Report!")
    overview_reporting = 'https://cdn-monitoring-poc.staging.globalsign.com/d/HML6oGNVz/ph-infra-monitoring-overview-report?orgId=1&refresh=1m'
    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    os.startfile(chrome, "open")
    webbrowser.get(chrome_path).open_new(overview_reporting)

def wR():
	
	toast("Weekly GCC Reset")
	os.system('C:/Users/joshua.garcia/AppData/Local/Microsoft/Teams/Update.exe --processStart "Teams.exe"')
	sg = pytz.timezone('Singapore')
	sg_time = datetime.now(sg)
	pyperclip.copy(sg_time.strftime("@JP Infra\nThe weekly restart for GSGAS05/06 and GSAPI10/11/12/13 at %Y/%m/%d is starting. If you encounter any problem for above server, please let us know. Also, it should not generate any alert, but if it does so, please let us know."))
	toast("You have 8 seconds to send to Notify JP Infra in General(Infra) Teams")

	time.sleep(8)
	gcc1 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-gcc-1st-restart/'
	gcc2 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-gcc-2nd-restart/'
	gcc3 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-api-ssl-1st-restart/'
	gcc4 = 'https://172.21.210.244/job/PROD/job/restart-services/job/prod-api-ssl-2nd-restart/'
	newrel = 'https://one.newrelic.com/'
	infratix = 'https://intranet.internal.globalsign.com/jira/browse/INFRA-5869'
	passmanager = 'https://password.internal.globalsign.com/manager/app/#/secrets/27316/general'

	
	fort_path= 'C:/Program Files/Fortinet/FortiClient/FortiClient.exe'
	os.startfile(fort_path, "open")
	time.sleep(10)
	toast("You have 8 seconds to send to Connect to forticlient")
	os.startfile(chrome, "open")
	webbrowser.get(chrome_path).open_new(gcc1)
	webbrowser.get(chrome_path).open_new(gcc2)
	webbrowser.get(chrome_path).open_new(gcc3)
	webbrowser.get(chrome_path).open_new(gcc4)
	webbrowser.get(chrome_path).open_new(newrel)
	webbrowser.get(chrome_path).open_new(infratix)
	webbrowser.get(chrome_path).open_new(passmanager)
	pyperclip.copy(sg_time.strftime("@JP Infra\nThe weekly restart for GSGAS05/06 and GSAPI10/11/12/13 at %Y/%m/%d is done.\nPlease check the following JIRA ticket for the details.\nhttps://intranet.internal.globalsign.com/jira/browse/INFRA-5869"))

def apac():
	monitor()
	main_screen("APAC")
	schedule.every().minute.at(":02").do(main_screen, shift_selected="APAC")
	schedule.every().day.at("06:00").do(cf_reporting)
	schedule.every().day.at("07:00").do(job)
	schedule.every().day.at("09:00").do(job)
	schedule.every().friday.at("10:00").do(wR)
	schedule.every().day.at("11:00").do(job)
	schedule.every().day.at("13:00").do(job)
	schedule.every().day.at("15:01").do(logout)

	while True:
		schedule.run_pending()
		time.sleep(5)

def emea():
	monitor()
	main_screen("EMEA")
	schedule.every().minute.at(":02").do(main_screen, shift_selected="EMEA")
	schedule.every().day.at("14:00").do(cf_reporting)
	schedule.every().day.at("17:00").do(job)
	schedule.every().day.at("15:00").do(job)
	schedule.every().day.at("19:00").do(job)
	schedule.every().day.at("21:00").do(job)
	schedule.every().day.at("23:01").do(logout)

	while True:
		schedule.run_pending()
		time.sleep(5)

def us():
	monitor()
	main_screen("US")
	schedule.every().minute.at(":02").do(main_screen, shift_selected="US")
	schedule.every().day.at("22:00").do(cf_reporting)
	schedule.every().day.at("23:00").do(job)
	schedule.every().day.at("01:00").do(job)
	schedule.every().day.at("03:00").do(job)
	schedule.every().day.at("05:00").do(job)
	schedule.every().day.at("07:01").do(logout)
	

	while True:
		schedule.run_pending()
		time.sleep(5)

def floating():
	monitor()
	main_screen("Floating")
	schedule.every().minute.at(":02").do(main_screen, shift_selected="Floating")
	schedule.every().day.at("11:00").do(job)
	schedule.every().day.at("13:00").do(job)
	schedule.every().day.at("15:00").do(job)
	schedule.every().day.at("17:00").do(job)
	schedule.every().day.at("19:00").do(job)
	schedule.every().day.at("20:01").do(logout)

	while True:
		schedule.run_pending()
		time.sleep(5)

	
def main():
	choose_option()
	signal.signal(signal.SIGINT, handler)
	print("APAC is 1")
	print("EMEA is 2")
	print("US is 3")
	print("Floating(11am-8pm) is 4\n")

	shift = int(input("Please enter your shift: "))
	if shift == 1:
		apac()

	elif shift == 2:
		emea()

	elif shift == 3:
		us()

	elif shift == 4:
		floating()
	else:
		print("Please choose a valid shift!")
		time.sleep(2)
		main()

if __name__ == '__main__':
	main()