import re
import smtplib
import time

import requests
from bs4 import BeautifulSoup

url = "https://tieba.baidu.com/p/6987793570"
message = """From: From Person <2692632421@qq.com>
To: To Person <1534114641@qq.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
sender = '2692632421@qq.com'
recevier = ['1534114641@qq.com', '951772682@qq.com', '2692632421@qq.com']
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"}
while 1:
    h = requests.get(url, headers=headers)
    h.encoding = h.apparent_encoding
    soup = BeautifulSoup(h.text, "html.parser")
    num = soup.find_all('span', class_="red")[1:2]

    num = str(num)
    pages = re.findall(r'\d+', num)
    time.sleep(5)
    url = url + '?pn='+ pages[0]
    fifa = requests.get(url, headers=headers)
    fifa.encoding = fifa.apparent_encoding
    soup = BeautifulSoup(fifa.text, "html.parser")
    fl = soup.find_all('span', class_="tail-info")[::-1]
    fl = fl[1:2]
    fl = str(fl)
    fl = re.findall(r'\d+', fl)
    for x in fl:
        if x[2] >='6'and x[3] >= '8' : 
            if x[2] <= '7' and x[3] <= '9':     
                smtp = smtplib.SMTP_SSL("smtp.qq.com")
                smtp.login('2692632421@qq.com', 'bpxbecooseuodcfg')
                smtp.sendmail(sender, recevier, message)
                smtp.quit()
        else:
            print(fl)
            break
    time.sleep(10)
