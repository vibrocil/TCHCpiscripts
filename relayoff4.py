import time
import grovepi4
import sys
relay = int(sys.argv[1])
grovepi4.pinMode(relay,"OUTPUT")
grovepi4.digitalWrite(relay,0)
