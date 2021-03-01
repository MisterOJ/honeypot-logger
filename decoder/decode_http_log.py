#!/usr/bin/env python3

import json
import subprocess
import select
import sh
import os


logFileName = os.getenv("LOG_FILE")
decodedLogFileName = os.getenv("DECODED_LOG_FILE")

f = subprocess.Popen(['tail','-F',logFileName],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(1):
        try:
            line = f.stdout.readline()
            jsonObject = json.loads(line)
            encodedData = jsonObject["data"]
            decodedData = bytearray.fromhex(encodedData).decode()
            if len(decodedData) > 2000:
                continue
            jsonObject["data"] = decodedData
            stringObject = json.dumps(jsonObject)
            with open(decodedLogFileName, "a") as http_decoded:
                http_decoded.write(stringObject)
                http_decoded.write("\n")
                http_decoded.close()
        except:
            continue