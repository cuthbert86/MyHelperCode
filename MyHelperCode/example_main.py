from MyHelperCode import GetTemperature, connect_to_wifi, WifiServer, to_json, collect_sensor_data, timestamp, write_to_csv, rolling_averagemean
import usocket
import socket
from time import time, sleep
import network
import time
import machine
from machine import Pin
import micropython
import ustruct as struct
import json
import random
import socket
from collections import deque



Self_Name = "Cuthbert"
Timestamp = timestamp()
print("timestamp", Timestamp)

Temperature = GetTemperature()
print("temperature", Temperature)

json_string = {"name":Self_Name,
                "temp":Temperature,
                "Timestamp":Timestamp,
               }
print("json_string", json_string)

csv_data = collect_sensor_data()
print("csv_data", csv_data)
write_to_csv(csv_data)

ip = connect_to_wifi()

Temperature = float(GetTemperature())
example_deque = deque([], 10)
example_deque.append(Temperature)
total = sum(example_deque)
length = len(example_deque)
average = rolling_averagemean(example_deque)
print(average)





