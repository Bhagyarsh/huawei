import csv



def setData(uid, slave_id, registers, timesend, vers):

    a = registers.get(32064)[5]["value"]
    b = registers.get(32065)[5]["value"]
    total_power = a + b

    a = registers.get(32078)[5]["value"]
    b = registers.get(32078)[5]["value"]
    Active_power_peak_of_current_day = a+b

    a = registers.get(32080)[5]["value"]
    b = registers.get(32081)[5]["value"]
    Active_power = a + b

    a = registers.get(32082)[5]["value"]
    b = registers.get(32083)[5]["value"]
    Reactive_power = a+b

    a = registers.get(32089)[5]["value"]
    b = registers.get(32089)[5]["value"]
    Device_status = a+b

    a = registers.get(32106)[5]["value"]
    b = registers.get(32107)[5]["value"]
    totlal_energy_yeild = a+b

    a = registers.get(32114)[5]["value"]
    b = registers.get(32115)[5]["value"]
    daily_energy = a+b

    a = registers.get(32118)[5]["value"]
    b = registers.get(32119)[5]["value"]
    energy_yeild_current_year = a+b

    a = registers.get(32116)[5]["value"]
    b = registers.get(32117)[5]["value"]
    energy_yeild_current_month = a+b

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
            "Active_power_peak_of_current_day":Active_power_peak_of_current_day,
            "Active_power":Active_power,
            "Device_status":Device_status,
            "Reactive_power":Reactive_power,
            "Power_factor":int(registers.get(32084)[5]["value"]),
            "Inverter_efficiency":int(registers.get(32086)[5]["value"]),
            "Cabinet_temperature":int(registers.get(32087)[5]["value"]),
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
            "pv1_current",
            "pv2_current",
            "pv3_current",
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
    print(data)

    with open(file_name, 'a') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, fieldnames)
        w.writerow(data)


def setCsvData(uid, slave_id, registers, timesend, vers):
    a = registers.get(32064)[5]["value"]
    b = registers.get(32065)[5]["value"]
    total_power = a + b

    a = registers.get(32078)[5]["value"]
    b = registers.get(32078)[5]["value"]
    Active_power_peak_of_current_day = a+b

    a = registers.get(32080)[5]["value"]
    b = registers.get(32081)[5]["value"]
    Active_power = a + b

    a = registers.get(32082)[5]["value"]
    b = registers.get(32083)[5]["value"]
    Reactive_power = a+b

    a = registers.get(32089)[5]["value"]
    b = registers.get(32089)[5]["value"]
    Device_status = a+b

    a = registers.get(32106)[5]["value"]
    b = registers.get(32107)[5]["value"]
    totlal_energy_yeild = a+b

    a = registers.get(32114)[5]["value"]
    b = registers.get(32115)[5]["value"]
    daily_energy = a+b

    a = registers.get(32118)[5]["value"]
    b = registers.get(32119)[5]["value"]
    energy_yeild_current_year = a+b

    a = registers.get(32116)[5]["value"]
    b = registers.get(32117)[5]["value"]
    energy_yeild_current_month = a+b

    sdata = {
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
        "offline": 1,
        "recordedAt": timesend,
        "Active_power_peak_of_current_day":Active_power_peak_of_current_day,
        "Active_power":Active_power,
        "Device_status":Device_status,
        "Reactive_power":Reactive_power,
        "Power_factor":int(registers.get(32084)[5]["value"]),
        "Inverter_efficiency":int(registers.get(32086)[5]["value"]),
        "Inverter_efficiency":int(registers.get(32086)[5]["value"]),
        "vers": vers
    }


    return sdata
