import pywhatkit
import os
from instabot import Bot

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

import smtplib

def email(username,password,touser,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username,password)
    server.sendmail(username,password, message)


def whats_app(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute)


def twitter(message):
    def account_info():
        with open('account_info.txt', 'r') as f:
            info = f.read().split()
            email = info[0]
            password = info[1]
        return email, password

    email, password = account_info()

    options = Options()
    options.add_argument("start.maximized")
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.twitter.com/login')

    email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'

    time.sleep(2)

    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(login_xpath).click()

    tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
    send_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'
    time.sleep(4)

    driver.find_element_by_xpath(tweet_xpath).click()
    time.sleep(0.5)
    driver.find_element_by_xpath(message_xpath).send_keys(message)
    time.sleep(0.5)
    driver.find_element_by_xpath(send_xpath).click()
    time.sleep(120)

def instagram(Username,Password,picture,caption):

    bot = Bot()
    bot.login(username =f"{Username}",password = f"{Password}")
    bot.upload_photo(f"{picture}",f"{caption}")




