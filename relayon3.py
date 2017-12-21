import time
import grovepi3
import sys
relay = int(sys.argv[1])
grovepi3.pinMode(relay,"OUTPUT")
grovepi3.digitalWrite(relay,1)
