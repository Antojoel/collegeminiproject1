import eel
from whatsap import message
from twitter import tweet
from timedelta import timed


def asma():
    def whatsapp(contact, mesage, doc):
        message(contact, mesage, doc)

    def twitter(email, passw, message, doc):
        tweet(email, passw, message, doc)

    eel.init('web')

    @eel.expose
    def dummy(message, social, user, passw, contact, doc, time):
        if social == 'Whatsapp':
            print(time)
            print(doc)
            timed(time)
            whatsapp(contact, message, doc)
            return(0)
        elif social == 'Twitter':
            timed(time)
            twitter(user, passw, message, doc)
            return(0)
        else:
            timed(time)

    eel.start('index.html', size=(1200, 1000))


asma()
