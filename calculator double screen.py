from tkinter import *
cal = Tk()
disp1=Entry(cal,bd=15,justify='right',font=('Calibri','35'),insertwidth=3,width=30)
disp1.grid(row=0,column=0,columnspan=4)
disp2=Entry(cal,bd=6,justify='right',font=('Calibri','20'),width=20)
disp2.grid(row=1,column=0,columnspan=4)

keys =["7","8","9","+","4","5","6","-","1","2","3","*","0","**",".","/","(",")","CE","="]
btn =[]

def func(i):
    if keys[i]=="=":
        s=str(eval(disp1.get()))
        disp2.delete(0,END)
        disp2.insert(END,s)
    elif keys[i]=="CE":
        disp1.delete(0,END)
        disp2.delete(0,END)
    else: disp1.insert(END,keys[i])
 
for i in range(len(keys)):
        btn.append(Button(cal,bd=8,text=keys[i],font=('Calibri','18'), command=lambda 
i=i:func(i)).grid(row=2+i//4,column=i%4,ipadx=30)) 
cal.mainloop()
