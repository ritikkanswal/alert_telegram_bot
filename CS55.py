import requests
import datetime
import time
import schedule
import json
from decouple import config
import os

link="https://api.telegram.org/bot"
token=config('SECRET_KEY')
chat_id="-1001221415233"

#fetching data from json file
def Days():
    with open("Time_Table_Data/CS55.json") as f:
        Data=json.load(f)
    return Data

Data=Days()
#sending message back to telegram bot 
def job(Dict):

    Url="{0}{1}/sendMessage?chat_id={2}&text={3}".format(link,token,chat_id,Dict['title'])
    requests.get(Url)
    time.sleep(2)

    Url="{0}{1}/sendMessage?chat_id={2}&text={3}".format(link,token,chat_id,Dict['url'])
    requests.get(Url)

    print("sended")


#logic part
for Dict in Data:
    if(Dict['day'].lower()=="monday"):
        schedule.every().monday.at(Dict['time']).do(job,Dict)
    elif(Dict['day'].lower()=="tuesday"):
        schedule.every().tuesday.at(Dict['time']).do(job,Dict)
    elif(Dict['day'].lower()=="wednesday"):
        schedule.every().wednesday.at(Dict['time']).do(job,Dict)
    elif(Dict['day'].lower()=="thursday"):
        schedule.every().thursday.at(Dict['time']).do(job,Dict)
    elif(Dict['day'].lower()=="friday"):
        schedule.every().friday.at(Dict['time']).do(job,Dict)
    elif(Dict['day'].lower()=="saturday"):
        schedule.every().saturday.at(Dict['time']).do(job,Dict)
    elif(Dict['day'].lower()=="sunday"):
        schedule.every().sunday.at(Dict['time']).do(job,Dict)

while True:
    schedule.run_pending()
    time.sleep(1)
