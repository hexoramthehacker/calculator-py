from tkinter import *

expression = ""

#-----------------functions-------------------------------
def press(num):
    global expression

    expression+=str(num)

    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = total
    except:
        equation.set("error")
        expression= ""  
def clear():
    global expression
    expression = ""
    equation.set("")
#--------------UI-------------------------------------------------------------#

window = Tk()
window.title("Calculator")

window.config(padx=10,pady=10,background="black")

equation = StringVar()

view = Entry(textvariable=equation)
view.grid(row=0,column=1,columnspan=3)



key_1 = Button(text="1",command=lambda:press(1))
key_1.grid(column=1,row=3)
    
key_2 = Button(text="2",command=lambda:press(2))
key_2.grid(column=2,row=3)

key_3 = Button(text="3",command=lambda:press(3))
key_3.grid(column=3,row=3)

key_4 = Button(text="4",command=lambda:press(4))
key_4.grid(column=1,row=4)

key_5 = Button(text="5",command=lambda:press(5))
key_5.grid(column=2,row=4)

key_6 = Button(text="6",command=lambda:press(6))
key_6.grid(column=3,row=4)

key_7 = Button(text="7",command=lambda:press(7))
key_7.grid(column=1,row=5)

key_8 = Button(text="8",command=lambda:press(8))
key_8.grid(column=2,row=5)

key_9 = Button(text='9',command=lambda:press(9))
key_9.grid(column=3,row=5)

key_0 = Button(text="0",command=lambda:press(0))
key_0.grid(column=2,row=6)

key_div = Button(text="/",command=lambda:press('/'))
key_div.grid(column=4,row=3)

key_add = Button(text="+",command=lambda:press('+'))
key_add.grid(column=4,row=4)

key_mul = Button(text="*",command=lambda:press("*"))
key_mul.grid(column=4,row=5)

key_sub = Button(text="-",command=lambda:press("-"))
key_sub.grid(column=4,row=6)


key_1eql = Button(text="=",command=equalpress)
key_1eql.grid(column=4,row=7)

window.mainloop()