from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

def tweet (email,password,message,filen="cd")
    dir_path = os.getcwd()
    options = webdriver.ChromeOptions()

    if os.path.isabs(filen):
        filep=filen
    else:
        filep=os.path.join(dir_path,filen)

    driver = webdriver.Chrome('C:\chrome\chromedriver.exe',chrome_options=options)

    driver.get('https://www.twitter.com/login')

    email_xpath = "//input[@type='text'][@name='session[username_or_email]']"
    password_xpath = "//input[@type='password'][@name='session[password]']"
    login_xpath = '//div[@role="button"][@data-testid="LoginForm_Login_Button"]'

    time.sleep(5)
    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(1)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath(login_xpath).click()
    time.sleep(5)

    message_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
    media='//input[@accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm"][@data-testid="fileInput"]'
    tweet='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'

    driver.find_element_by_xpath(message_xpath).send_keys(message)
    time.sleep(0.5)
    if filen!="cd":
        driver.find_element_by_xpath(media).send_keys(filep)
        time.sleep(0.5)
    driver.find_element_by_xpath(tweet).click()
    time.sleep(5)