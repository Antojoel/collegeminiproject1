import time

def timed(timen):
    if timen=="":
        return
    tim=timen.split(':')
    time_hour=int(tim[0]) 
    time_min=int(tim[1])

    callsec = (time_hour*3600)+(time_min*60)
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    print(lefttm)
    time.sleep(lefttm-10)