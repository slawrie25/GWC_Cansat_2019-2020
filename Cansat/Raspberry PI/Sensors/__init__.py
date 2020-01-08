import glob

sensor_list = []
excluded_files = [
	"__init__",
	"example",
	"cansat_sensor"
]

# Get all sensors in the Sensors directory and import them
for sensorFile in glob.glob("*.py"):
	# Remove the .py from the sensorFile
	sensorFile = sensorFile[:sensorFile.find(".py")]

	# Check if it is in the list of excluded files
	if sensorFile in excluded_files:
		continue

	# If not, import it
	sensor_list.append(__import__(sensorFile))