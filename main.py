import eel

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from whatsap import whatsapp
from twitter import tweet
from insta import instagram
from timedelta import timed

def whatsapp(contact, message,doc):
    whatsapp(contact,message,doc)


def twitter(email,passw, message,doc):
    tweet(email,passw,message,doc)

eel.init('web')

@eel.expose
def dummy(message,social,user,passw,contact,doc,time):
    if social=='Whatsapp':
        timed(time)
        whatsapp(contact,message,doc)
        return(0)
    elif social=='Twitter':
        timed(time)
        twitter(user,passw,message)
        return(0)
    else:
        timed(time)
        return(instagram(user,passw,doc,message))
        
        

eel.start('index.html',size=(1000,800))