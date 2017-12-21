import time
import grovepi5
import sys
relay = int(sys.argv[1])
grovepi5.pinMode(relay,"OUTPUT")
grovepi5.digitalWrite(relay,1)
