import pigpio
import pynmea2
import cansat_sensor

class gps(cansat_sensor.Sensor):
	self.pi = pigpio.pi()

	self.rx = 23
	self.baud = 9600
	self.bits = 8

	self.pi.set_mode(rx, pigpio.INPUT)

	self.pigpio.exceptions = False
	self.pi.bb_serial_read_close(rx)
	self.pigpio.exceptions = True

	self.pi.bb_serial_read_open(rx, baud, bits)


	def data():
		data = ""
		while True:
			(count, char)= pi.bb_serial_read(rx)
			for i in range(count):
				if chr(char[i]) == "\n":
					return([data.replace("\r", "")])
				data += chr(char[i])

sensor = gps("GPS", "G")