import random


def generate_Cart_ID(self):
    choice = '0123456789abcdefghijklmnopqrstuvwxyz'
    SIZE = 10+26

    cartID = ''

    for i in range(0, SIZE):
        c = random.randint(0,SIZE-1)
        cartID+=choice[c]
    
    return cartID

def t1():
    for i in range(1,10,2):        
        print(i)

import datetime
def t2():
    t = datetime.date.today.__str__
    t2 = datetime.date.today.__str__
    
    print("@",t)

#messing around with time and datetime
import time #has strftime
import datetime #has strftime too?
def t3():
    print("Time in seconds since the epoch:%s"  %time.time())
    print("Current date and time: ", datetime.datetime.now())
    print("Or like this: ",datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

    print("Current year: ", datetime.date.today().strftime("%Y"))
    print("Month of year: ", datetime.date.today().strftime("%B"))
    print("Week number of the year: ", datetime.date.today().strftime("%W"))
    print("Weekday of the week: ", datetime.date.today().strftime("%w"))
    print("Day of year: ", datetime.date.today().strftime("%j"))
    print("Day of the month : ", datetime.date.today().strftime("%d"))
    print("Day of week: ", datetime.date.today().strftime("%A"))

import time
import datetime
def t4():
    past = datetime.datetime(1998, 12, 5, 2, 23, 54, 199)
    now = datetime.datetime.now()
    print("-"*25)
    print("NOW: ", now)
    print("NOW YEAR: ",now.year)
    print("NOW MONTH: ",now.month)

    
    print("PAST IS: ",past)


    
    

    




def run():
    t4()
    

run()
