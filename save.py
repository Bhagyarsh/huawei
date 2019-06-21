import csv
from networkconnection import internet_on
import json
from usim800 import sim800
from rename import rename
from uvid import getuvid
import requests
import time
import delete
uid = getuvid()
GSM = False
# if GSM:
#     gsm = sim800(baudrate=9600, path="/dev/ttys1")
#     gsm.requests.APN = "www"
def createfile(file_name):

    with open(file_name, mode='w') as csv_file:

        fieldnames = [
            "uvid",
            "slave",
            "pv1_voltage",
            "pv2_voltage",
            "pv3_voltage",
            "pv4_voltage",
            "pv5_voltage",
            "pv6_voltage",
            "pv1_current",
            "pv2_current",
            "pv3_current",
            "pv4_current",
            "pv5_current",
            "pv6_current",
            "pv1_power",
            "pv2_power",
            "pv3_power",
            "daily_energy",
            "total_energy",
            "annual_energy",
            "offline",
            "recordedAt",
            "Active_power_peak_of_current_day",
            "Active_power",
            "Device_status",
            "Reactive_power",
            "Power_factor",
            "Inverter_efficiency",
            "Cabinet_temperature",
            "vers",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()


def sentsavedata(file_name, temp_file, url,vers):
    createfile('temp.csv')
    line = 0
    with open(file_name, 'r') as inp, open(temp_file, 'a') as out:

        writer = csv.writer(out)
        for row in csv.reader(inp):
            print(line)
            if line != 0:
                data = {
                    "uvid": row[0],
                    "slave": row[1],
                    "pv1_voltage": row[2],
                    "pv2_voltage": row[3],
                    "pv3_voltage": row[4],
                    "pv1_current": row[8],
                    "pv2_current": row[9],
                    "pv3_current":row[10],
                    "pv1_power": row[14],
                    "pv2_power": row[15],
                    "pv3_power":row[16],
                    "daily_energy":row[17],
                    "total_energy":  row[18],
                    "annual_energy": row[19],
                    "other": str({"pv4_voltage": row[5],
                                "pv5_voltage": row[6],
                                "pv6_voltage": row[7],
                                "pv4_current": row[11],
                                "pv5_current": row[12],
                                "pv6_current":row[13],
                                "Active_power_peak_of_current_day":row[22],
                                "Active_power":row[23],

                                "Device_status":row[24],
                                "Reactive_power":row[25],
                                "Power_factor":row[26],
                                "Inverter_efficiency":row[27],
                                "Cabinet_temperature":row[28],
                                "vers":row[29]}),
                    "offline": 1,
                    "recordedAt": row[21],

                }

                headers = {'Content-type': 'application/json'}

                try:
                    print(data)
                    if not GSM:
                        r = requests.post(url, data=json.dumps(data),
                                      headers=headers, timeout=1)
                    else :
                        r = gsm.requests.post(url=url,data=json.dump(data))
                    print(r)
                    print(r.content)
                    time.sleep(2)
                except requests.ConnectionError:
                    writer.writerow(row)
                    print('no net')
                except requests.exceptions.ReadTimeout:
                    writer.writerow(row)
                    print('timeout')
            line += 1
    delete.delete(file_name)
    rename(temp_file, file_name)
