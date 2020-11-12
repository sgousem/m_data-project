from bs4 import BeautifulSoup
from random import choice
import urllib
import re
import os,sys,time
import requests
import webbrowser
import pyautogui
import pandas as pd
#dictionary for mobile number from just dial
mob_dict = {
        'mobilesv icon-dc':'+',
        'mobilesv icon-fe' :'(',
        'mobilesv icon-hg' :')',
        'mobilesv icon-ba' :'-',
        'mobilesv icon-acb' : '0',
        'mobilesv icon-yz' : '1',
        'mobilesv icon-wx' : '2',
        'mobilesv icon-vu' : '3',
        'mobilesv icon-ts' : '4',
        'mobilesv icon-rq' : '5',
        'mobilesv icon-po' : '6',
        'mobilesv icon-nm' : '7',
        'mobilesv icon-lk' : '8',
        'mobilesv icon-ji' : '9' }
#proxy function used to get random ip address fro free proxies
def get_proxy():
    url = "https://www.sslproxies.org/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html5lib')
    return {'https':choice(list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x:x.text,soup.find_all('td')[::8]),
                        map(lambda x:x.text,soup.find_all('td')[1::8]))))))}
#html file format save function
def get_html(url1,number):
    chrome_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(chrome_path),1)
    webbrowser.get('firefox').open_new_tab(url=url1)
    time.sleep(10)
    #pyautogui.moveTo(1355,92)
    #pyautogui.dragTo(1355,708,5,button='left')
    #time.sleep(5)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(3)
    pyautogui.write('temp{} '.format(number),0.5)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

#functions used to get name, address,mobile number
def get_name(body):
    #time.sleep(1)
    return body.find('span', {'class':'jcn'}).a.string

def get_phone_number(body):
	try:
		mob_num_list = [ ]
		numlist =  body.find('p', {'class':'contact-info'}).span
		num_class = re.findall(r'mobilesv icon-[a-z]{2,}',str(numlist))
		for numref in num_class:
			mob_num_list.append(mob_dict[numref])
		mn = mob_num_list[6:]
		fmn = ("".join([str(i) for i in mn]))
		return fmn
	except AttributeError:
		return ''
def get_address(body):
    #time.sleep(1)
    return body.find('span', {'class':'mrehover'}).text.strip()
def get_district():
    df = pd.read_csv('distfile.csv')
    dists = list(df['name'].str.title())
    max_num = list(df['number'])
    data = dict(zip(dists,max_num))
    return data,dists