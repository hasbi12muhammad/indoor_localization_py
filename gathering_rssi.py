import logging
from flask import Flask
from flask import request
from datetime import datetime
import csv

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Mac 1 dan Mac 2 untuk ESP32 pada Ruang 1
# Mac 3 dan Mac 4 untuk ESP32 pada Ruang 2
# Mac 5 dan Mac 6 untuk ESP32 pada Ruang 3

mac1, mac2, mac3, mac4, mac5 = "3C:71:BF:C4:E1:F4", "B4:E6:2D:B7:72:45","B4:E6:2D:B7:6B:91", "3C:71:BF:88:A0:B4", "B4:E6:2D:B3:57:E5"

# rssi[0] untuk Mac 1, rssi[1] untuk Mac 2
rssi = [None, None, None, None, None]


@app.route("/", methods=['POST'])
def main():
    try:
        data = request.get_json(force=True)
        global rssi
        if data['mac'] == mac1:
            rssi[0] = data['rssi']
        elif data['mac'] == mac2:
            rssi[1] = data['rssi']
        elif data['mac'] == mac3:
            rssi[2] = data['rssi']
        elif data['mac'] == mac4:
            rssi[3] = data['rssi']
        else:
            rssi[4] = data['rssi']
        if any(x is None for x in rssi):
            print("Waiting Another Rssi...")
        else:
            nTemp = -120
            bEqual = True

            for item in rssi:
                if nTemp != item:
                    bEqual = False
                    break

            if bEqual:
                print("All rssi valued -120")
            else:
                new_row = ['Ruang 2', datetime.now().time().replace(
                    microsecond=0), rssi[0], rssi[1], rssi[2], rssi[3], rssi[4]]

                with open('rssi_collected.csv', 'a', newline='') as csv_file:
                    writer = csv.writer(
                        csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(new_row)

                csv_file.close()
                print("1 row inserted")
                rssi = [None, None, None, None, None]
        return ""
    except Exception as e:
        return print('error', e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
