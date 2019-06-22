import csv

def return_int_value(a, b):
    a = hex(int(a))
    b = hex(int(b))
    print
    if a == 0 and b!= 0:
        hex_a = b[2:]
    elif a==0 and b == 0 :
   	 return 0
    else:
        hex_a = a + b[2:]
    return (int(hex_a, 0))


def setData(uid, slave_id, registers,registers2,  timesend, vers):
    print("doem")
    a = registers2.get(32064)[5]["value"]
    b = return_int_value(a[0],a[1])
    total_power = b

    a = registers2.get(32078)[5]["value"]
    b = return_int_value(a[0],a[1])
    Active_power_peak_of_current_day = b/1000

    a = registers2.get(32080)[5]["value"]
    b = return_int_value(a[0],a[1])
    Active_power = b/1000

    a = registers2.get(32082)[5]["value"]
    b = return_int_value(a[0],a[1])
    Reactive_power = b/100

    a = registers2.get(32089)[5]["value"]
    b = return_int_value(a[0],a[1])
    Device_status = b

    a = registers2.get(32106)[5]["value"]
    b = return_int_value(a[0],a[1])
    totlal_energy_yeild = b/100

    a = registers2.get(32114)[5]["value"]
    b = return_int_value(a[0],a[1])
    daily_energy = b/100

    a = registers2.get(32118)[5]["value"]
    b = return_int_value(a[0],a[1])
    energy_yeild_current_year = b/100

    a = registers2.get(32116)[5]["value"]
    b = return_int_value(a[0],a[1])
    energy_yeild_current_month = b/100

    data = {
        "uvid": uid,
        "slave": slave_id,
        "pv1_voltage": int(registers.get(32016)[5]["value"]),
        "pv2_voltage": int(registers.get(32018)[5]["value"]),
        "pv3_voltage": int(registers.get(32020)[5]["value"]),
        
        "pv1_current": int(registers.get(32017)[5]["value"]),
        "pv2_current": int(registers.get(32019)[5]["value"]),
        "pv3_current": int(registers.get(32021)[5]["value"]),
        "pv1_power": total_power,
        "pv2_power": 0,
        "pv3_power":0,
        "daily_energy":daily_energy,
        "total_energy":  totlal_energy_yeild,
        "annual_energy": energy_yeild_current_year,
        "offline": 0,
        "recordedAt": timesend,
        "other": str({
                "montly_energy": energy_yeild_current_month,
                "pv4_voltage": int(registers.get(32022)[5]["value"]),
                "pv5_voltage": int(registers.get(32024)[5]["value"]),
                "pv6_voltage": int(registers.get(32026)[5]["value"]),
                "pv4_current": int(registers.get(32023)[5]["value"]),
                "pv5_current": int(registers.get(32025)[5]["value"]),
                "pv6_current": int(registers.get(32027)[5]["value"]),
                "Active_power_peak_of_current_day":Active_power_peak_of_current_day,
                "Active_power":Active_power,
                "Device_status":Device_status,
                "Reactive_power":Reactive_power,
                "Power_factor":int(registers.get(32084)[5]["value"])/10,
                "Inverter_efficiency":int(registers.get(32086)[5]["value"])/100,
                "Cabinet_temperature":int(registers.get(32087)[5]["value"])/10,
                "vers": vers})

    }
    print(data)
    return data


def writecsv(file_name, data):
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
            "montly_energy"

    ]
    print(data)

    with open(file_name, 'a') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, fieldnames)
        w.writerow(data)


def setCsvData(uid, slave_id, registers,registers2, timesend, vers):
    print("doem")
    a = registers2.get(32064)[5]["value"]
    b = return_int_value(a[0],a[1])
    total_power = b

    a = registers2.get(32078)[5]["value"]
    b = return_int_value(a[0],a[1])
    Active_power_peak_of_current_day = b/1000

    a = registers2.get(32080)[5]["value"]
    b = return_int_value(a[0],a[1])
    Active_power = b/1000

    a = registers2.get(32082)[5]["value"]
    b = return_int_value(a[0],a[1])
    Reactive_power = b/100

    a = registers2.get(32089)[5]["value"]
    b = return_int_value(a[0],a[1])
    Device_status = b

    a = registers2.get(32106)[5]["value"]
    b = return_int_value(a[0],a[1])
    totlal_energy_yeild = b/100

    a = registers2.get(32114)[5]["value"]
    b = return_int_value(a[0],a[1])
    daily_energy = b/100

    a = registers2.get(32118)[5]["value"]
    b = return_int_value(a[0],a[1])
    energy_yeild_current_year = b/100

    a = registers2.get(32116)[5]["value"]
    b = return_int_value(a[0],a[1])
    energy_yeild_current_month = b/100

    sdata = {
        "uvid": uid,
        "slave": slave_id,
        "pv1_voltage": int(registers.get(32016)[5]["value"]),
        "pv2_voltage": int(registers.get(32018)[5]["value"]),
        "pv3_voltage": int(registers.get(32020)[5]["value"]),
        "pv1_current": int(registers.get(32017)[5]["value"]),
        "pv2_current": int(registers.get(32019)[5]["value"]),
        "pv3_current": int(registers.get(32021)[5]["value"]),
        "pv4_voltage": int(registers.get(32022)[5]["value"]),
        "pv5_voltage": int(registers.get(32024)[5]["value"]),
        "pv6_voltage": int(registers.get(32026)[5]["value"]),
        "pv4_current": int(registers.get(32023)[5]["value"]),
        "pv5_current": int(registers.get(32025)[5]["value"]),
        "pv6_current": int(registers.get(32027)[5]["value"]),
        "pv1_power": total_power,
        "pv2_power": 0,
        "pv3_power":0,
        "montly_energy": energy_yeild_current_month,
        "daily_energy":daily_energy,
        "total_energy":  totlal_energy_yeild,
        "annual_energy": energy_yeild_current_year,
        "offline": 1,
        "recordedAt": timesend,
        "Active_power_peak_of_current_day":Active_power_peak_of_current_day,
        "Active_power":Active_power,
        "Device_status":Device_status,
        "Reactive_power":Reactive_power,
        "Power_factor":int(registers.get(32084)[5]["value"])/10,
        "Inverter_efficiency":int(registers.get(32086)[5]["value"])/100,
        "Cabinet_temperature":int(registers.get(32087)[5]["value"])/10,
        "vers": vers,
         "montly_energy": energy_yeild_current_month,
    }


    return sdata
