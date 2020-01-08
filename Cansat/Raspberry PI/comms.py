# For interfacing with the RFM96w
import adafruit_rfm9x
import digitalio
import board
import busio
import datetime

# Setup connection
RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Open a file
backup = open("DATA - " + str(datetime.datetime.utcnow()), "w+")

def send(data):
	print(data)
	backup.write(data + "\n")
	rfm9x.send(bytes(data,"UTF-8"))
