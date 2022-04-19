import RPi.GPIO as GPIO
import blynklib
BLYNK_AUTH = '0a2e93ac0c534d038e95e38a1c0f638c'
blynk=blynklib.Blynk(BLYNK_AUTH)
GPIO.setmode(GPIO.BOARD)
led=8
GPIO.setup(led,GPIO.OUT)
@blynk.handle_event('write V1')
def read__handler(pin, value):
   print(value)
   if value==[u'1']:
      GPIO.output(led,GPIO.HIGH)
      print('on')
   elif  value ==[u'0']:
       GPIO.output(led,GPIO.LOW)
       print('off')
while 1:
   blynk.run()
