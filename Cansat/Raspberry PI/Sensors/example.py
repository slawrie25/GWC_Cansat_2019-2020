import cansat_sensor

class Example(cansat_sensor.Sensor):
    def data(self):
        return "AHDJHFD", self.name, self.id

sensor = Example("ABCD", "A")
print(sensor.data())