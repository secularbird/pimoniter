import unittest2
import sysmonitor


class SysMonitorTestCase(unittest2.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGet_Cpu_Percent(self):
        sysmonitor.get_cpu_percent()

    def testGet_Sensor_Temp(self):
        sysmonitor.get_sensor_temp()

    def testGet_Local_Weather_Temp(self):
        sysmonitor.get_local_weather_temp()


if __name__ == "__main__":
    unittest2.main()