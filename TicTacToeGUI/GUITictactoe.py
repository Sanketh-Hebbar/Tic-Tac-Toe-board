from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
root = Tk()
root.resizable(False,False)

root.title('TIC TAC TOE')
root.iconbitmap('Alex-T-Minimal-Fruit-Watermelon.ico')
#root.geometry("240x280")
player = 1
count = 0

def disable_buttons():
    but1.config(state=DISABLED)
    but2.config(state=DISABLED)
    but3.config(state=DISABLED)
    but4.config(state=DISABLED)
    but5.config(state=DISABLED)
    but6.config(state=DISABLED)
    but7.config(state=DISABLED)
    but8.config(state=DISABLED)
    but9.config(state=DISABLED)

    
 
 
def wincheck():
    if but1["text"]=='X' and but2["text"]=='X'and but3["text"]=='X'or but4["text"]=='X' and but5["text"]=='X'and but6["text"]=='X'or but7["text"]=='X' and but8["text"]=='X'and but9["text"]=='X'or but1["text"]=='X' and but4["text"]=='X'and but7["text"]=='X'or but2["text"]=='X' and but5["text"]=='X'and but8["text"]=='X'or but3["text"]=='X' and but6["text"]=='X'and but9["text"]=='X'or but1["text"]=='X' and but5["text"]=='X'and but9["text"]=='X'or but3["text"]=='X' and but5["text"]=='X'and but7["text"]=='X':
        messagebox.showinfo("Congrats", "X wins")
        disable_buttons()
    elif but1["text"]=='O' and but2["text"]=='O'and but3["text"]=='O'or but4["text"]=='O' and but5["text"]=='O'and but6["text"]=='O'or but7["text"]=='O' and but8["text"]=='O'and but9["text"]=='O'or but1["text"]=='O' and but4["text"]=='O'and but7["text"]=='O'or but2["text"]=='O' and but5["text"]=='O'and but8["text"]=='O'or but3["text"]=='O' and but6["text"]=='O'and but9["text"]=='O'or but1["text"]=='O' and but5["text"]=='O'and but9["text"]=='O'or but3["text"]=='O' and but5["text"]=='O'and but7["text"]=='O':
        messagebox.showinfo("Congrats", "O wins")
        disable_buttons()
    elif count==9:
        messagebox.showinfo("oops...", "IT'S A TIE!!")
        disable_buttons()
        
        
#button click
def clicked(b):
    global player,count

    
    if b["text"]==" " and player==1:
        b["text"]="X"
        player=0
        count += 1
        wincheck()
    elif b["text"]==" " and player==0:
        b["text"]="O"
        player=1
        count += 1
        wincheck()
    else:
        messagebox.showerror("Error", "Already clicked")
        
#Lambda for passing anything into function



def reset():
    global but1,but2,but3,but4,but5,but6,but7,but8,but9,clicked,count
    count=0
    

    but1 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but1))
    but1.grid(row=1,column=0)

    but2 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but2))
    but2.grid(row=1,column=1)

    but3 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but3))
    but3.grid(row=1,column=2)

    but4 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but4))
    but4.grid(row=2,column=0)

    but5 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but5))
    but5.grid(row=2,column=1)

    but6 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but6))
    but6.grid(row=2,column=2)

    but7 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but7))
    but7.grid(row=3,column=0)

    but8 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but8))
    but8.grid(row=3,column=1)

    but9 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but9))
    but9.grid(row=3,column=2)
    
    
    
reset_btn = PhotoImage(file='reset.png')  
    
resetbutton = Button(root,image=reset_btn,borderwidth=0,command=reset).grid(row=0,column=1)


but1 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but1))
but1.grid(row=1,column=0)

but2 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but2))
but2.grid(row=1,column=1)

but3 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but3))
but3.grid(row=1,column=2)

but4 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but4))
but4.grid(row=2,column=0)

but5 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but5))
but5.grid(row=2,column=1)

but6 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but6))
but6.grid(row=2,column=2)

but7 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but7))
but7.grid(row=3,column=0)

but8 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but8))
but8.grid(row=3,column=1)

but9 = Button(root,text =" ",height=6 , width=12,fg='black',bg='#D2ACFC',font=('Comic Sans MS',17),command=lambda:clicked(but9))
but9.grid(row=3,column=2)
    




        


root.mainloop()
