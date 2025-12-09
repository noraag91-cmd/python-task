from tkinter import *
root=Tk()
root.geometry('400x500')
root.title('home')
def fun():
    name=txt.get('1.0','end')
    lbl['text']=name
btn=Button(root,command=fun,text='click me',width='12',height='3',fg='white',bg='black',font='25')
btn.pack()
lbl=Label(root,width='25',height='10',fg='white',bg='black',font='25')
txt=Text(root,width='25',height='13')
txt.pack()
lbl.pack()

root.mainloop()