import eel

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from whatsap import message
from twitter import tweet
from insta import instagram
from timedelta import timed

def whatsapp(contact, mesage,doc):
    message(contact,mesage,doc)


def twitter(email,passw,message,doc):
    tweet(email,passw,message,doc)

eel.init('web')

@eel.expose
def dummy(message,social,user,passw,contact,doc,time):
    #rdoc=r"{}".format(doc)
    if social=='Whatsapp':
        timed(time)
        whatsapp(contact,message,doc)
        return(0)
    elif social=='Twitter':
        timed(time)
        twitter(user,passw,message,doc)
        return(0)
    else:
        timed(time)
        return(instagram(user,passw,rdoc,message))
        
        

eel.start('index.html',size=(1200,1000))