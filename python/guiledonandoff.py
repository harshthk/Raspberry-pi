import Tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO8 = 8
GPIO10 = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO8,GPIO.OUT)
GPIO.setup(GPIO10,GPIO.OUT)

m=tk.Tk()
m.geometry("300x300")
m.wm_title("led on an off")

GPIO8_state = True
GPIO10_state = True

def GPIO8button():
	global GPIO8_state
	if GPIO8_state == True:
		GPIO.output(GPIO8,GPIO8_state)
		GPIO8_state = False
		ONlabel = tk.label(m,text="turned on",fg="green")
		ONlabel = grid(row=0, column=1)
	else:
		GPIO.output(GPIO8, GPIO8_state)
		GPIO8_state = True
		ONlabel = tk.label(m, text="turned off",fg="red") 
		ONlabel.grid(row=0,column=1)
def GPIO10button():
	global GPIO10_state
	if GPIO10_state == True:
		GPIO.output(GPIO10,GPIO10_state)
		GPIO10_state = False
		OFFlabel = tk.label(m,text="turned on",fg="green")
		OFFlabel.grid(row=1,Column=1)
	else:
		GPIO.output(GPIO10,GPIO10_state)
		GPIO10_state = True
		OFFlabel = tk.label(m,text="turned off",fg="red")
		OFFlabel.grid(row=1,column=1)
ONbutton=tk.Button(m,text='red led',bg='blue',command=GPIO8button)
ONbutton.grid(row=0,column=0)

OFFbutton=tk.Button(m,text='green led',bg='blue',command=GPIO10button)
OFFbutton.grid(row=1,column=0)	
m.mainloop()
