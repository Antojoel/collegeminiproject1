from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os


def tweet(email, password, message, filen):
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpt")
    options = webdriver.ChromeOptions()
    options.add_argument(
        r"user-data-dir={}".format(profile))
    print(filen)

    if filen != None:
        if os.path.isabs(filen):
            filep = filen
        else:
            filep = os.path.join(dir_path, filen)

    driver = webdriver.Chrome(
        'C:\chrome\chromedriver.exe', chrome_options=options)

    driver.get('https://www.twitter.com/login')

    email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
    next_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'
    password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input'
    login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[3]/div/div'

    time.sleep(5)
    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(1)
    driver.find_element_by_xpath(next_xpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath(login_xpath).click()
    time.sleep(5)

    message_btn = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
    media = '//input[@accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm"][@data-testid="fileInput"]'
    tweet = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div'
    driver.find_element_by_xpath(message_btn).click()
    driver.find_element_by_xpath(message_xpath).send_keys(message)
    time.sleep(0.5)
    if filen != None:
        driver.find_element_by_xpath(media).send_keys(filep)
        time.sleep(3)
    driver.find_element_by_xpath(tweet).click()
    time.sleep(5)
    driver.quit()
