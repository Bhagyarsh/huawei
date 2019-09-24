import csv
from networkconnection import internet_on
import json
from rename import rename
from uvid import getuvid
import requests
import time
import delete
import json
import os
uid = getuvid()

def sentsavedata(slave_id,url):
        file_name = uid + slave_id +".csv"
        if os.path.exists(file_name):
                sentsavefile(url,uid,file_name)
def createfile(file_name):
    with open(file_name, mode='w') as csv_file:
        fieldnames = [
            'uvid',
            'slave',
            'power',
            'energy',
            'recordedAt'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()


def sentsavefile(url,uvid,file_name):
        print("sending save data")
        r = requests.get(url = "https://solardata2.tk")
        if internet_on():
                print("net is on ==> sending save data !!")
                with open(file_name,'rb') as f:
                        files ={"datafile":f}
                        value = {"uvid":uvid}
                        r = requests.post(url,files=files,data=value,timeout=60*2)
                        print(r)
                        print(r.content)
                        if (r.status_code==200):
                                delete.delete(file_name)
                                print("deleting file")
                                









































































































































































































































































































































































