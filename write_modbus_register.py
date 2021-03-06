#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

if len(sys.argv) <= 3:
   print("Usage: python3 script.py   ip   register  value")
   sys.exit(0)

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
  client.write_register(int(sys.argv[2]), int(sys.argv[3])) 
  print("Written")