# The cansat_sensor class for creating an interface for the main code
import cansat_sensor

#For interfacing with the Arduino
import serial

#Raspberry Pi serial port
port = "/dev/ttyS0"

#Setup uart connection
uart = serial.Serial(port)

# Extend the sensor class
class Arduino(cansat_sensor.Sensor):
    def data(self):
        return uart.readline()

# Actually create the sensor object
sensor = Arduino("Arduino", "A")