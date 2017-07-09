import psutil
from pymongo import MongoClient
import datetime
import threading


client = MongoClient()
db = client.sysinfo

global timer


def get_sensor_temp():
    with open("/sys/class/hwmon/hwmon0/temp1_input") as temp1:
        return int(temp1.read())


def record_db():

    temp = get_sensor_temp()
    recorde_time = datetime.datetime.now()
    temp_data = {"temp": temp, "time": recorde_time}
    print(temp_data)
    db.temp.insert(temp_data)

    timer = threading.Timer(60, record_db)
    timer.start()


def main():
    timer = threading.Timer(60, record_db)
    timer.start()


if __name__ == "__main__":
    main()
