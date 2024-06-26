from time import sleep
from webbrowser import get
from pyfiglet import Figlet
import requests
from colorama import Fore, Back, Style
from tqdm import tqdm
import pyshorteners
import folium 
#from tkinter import *
import pyautogui
import keyboard
import socket
import webbrowser
import pandas



def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		#print(response)



		data = {
			
			'[IP]': response.get('query'),
			'[Int prov]': response.get('isp'),
			'[Region Name]': response.get('regionName'),
			'[City]': response.get('city'),
			'[ZIP]': response.get('zip'),
			'[Lat]': response.get('lat'),
			'[Lon]': response.get('lon'),

		}


	

		for k, v in data.items():
			print(f'{k} : {v}' + Fore.GREEN)
			
		m = folium.Map(location=[response.get("lat"), response.get("lon"),])
		#m.save(f'{response.get("query")}_{response.get("city")}.html')
		folium.Marker(
    		location=[response.get("lat"), response.get("lon"),],
    		tooltip="Click me!",
    		popup="Near by",
    		icon=folium.Icon(color="green"),
	).add_to(m)
		"""folium.Marker(
    		location=[response.get("lat"), response.get("lon"),],
    		tooltip="Click me!",
    		popup="Timberline Lodge",
    		icon=folium.Icon(color="green"),
	).add_to(m)"""
		m.save(f'{response.get("query")}_{response.get("city")}.html')


	except requests.exceptions.ConnectionError:
		print('[!] Please check your connection!')



def main():
	

# main xd
	
	ip = input('Please enter a target IP: ' + Fore.GREEN)



	"""for i in tqdm(range(1, 500), colour='green'):
		sleep(random.uniform(0.01, 0.1))"""
		

	get_info_by_ip(ip=ip)


	font_text = Figlet(font='slant')
	print(font_text.renderText('IP INFO'))
	sleep(0.05)
# delay 0.05, 0.01


if __name__ == '__main__':
	main()



sleep(0.1)

print('Press Esc to EXit')

"""url = 'https://github.com/LikeNugesC'
print(webbrowser.get()) #chrome, microsoft edge
webbrowser.open_new(url)"""

sleep (0.5)

while 1:
	if keyboard.is_pressed('esc'):
		print('EXIT')
		break
