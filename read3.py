import grovepi3
import sys
sensor = int(sys.argv[1])
grovepi3.pinMode(sensor,"INPUT")
try:
	sensor_value = grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
	sensor_value += grovepi3.analogRead(sensor)
except IOError:
	pass
if sensor_value<10:
        print 1
elif sensor_value==255:
        print 1
elif sensor_value==256:
        print 1
elif sensor_value==258:
        print 1
elif sensor_value==1:
        print 1
else:
        print 2

