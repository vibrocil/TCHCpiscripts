import time
import grovepi6
import sys
relay = int(sys.argv[1])
grovepi6.pinMode(relay,"OUTPUT")
grovepi6.digitalWrite(relay,1)
