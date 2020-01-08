# Import needed modules
import os
import sys
import glob
import threading
import time

# Import module for communications
import comms

# The sensors
import sensors

# The packet buffer
packetBuffer = []
	
# Get the sensors
sensors = sensors.sensor_list

# Sensor thread worker
def worker(sensor):
	while True:
		# Get data from sensor
		data = sensor.sensor.data()
		
		# Pack the data with struct
		packet = str(sensor.sensor.id) + "," + str(time.time()) + "," + str(data)
		
		# Put the packed data into a buffer for sending
		packetBuffer.append(packet)

# Loop through the sensors and create a thread for each
threads = []
for sensor in sensors:
	# Create the thread and give it a sensor as an argument
	thread = threading.Thread(target=worker, args=(sensor,))
	
	# Make it a daemon so it dies on ctrl+c
	thread.daemon = True
	
	# Put it in the list of threads
	threads.append(thread)
	
	# Start the thread
	thread.start()

# Send data to base-station
while True:
	try:
		data = packetBuffer.pop(0)
		comms.send(data)
	except:
		time.sleep(0.1)
