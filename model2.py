from bs4 import BeautifulSoup
from random import choice
import urllib
import re
import os,sys,time
import requests
import webbrowser
import pyautogui
import utils as ut 
import csv
import glob
def get_name(addrs):
    str_list = list(addrs.split('/'))
    uname = str_list[0]
    #oname = uname[13:]
    return uname
#getting district names and number of pages       
data,dists = ut.get_district()
path = os.getcwd()
for district in dists:
    max_num = data['{}'.format(district)]
    #os.system("taskkill /im firefox.exe /f")
    try:
        fname = get_name(district)
        sfile = "{}.csv".format(fname)
        fields = ['Name','Mobile number','adress'] 
        os.chdir(os.path.join(path,'CDATA'))
        with open(sfile, 'a',encoding='utf-8',newline='') as csvfile:
            csvwriter = csv.writer(csvfile) 
                # writing the fields 
            csvwriter.writerow(fields)
            os.chdir(path)
            page_number = 1
            while True:
                if page_number>max_num:
                    break
                #url="https://www.justdial.com/%s/Mosques/nct-10328437/page-%s" % (district,page_number)
                chrome_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(chrome_path),1)
                webbrowser.get('firefox').open_new_tab(url="https://www.justdial.com/%s/nct-10253670/page-%s" % (district,page_number))
                time.sleep(12)
                pyautogui.hotkey('ctrl', 's')
                time.sleep(1)
                #pyautogui.typewrite('temp{}'.format(page_number))
                #time.sleep(2)
                pyautogui.press('enter')
                time.sleep(8)
                pyautogui.click(1479,12)
                extension = 'htm'
                all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
                for htm_file in all_filenames:
                    page = open(htm_file,'r',encoding='utf-8')
                    #page = urllib.request.urlopen(req , proxy , timeout=5)
                    #time.ctime(1)
                    # page=urllib2.urlopen(url)
                    soup = BeautifulSoup(page.read(), "html.parser")
                    services = soup.find_all('li', {'class': 'cntanr'})
                    # Iterate through the 10 results in the page
                    for service_html in services:
                        # Parse HTML to fetch data
                        name = ut.get_name(service_html)
                        phone = ut.get_phone_number(service_html)
                        #rating = get_rating(service_html)
                        #count = get_rating_count(service_html)
                        address = ut.get_address(service_html)
                        #location = get_location(service_html)
                        #data = [name, phone, address]
                        # creating a csv writer object        
                        csvwriter.writerow([name, phone, address])
                    page.close()
                    os.remove(htm_file)
                page_number+=1
            os.system("taskkill /im firefox.exe /f")
            if max_num>2:
                time.sleep(8)
            else:
                time.sleep(10)
            csvfile.close()
    except FileNotFoundError:
        pass
print('process completed successfully')

'''
def save_html(page_number):
    pyautogui.hotkey('ctrl', 's')
    time.sleep(5)
    pyautogui.typewrite('temp{}'.format(page_number))
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
def htm_gen(max_num):
    page_number = 1
    while True:
        if page_number>max_num:
            break
        #url="https://www.justdial.com/%s/Mosques/nct-10328437/page-%s" % (district,page_number)
        chrome_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(chrome_path),1)
        webbrowser.get('firefox').open_new_tab(url="https://www.justdial.com/%s/Mosques/nct-10328437/page-%s" % (district,page_number))
        time.sleep(5)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(3)
        pyautogui.typewrite('temp{}'.format(page_number))
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(8)
        #time.sleep(5)
        #save_html(page_number)
        #get_html(url,page_number)
        print('page{} process ended at: '.format(page_number)+time.ctime())
        page_number+=1
        os.system("taskkill /im firefox.exe /f")
'''