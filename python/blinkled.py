import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

while True:
	GPIO.output(8,True)
	time.sleep(1)
	GPIO.output(8,False)
	time.sleep(1)
	GPIO.output(10,True)
	time.sleep(1)
	GPIO.output(10,False)
	time.sleep(1)
