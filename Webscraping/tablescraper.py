#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
TableScraper

All code in here should be universal for all tables!


"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import termcolor
from art import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

date_time = datetime.datetime.now()

art = text2art("TABLE WEBSCRAPER", font='small', chr_ignore=True)
print(termcolor.colored(art, 'green'))
print(termcolor.colored('BY HippoTheHacker', 'green'))
print(termcolor.colored(date_time.strftime("%H:%M %d-%B-%Y"), 'green'))
print()


#Hardcoded website
url = 'https://www.cryptocurrencychart.com/'


page = requests.get(url)
page.text
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table', class_= 'market-cap-list', id = 'currency-table')

##############################################
table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns = headers)

############################################

table.find_all('tr')[1:]

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [td.text for td in row_data]
    length = len(df)
    df.loc[length] = row

############################################

#df.to_excel('C:/scraping/scraped.xls')
df.to_csv('C:/scraping/scraped.csv')

#Input the email account that will send the email and who will receiving it
sender = 'YOUR GMAIL HERE'
receiver = 'YOUR GMAIL HERE'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Crypto Table'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('C:/scraping/scraped.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="scraped.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'YOUR GMAIL HERE', password = 'PASSWORD')
s.sendmail(sender, receiver, msg.as_string())
s.quit()


print(termcolor.colored('EXCEL EXPORTED TO FOLDER! ٩(^‿^)۶ ', 'green'))
print(termcolor.colored('AND EMAIL SENT! ٩(^‿^)۶ ', 'green'))
    