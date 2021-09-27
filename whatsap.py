import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def message(contact, text, filen):
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
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
        "c:\chrome\chromedriver.exe", chrome_options=options)

    driver.get("https://web.whatsapp.com")
    time.sleep(10)

    inp_xpath_search = '//div[@class="_13NKt copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]'
    input_box_search = WebDriverWait(driver, 50).until(
        lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact)
    time.sleep(2)
    selected_contact = driver.find_element_by_xpath(
        "//span[@title='"+contact+"']")
    selected_contact.click()

    inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@contenteditable="true"][@data-tab="9"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(2)

    input_box.send_keys(text + Keys.ENTER)
    time.sleep(2)

    if filen != None:
        attach = '//*[@id="main"]/footer/div[1]/div/div/div[1]/div[2]/div/div'
        input_xpath = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"][@type="file"]'
        send = '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span'

        driver.find_element_by_xpath(attach).click()
        time.sleep(5)
        driver.find_element_by_xpath(input_xpath).send_keys(filep)
        time.sleep(10)
        driver.find_element_by_xpath(send).click()
    time.sleep(5)
    driver.quit()
