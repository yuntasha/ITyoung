import os

os.system("ipconfig,-all")

import socket

in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)

import requests
import re
req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)[1]
print(out_addr)