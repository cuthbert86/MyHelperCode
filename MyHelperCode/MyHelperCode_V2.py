import network
import usocket
import socket
from time import time, sleep
import network
import time
import machine
#from picozero import pico_temp_sensor
from machine import Pin
import micropython
import ustruct as struct
import json



Self_Name = "Cuthbert"
SSID = ''  # wifi username
PASSWORD = '' # wifi password
ssidRouter     = ''    #Enter the router name
passwordRouter = '' #Enter the router password
ssidAP         = 'Pico W'      #Enter the AP name
passwordAP     = '12345678'    #Enter the AP password
local_IP       = '192.168.4.150'
gateway        = '192.168.4.1'
subnet         = '255.255.255.0'
dns            = '8.8.8.8'

adcpin = 4
sensor = machine.ADC(adcpin)
sock = usocket
SERVER_HOSTNAME = ""

USER = ""
PASSWORD = ""
wlan = network.WLAN(network.STA_IF)
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)


def read_json_file(file_path):
    """
    Function for reading json file
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except:
        return None
    else:
        return data


def write_json_file(file_path, data):
    """
    Function for writing json file
    """
    try:
        with open(file_path, "w") as file:
            json.dump(data, file)
    except:
        return None
    else:
        return data


def GetTemperature():
    adc_value = sensor.read_u16()
    volt = (3.3/65535) * adc_value
    temperature = 27 - (volt - 0.706)/0.001721
    temp = str(round(temperature, 1))
#    timestamp = datetime.now().isoformat()
    print(temp)
    return temp


def connect_to_wifi():
    SSID = ''
    PASSWORD = ''
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
        print("Waiting for connection...")
    else:
        print("Wi-Fi connected!")
        print("IP address:", wlan.ifconfig())


def to_json(temperature):

    # Create a dictionary to hold the sensor data
    sensor_data = {
        "Self Name": Self_Name,
        "temperature": temperature,
    }

    # Convert the dictionary to a JSON string
    json_data = json.dumps(sensor_data)
    return json_data


def WifiServer(ssidAP,passwordAP):
    local_IP = '192.168.1.1'
    gateway = '192.168.1.10'
    subnet = '255.255.255.0'
    dns = '8.8.8.8'
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.ifconfig([local_IP,gateway,subnet,dns])
    print("Setting soft-AP  ... ")
    ap_if.config(essid=ssidAP, password=passwordAP)
    ap_if.active(True)
    print('Success, IP address:', ap_if.ifconfig())
    open_socket()
    print("Setup End\n")
    

def open_socket():
    # Open a socket
    ip = '192.168.1.10'
    address = (ip, 8080)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def STA_Setup(ssidRouter,passwordRouter):
    print("Setting soft-STA  ... ")
    if not sta_if.isconnected():
        print('connecting to',ssidRouter)
        sta_if.active(True)
        sta_if.connect(ssidRouter,passwordRouter)
        while not sta_if.isconnected():
            pass
    print('Connected, IP address:', sta_if.ifconfig())
    print("Setup End")


def AP_Setup(ssidAP,passwordAP):
    ap_if.ifconfig([local_IP,gateway,subnet,dns])
    print("Setting soft-AP  ... ")
    ap_if.config(essid=ssidAP, password=passwordAP)
    ap_if.active(True)
    print('Success, IP address:', ap_if.ifconfig())
    print("Setup End\n")


def collect_sensor_data():
    # Collect data from the sensor
    Temp = GetTemperature()
    
    # Get the current timestamp
    timestamp = time.time()
    
    # Format timestamp to YYYY-MM-DD HH:MM:SS
    formatted_time = time.localtime(timestamp)
    timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        formatted_time[0], formatted_time[1], formatted_time[2], 
        formatted_time[3], formatted_time[4], formatted_time[5]
    )

    # Create a CSV formatted string
    csv_data = "{},{}\n".format(timestamp_str, Temp)
    
    return csv_data


def timestamp():
    TimeStamp = time.localtime()
    return TimeStamp


def write_to_csv(csv_data, filename="file_Name.csv"):
    # Write the CSV data to a file
    with open(filename, "a") as file:
        file.write(csv_data)
        

# How to set up a deque and append data to it and calcvulate the rolling average.
from collections import deque

"""
Temperature = float(GetTemperature())
d = deque([], 10)
print(len(d))
d.append(Temperature)
d.append(Temperature)
print(len(d))
total = sum(d)
length = len(d)
print(total)
average = total / length
"""

def rolling_averagemean(example_deque):
    total = sum(example_deque)
    length = len(example_deque)
    aveMean = total / length
    
    return aveMean


    