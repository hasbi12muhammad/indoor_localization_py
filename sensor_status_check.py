import logging
from flask import Flask
from flask import request
from datetime import datetime
import csv

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Mac 1 untuk ESP32 pada Ruang 1
# Mac 2 untuk ESP32 pada Ruang 2

mac1, mac2, mac3, mac4, mac5 = "3C:71:BF:C4:E1:F4", "B4:E6:2D:B7:72:45","B4:E6:2D:B7:6B:91", "3C:71:BF:88:A0:B4", "B4:E6:2D:B3:57:E5"


#rssi[0] untuk Mac 1, rssi[1] untuk Mac 2, dst..
sensor = [None,None,None,None,None]

@app.route("/", methods=['POST'])
def main():
    try:
        data = request.get_json(force=True)
        if data['mac'] == mac1 and sensor[0] == None:
            sensor[0] = "Ok"
            print("Sensor 1 is Online")
        elif data['mac'] == mac2 and sensor[1] == None:
            sensor[1] = "Ok"
            print("Sensor 2 is Online")
        elif data['mac'] == mac3 and sensor[2] == None:
            sensor[2] = "Ok"
            print("Sensor 3 is Online")
        elif data['mac'] == mac4 and sensor[3] == None:
            sensor[3] = "Ok"
            print("Sensor 4 is Online")
        elif sensor[4] == None:
            sensor[4] = "Ok"
            print("Sensor 5 is Online")
        #print(data,datetime.now().time().replace(microsecond=0))
        return ""
    except Exception as e:
        return print('error', e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
