import minimalmodbus as mb
instrument = mb.Instrument('/dev/ttyUSB1', 1)
instrument.serial.baudrate = 9600  # Baud
instrument.serial.bytesize = 8
instrument.serial.stopbits = 1
instrument.serial.timeout = 2  # seconds
instrument.address = 1   # this is the slave address number
instrument.mode = mb.MODE_RTU   #
value =  instrument.read_registers(32118, 2,3)
print(value)

def return_int_value(a, b):
    a = hex(int(a))
    b = hex(int(b))
    if a == 0:
        hex_a = b[2:]
    else:
        hex_a = a + b[2:]
    return (int(hex_a, 0))

print(return_int_value(value[0],value[1]))