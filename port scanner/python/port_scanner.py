#!/usr/bin/python3
# Port scanner v 0.1.0 by @sasanzare 2022/07/12

import socket
import termcolor


def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(termcolor.colored(("[+] Port Opened " + str(port)), 'green'))
		sock.close()
	except:
		pass

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
     Port scanner
     By: @sasanzare
    ================================+================================
    ''', 'cyan'))

targets = input("[*] Please Enter Targets To Scan(split them by , ) : ")
ports = int(input("[*] Please Enter How Many Ports You Want To Scan : "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'yellow'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)

print(termcolor.colored('''
    =====================  Have A Hacking Time  =====================''', 'magenta'))