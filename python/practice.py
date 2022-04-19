import Tkinter as tk
m=tk.Tk()

m.title('harsh')
m.geometry('300x300')

while True:
	button=tk.Button(m,text='ledon',width=25,command=m.destroy)
	print('led on')

while True:
	button1=tk.Button(m,text='ledoff',width=25,command=m.destroy)
	print('led off')

button.pack()
button1.pack()

m.mainloop()
