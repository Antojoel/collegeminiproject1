import eel

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pywhatkit

def whatsapp(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute)

def twitter(email,password, message):

    options = Options()
    options.add_argument("start.maximized")
    driver = webdriver.Chrome('C:\chrome\chromedriver.exe')

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
    time.sleep(5)
    driver.quit()

eel.init('web')

@eel.expose
def dummy(message,time,social,user,passw,ph_no):
    ti=time.split(':')
    if social=='Whatsapp':
       whatsapp(ph_no,message,int(ti[0]),int(ti[1]))
       return(0)
    elif social=='Twitter':
        twitter(user,passw,message)
        return(0)
    else:
        #instagram(user,passw,message,message)
        pass
        

eel.start('index.html',size=(1000,800))