#!/usr/bin/python3
# Email scarper v 0.1.0 by @sasanzare 2022/07/10
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

#Made by sasan zare
print(''' 
    ================================+================================
                    _______  _______  _______  _______
                   (  ____ \(  ___  )/ ___   )(  ___  )
                   | (    \/| (   ) |\/   )  || (   ) |
                   | (_____ | (___) |    /   )| (___) |
                   (_____  )|  ___  |   /   / |  ___  |
                         ) || (   ) |  /   /  | (   ) |
                   /\____) || )   ( | /   (_/\| )   ( |
                   \_______)|/     \|(_______/|/     \|
     Email scarper
     By: @sasanzare
    ================================+================================
    ''')

user_url = str(input('[+] Please Enter Target URL To Scan : '))
processes = int(input('[ ] Please Enter The Number Of Processes : '))

urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0

try:
    while len(urls):
        if count == processes:
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
        count += 1
except KeyboardInterrupt:
    print('''
    =========================  [-] Closing!  ========================''')
print('')
for mail in emails:
    print(mail)
    
print('''
    =====================  Have A Hacking Time  =====================''')