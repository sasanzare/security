#!/usr/bin/python3
# directories v 0.1.0 by @sasanzare 2022/07/20
import requests
import termcolor

#Made by sasan zare
print(termcolor.colored(''' 
    ================================+================================
                    _______  _______  _______  _______
                   (  ____ \(  ___  )/ ___   )(  ___  )
                   | (    \/| (   ) |\/   )  || (   ) |
                   | (_____ | (___) |    /   )| (___) |
                   (_____  )|  ___  |   /   / |  ___  |
                         ) || (   ) |  /   /  | (   ) |
                   /\____) || )   ( | /   (_/\| )   ( |
                   \_______)|/     \|(_______/|/     \|
     directories
     By: @sasanzare
    ================================+================================
    ''', 'cyan'))

target_url = input('[*] Please Enter Target URL: ')
file_name = input('[*] Please Enter Name Of The File Containing Directories: ')


def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass


file = open(file_name, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url + '/' + directory
	response = request(full_url)
	if response:
		print('[*] Discovered Directory At This Path: ' + full_url)
