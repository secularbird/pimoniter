import psutil
from pymongo import MongoClient
import datetime
import threading
import requests
import json

client = MongoClient()
db = client.sysinfo

global timer


def get_sensor_temp():
    with open("/sys/class/hwmon/hwmon0/temp1_input") as temp1:
        return int(temp1.read())


def get_local_weather_temp():
    '''get local weather temp which using amap api'''
    weatherapi = "http://restapi.amap.com/v3/weather/weatherInfo?key=bb46dc7c8cfb9f2b89b46f26c0b41e7f&city=310104&extensions=base"
    req = requests.get(weatherapi)
    j = json.loads(req.text)
    if j["info"] == "OK":
        return j["lives"][0]["temperature"]
    else:
        return 0


def get_cpu_percent():
    return psutil.cpu_percent(interval=None)


def record_db():

    temp = get_sensor_temp()
    weather_temp = get_local_weather_temp()
    record_time = datetime.datetime.now()
    cpu_percent = get_cpu_percent()
    temp_data = {"temp": temp, "weather_temp": weather_temp, "cpu_percent": cpu_percent, "time": record_time}
    print(temp_data)
    db.temp.insert(temp_data)

    timer = threading.Timer(60, record_db)
    timer.start()


def main():
    timer = threading.Timer(60, record_db)
    timer.start()


if __name__ == "__main__":
    main()
