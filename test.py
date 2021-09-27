# from selenium import webdriver
# from selenium.webdriver.chrome import options
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import time
# import os

# driver = webdriver.Chrome()

# driver.get('https://www.twitter.com/login')

# email_xpath = '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'''
# next_xpath = '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'''
# password_xpath = '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input'''
# login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[3]/div/div'

# email = "antojoel8020@gmail.com"
# password = "asmaproject"



# time.sleep(5)
# driver.find_element_by_xpath(email_xpath).send_keys(email)
# time.sleep(1)
# driver.find_element_by_xpath(next_xpath).click()
# time.sleep(3)
# driver.find_element_by_xpath(password_xpath).send_keys(password)
# time.sleep(1)
# driver.find_element_by_xpath(login_xpath).click()



#importing all dependencies
import numpy as np
import tweepy

#variables for accessing twitter API
consumer_key='L1MTJBJe0Gg58kKJdJVsuj86y'
consumer_secret_key='y5kOdlFScqeotHjjJsNyLgIFoA8lHPi8ErlHYHkbcjfkAjHQhm'
access_token='945920379536654336-pHxcILWxTl5mRoG1qTD1iSbhgYHD1ud'
access_token_secret='RTESyfWBLXEu4gUucX97qYpGfTiTRkpKICWfGQ6wWhLNT'

#authenticating to access the twitter API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

tweet_text="hello world"
image_path =r"D:\vscode\python\collegeminiproject1\test cases\hello.jpg"

#Generate text tweet with media (image)
status = api.update_with_media(image_path, tweet_text)
api.update_status(status=tweet_text)

