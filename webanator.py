#!/bin/python3

import os
import re
import time
import socket
import http.client
import requests
import threading
from queue import Queue
from colorama import Fore, Style
from colorama import Fore as colour

RED = colour.RED
CYAN = colour.CYAN
BLUE = colour.BLUE
WHITE = colour.WHITE
GREEN = colour.GREEN
YELLOW = colour.YELLOW

def banner():
	os.system('clear')
	print("")
	colors = [BLUE, RED, WHITE] * 10
	for i, line in enumerate("""
██╗    ██╗███████╗██████╗  █████╗ ███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗
██║    ██║██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
	""".strip().split("\n")):
		print(f"{colors[i]} {line}")
	print("")
	print(f"{RED}[{WHITE}!!!{RED}] {BLUE}Tool-Name {WHITE}: {RED}WEBANATOR")
	print(f"{RED}[{WHITE}!!!{RED}] {BLUE}Github    {WHITE}: {RED}https://github.com/K3ysTr0K3R")
	print(f"{RED}[{WHITE}!!!{RED}] {BLUE}Instagram {WHITE}: {RED}jaredbrts175")
	print(f"{RED}[{WHITE}!!!{RED}] {BLUE}Coded By  {WHITE}: {RED}K3ysTr0K3R")
banner()
print("")
print(f"{BLUE}========================================================")
print(f"{RED}[{WHITE}???{RED}] Checking internet connection{BLUE}...")

try:
	connect_google = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	CONNECTION = connect_google.connect_ex(('www.google.com',80))
	if (CONNECTION == 0):
		print(f"{GREEN}[{BLUE}+++{GREEN}] Internet Connection Established: {CYAN}Proceeding")
		print(f"{BLUE}========================================================")
		banner()
except socket.gaierror:
	print(f"{RED}[{WHITE}!!!{RED}] No Internet Connection Found{BLUE}: {RED}Exiting")
	print(f"{BLUE}========================================================")
	exit()

B = BLUE
R = RED
W = WHITE
print("")
option = input(f"""{B}╔════════════════════════════════════════════════════════════════════════════╗
{R}║ {R}[{W}1{R}] {W}USA                         {R}║ {R}[{W}13{R}] {W}China                               {R}║
{W}║ {R}[{W}2{R}] {W}Canada                      {W}║ {R}[{W}14{R}] {W}Japan                               {W}║
{B}║ {R}[{W}3{R}] {W}Mexico                      {B}║ {R}[{W}15{R}] {W}North Korea                         {B}║
{R}║ {R}[{W}4{R}] {W}Brazil                      {R}║ {R}[{W}16{R}] {W}Taiwan                              {R}║
{W}║ {R}[{W}5{R}] {W}Romania                     {W}║ {R}[{W}17{R}] {W}American Samoa                      {W}║
{B}║ {R}[{W}6{R}] {W}Nigeria                     {B}║ {R}[{W}18{R}] {W}Netherlands                         {B}║
{R}║ {R}[{W}7{R}] {W}South Africa                {R}║ {R}[{W}19{R}] {W}India                               {R}║
{W}║ {R}[{W}8{R}] {W}France                      {W}║ {R}[{W}20{R}] {W}Switzerland                         {W}║
{B}║ {R}[{W}9{R}] {W}Madagascar                  {B}║ {R}[{W}21{R}] {W}Tanzania                            {B}║
{R}║ {R}[{W}10{R}] {W}Russia                     {R}║ {R}[{W}22{R}] {W}Belarus                             {R}║
{W}║ {R}[{W}11{R}] {W}Germany                    {W}║ {R}[{W}23{R}] {W}Estonia                             {W}║
{B}║ {R}[{W}12{R}] {W}Finland                    {B}║ {R}[{W}24{R}] {W}Slovenia                            {B}║
{R}╚════════════════════════════════════════════════════════════════════════════╝

{RED}[{WHITE}?{RED}] {WHITE}Choose the country you would like to gather webcams from{BLUE}: """)

if option == "":
	print(f"{RED}[{WHITE}!{RED}] You must pick an option")
	exit()
elif option == "1":
	country_code = "US"
elif option == "2":
	country_code = "CA"
elif option == "3":
	country_code = "MX"
elif option == "4":
	country_code = "BR"
elif option == "5":
	country_code = "RO"
elif option == "6":
	country_code = "NG"
elif option == "7":
	country_code = "ZA"
elif option == "8":
	country_code = "FR"
elif option == "9":
	country_code = "MG"
elif option == "10":
	country_code = "RU"
elif option == "11":
	country_code = "DE"
elif option == "12":
	country_code = "FI"
elif option == "13":
	country_code = "CN"
elif option == "14":
	country_code = "JP"
elif option == "15":
	country_code = "NK"
elif option == "16":
	country_code = "TW"
elif option == "17":
	country_code = "AS"
elif option == "18":
    country_code = "NL"
elif option == "19":
    country_code = "IN"
elif option == "20":
    country_code = "CH"
elif option == "21":
    country_code = "TZ"
elif option == "22":
    country_code = "BY"
elif option == "23":
    country_code = "EE"
elif option == "24":
    country_code = "SI"
elif option == "25":
    country_code = "MY"
elif option == "26":
    country_code = "AE"
    
else:
	print("[!] Invalid option selected")
	print("[!] Aborting")
	exit()

if country_code == "US":
	country_name = "United States"
elif country_code == "CA":
	country_name = "Canada"
elif country_code == "MX":
	country_name = "Mexico"
elif country_code == "BR":
	country_name = "Brazil"
elif country_code == "RO":
	country_name = "Romania"
elif country_code == "NG":
	country_name = "Nigeria"
elif country_code == "ZA":
	country_name = "South Africa"
elif country_code == "FR":
	country_name = "France"
elif country_code == "MG":
	country_name = "Madagascar"
elif country_code == "RU":
	country_name = "Russia"
elif country_code == "DE":
	country_name = "Germany"
elif country_code == "FI":
	country_name = "Finland"
elif country_code == "CN":
	country_name = "China"
elif country_code == "JP":
	country_name = "Japan"
elif country_code == "NK":
	country_name == "North Korea"
elif country_code == "TW":
	country_name = "Taiwan"
elif country_code == "AS":
	country_name = "American Samoa"
elif country_code == "NL":
	country_name = "Netherlands"
elif country_code == "IN":
	country_name = "India"
elif country_code == "CH":
	country_name = "Switzerland"
elif country_code == "TZ":
	country_name = "Tanzania"
elif country_code == "BY":
	country_name = "Belarus"
elif country_code == "EE":
	countty_name = "Estonia"
elif country_code == "SI":
	countty_name = "Slovenia"
elif country_code == "MY":
	country_name = "Malaysia"
elif country_code == "AE":
	country_name = "United Arab Emirates"
		
banner()
print("")
print(f"{RED}[{WHITE}!{RED}] {WHITE}Scanning for webcams in{B}: {RED}{country_name}")
print("")

webcams_queue = Queue()

webcam_count = 0
max_webcams = 100

def scan(webcam, webcam_count, webcams_queue):
	#webcam
	try:
		server_name = requests.get(webcam)
		response = server_name.status_code
		server = server_name.headers['Server']
		print(f"{R}[{B}+{R}] {W}{webcam} {R}[{W}{server}{R}] {R}[{W}{response}{R}]")
		with threading.Lock():
			webcam_count += 1
			if not webcams_queue.empty() and webcam_count < max_webcams:
				new_webcam = webcams_queue.get()
				t = threading.Thread(target=scan, args=(new_webcam, webcam_count, webcams_queue))
				t.start()
			else:
				return
	except KeyError:
		pass
	except requests.exceptions.ConnectionError:
		pass
	except urllib3.exceptions.MaxRetryError:
		pass

try:
	for pages in range(1, 365):
		user_agent = {"User-Agent": "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36"}
		req_main = requests.get(f'http://www.insecam.org/en/bycountry/{country_code}/?page={pages}', headers=user_agent)
		req_source = req_main.text
		webcams = re.findall(r'http://\d+.\d+.\d+.\d+:\d+', req_source)
		# Fill the queue with the webcam URLs
		for webcam in webcams:
			webcams_queue.put(webcam)
		first_webcam = webcams_queue.get()
		t = threading.Thread(target=scan, args=(first_webcam, webcam_count, webcams_queue))
		t.start()
except KeyboardInterrupt:
	print(f"{R}[{W}!{R}] {W}Scanning terminated by the user")
	exit()
