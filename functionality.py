from selenium import webdriver
from selenium.webdriver.edge.service import Service
import random
from csv import *
import csv
import smtplib
from email.mime.text import MIMEText

def get_message(lists):
    ser = Service("C:\\Users\\Victor\\coding_projects\\python_projects\\ig_bot\\msedgedriver.exe")
    browser = webdriver.Edge(service = ser)
    browser.implicitly_wait(20)

    page = random.randint(1, 100)
    quote_num = random.randint(1, 30)
    topic = lists[random.randint(1,len(lists)) - 1]
    browser.get('https://www.goodreads.com/quotes/tag/' + topic + '?page=' + str(page))

    li = []

    for item in browser.find_elements_by_css_selector("div.quoteText"):
        li.append(item.text)

    browser.quit()

    print(li[quote_num - 1])

def add_mailing_list(contact_type, carrier, contact, selections):
    data = [contact_type, carrier, contact, selections]

    with open('mailing_list.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(data)

def send_message():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login( 'vtheman432@gmail.com', '<gmail_password>' )

    with open('mailing_list.csv', 'r') as read_obj:
        reader = csv.reader(read_obj)
        for row in reader:
            if (row[0] == "email"):
                server.sendmail("vtheman432@gmail.com", row[2], get_message(row[3]))