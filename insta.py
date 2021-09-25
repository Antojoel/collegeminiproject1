from instabot import Bot
import os

def instagram(Username,Password,picture,caption):
    
    try:
               
        bot=Bot()
        bot.login(username =f"{Username}",password = f"{Password}")
        bot.upload_photo(f"{picture}",f"{caption}")
        bot.logout()
        filn=Username+'_uuid_and_cookie.json'
        filp='config\\'+filn
        os.remove(filp)
        ren=picture+'.REMOVE_ME'
        os.rename(ren,picture)
        return(1)
    
    except OSError as e:
        return(3)

    except:
        bot.logout()
        filn=Username+'_uuid_and_cookie.json'
        filp='config\\'+filn
        os.remove(filp)
        return(2)
