from tkinter import *
import cv2

cal = Tk()
cal.title("TEZT APP 1")
opretor = ""

text_Input =StringVar ()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default')

textdislpay = Entry(cal,font=('arial',50,'bold'), textvariable="Choose They Way To know More About It:-", bd=25, insertwidth=4, bg="cyan") .grid(columnspan=10)

btn1=Button(cal,padx=10,bd=10,fg='black',font=('arial', 25,'bold'),text="Wear Mask Whenever You Go Out Side...") .grid(row=1,column=0)

btn2=Button(cal,padx=10,bd=10, fg='black',font=('arial', 25,'bold'),text="Wear Mask Whenever You Go Out Side...") .grid(row=2,column=0)

btn3=Button(cal,padx=10,bd=10, fg='black',font=('arial', 25,'bold'),text="Wear Mask Whenever You Go Out Side...") .grid(row=3,column=0)

btn4=Button(cal,padx=10,bd=10, fg='black',font=('arial', 25,'bold'),text="Wear Mask Whenever You Go Out Side...") .grid(row=4,column=0)

btn5=Button(cal,padx=10,bd=10, fg='black',font=('arial', 25,'bold'),text="Wear Mask Whenever You Go Out Side...") .grid(row=5,column=0)

btn = Button(cal, bg="red",text = 'Close', bd = '5',
                          command = cal.destroy) .grid(row=0,column=10)

cal.mainloop()