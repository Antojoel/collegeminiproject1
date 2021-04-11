import pywhatkit

def whatsapp(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute)