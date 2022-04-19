import Tkinter as tk
import RPi.GPIO as GPIO
import time

m=tk.Tk()
m.geometry("300x300")
m.wm_title("led on an off")

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

#while True:
	button=tk.Button(m,text='led on',command=m.destroy)
	#GPIO.output(8,True)
	#time.sleep(1)
#while True:
	button1=tk.Button(m,text='led off')
	#GPIO.output(10,True)
	#time.sleep(1)
button.pack()
button1.pack()
m.mainloop()
