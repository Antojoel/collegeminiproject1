from instabot import Bot
import os

def instagram(Username,Password,picture,caption):
    try:
        #
        #os.remove()
        bot=Bot()
        bot.login(username =f"{Username}",password = f"{Password}")
        bot.upload_photo(f"{picture}",f"{caption}")
        bot.logout()
        
        return(1)
    except:
        return('err')
        
