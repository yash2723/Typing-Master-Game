def sliding_word():
    global count,temp
    heading = " Welcome in Typing Master Game "
    if count >= len(heading):
        count = 0
        temp = ''
    temp = temp + heading[count]
    count = count + 1
    title_label['text'] = temp
    title_label.after( 150 , sliding_word)

def Clicked():
    if lan.get() == '' :
        messagebox.showinfo("Notification" , "Please First of all Select the anyone Language")
    
    else :
        # print(lan.get())    
        root.destroy()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Typing Master")
root.geometry('600x300')

count = 0
temp = ''
title_label = Label(root , text = " " , font = "Arial 25 bold" , fg = "white" , bg = "red" , width = 30 , bd = 10)
title_label.place(x=0 , y=10)
sliding_word()
title_label.configure()

name = StringVar()
color = StringVar()
lan = StringVar()

name_label = Label(root , text = "Name : ")
name_label.place(x=200 , y=98)

name_value = Entry(root , textvariable = name)
name_value.place(x=250 , y=100)

color_label = Label(root , text = "Theme : ")
color_label.place(x=200 , y=148)

color_value = Entry(root , textvariable = color)
color_value.place(x=250 , y=150)

lan_label = Label(root , text = "Language : ")
lan_label.place(x=200 , y=190)

lan_value = Radiobutton(root , text = "C" , variable = lan , value = "c")
lan_value.place(x=270 , y=190)

lan_value = Radiobutton(root , text = "C++" , variable = lan , value = "cpp")
lan_value.place(x=310 , y=190)

lan_value = Radiobutton(root , text = "Java" , variable = lan , value = "java")
lan_value.place(x=365 , y=190)

lan_value = Radiobutton(root , text = "Python" , variable = lan , value = "python")
lan_value.place(x=420 , y=190)

lan_value = Radiobutton(root , text = "Java Script" , variable = lan , value = "js")
lan_value.place(x=490 , y=190)

btn = Button(root , text = "Submit" , command = Clicked)
btn.place(x=280 , y=230)

root.mainloop()


################################################################################################################################################
def sliding_word():
    global count,temp
    heading = " Welcome in Typing Master Game "
    if count >= len(heading):
        count = 0
        temp = ''
    temp = temp + heading[count]
    count = count + 1
    title_label['text'] = temp
    title_label.after( 150 , sliding_word)
    
def startgame(event):
    global score,wrong,ra
    if score == -10:
        timer()
    if ip.get() == target_label['text'] :
        score = score + 10
        score_value['text'] = score
        ip.set('')
        if ra == (len(words) - 1) :
            messagebox.showinfo("Result" , "Time : " + str(time) + "s" + "  Attemting Words : " + str(score/10) + "\n" + "Right Words : " + str((score/10)-wrong) + "\n" + "Wrong Words : " + str(wrong))
            root.destroy()
        else :
            ra = ra + 1
        target_label['text'] = words[ra]
        instruction_label['text'] = ''
        bottom_label['text'] = "Word is Matched"
    
    else :
        ip.set('')
        wrong = wrong + 1
        bottom_label['text'] = "Word is not Matched"

def timer():
    global time
    # if time == 0:
    #     messagebox.showinfo('Result' ,"Attemting Words : " + str(score/10) + "\n" + "Right Words : " + str((score/10)-wrong) + "\n" + "Wrong Words : " + str(wrong))
    #     root.destroy()
    time = time + 1
    time_value['text'] = time
    time_value.after(1000 , timer)

from tkinter import *
import random
from tkinter import messagebox
import pygame

root = Tk()
pygame.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(loops = 10)

################################################################### Main Window

root.title("Typing Master")
root.geometry("600x500")
root.resizable(False,False)
root.configure(background = "black")

################################################################### Variables

count = 0
temp = ''
ip = StringVar()
score = -10
time = 0
words = ['Apple' , 'Mango' , 'Grapes' , 'Car' , 'Vagitable' , 'Maths' , 'Science' , 'Lenovo' , 'Nokia' , 'Google' , 'Dell' , 'Hp' , 'Onion' , 'Book' , 'Google Chrome' , 'Social Science' , 'Python' , 'Java' , 'Java Script' , 'Languages' , 'MongoDB' , 'SQL' , 'Samsung' , 'Ramesh' , 'Mahesh' , 'Whatsapp' , 'Facebook' , 'Instagram' ]

if lan.get() == 'c':
    words = ['C' , 'auto' , 'const' , 'double' , 'float' , 'int' , 'short' , 'struct' , 'unsigned' , 'break' , 'continue' , 'else' , 'for' , 'long' , 'signed' , 'switch' , 'void' , 'case' , 'default' , 'enum' , 'goto' , 'register' , 'sizeof' , 'typedef' , 'volatile' , 'char' , 'do' , 'extern' , 'if' , 'return' , 'static' , 'union' , 'while' , 'printf' , 'scanf']

elif lan.get() == 'cpp':
    words = ['CPP' , 'auto' , 'asm' , 'bool' , 'break' , 'case' , 'catch' , 'char' , 'class' , 'const' , 'continue' , 'default' , 'delete' , 'do' , 'double' , 'else' , 'enum' , 'explicit' , 'export' , 'extern' , 'false' , 'float' , 'for' , 'friend' , 'goto' , 'if' , 'inline' , 'int' , 'long' , 'mutable' , 'namespace' , 'new' , 'operator' , 'private' , 'protected' , 'public' , 'register' , 'return' , 'short' , 'signed' , 'sizeof' , 'static' , 'struct' , 'switch' , 'template' , 'this' , 'throw' , 'true' , 'try' , 'typedef' , 'typeid' , 'typename' , 'union' , 'unsigned' , 'using' , 'virtual' , 'void' , 'volatile' , 'while']

elif lan.get() == 'java':
    words = ['Java' , 'auto' , 'asm' , 'bool' , 'break' , 'case' , 'catch' , 'char' , 'class' , 'const' , 'continue' , 'default' , 'delete' , 'do' , 'double' , 'else' , 'enum' , 'explicit' , 'export' , 'extern' , 'false' , 'float' , 'for' , 'friend' , 'goto' , 'if' , 'inline' , 'int' , 'long' , 'mutable' , 'namespace' , 'new' , 'operator' , 'private' , 'protected' , 'public' , 'register' , 'return' , 'short' , 'signed' , 'sizeof' , 'static' , 'struct' , 'switch' , 'template' , 'this' , 'throw' , 'true' , 'try' , 'typedef' , 'typeid' , 'typename' , 'union' , 'unsigned' , 'using' , 'virtual' , 'void' , 'volatile' , 'while']

elif lan.get() == 'python':
    words = ['Python' , 'auto' , 'asm' , 'bool' , 'break' , 'case' , 'catch' , 'char' , 'class' , 'const' , 'continue' , 'default' , 'delete' , 'do' , 'double' , 'else' , 'enum' , 'explicit' , 'export' , 'extern' , 'false' , 'float' , 'for' , 'friend' , 'goto' , 'if' , 'inline' , 'int' , 'long' , 'mutable' , 'namespace' , 'new' , 'operator' , 'private' , 'protected' , 'public' , 'register' , 'return' , 'short' , 'signed' , 'sizeof' , 'static' , 'struct' , 'switch' , 'template' , 'this' , 'throw' , 'true' , 'try' , 'typedef' , 'typeid' , 'typename' , 'union' , 'unsigned' , 'using' , 'virtual' , 'void' , 'volatile' , 'while']

elif lan.get() == 'js':
    words = ['JavaScript' , 'auto' , 'asm' , 'bool' , 'break' , 'case' , 'catch' , 'char' , 'class' , 'const' , 'continue' , 'default' , 'delete' , 'do' , 'double' , 'else' , 'enum' , 'explicit' , 'export' , 'extern' , 'false' , 'float' , 'for' , 'friend' , 'goto' , 'if' , 'inline' , 'int' , 'long' , 'mutable' , 'namespace' , 'new' , 'operator' , 'private' , 'protected' , 'public' , 'register' , 'return' , 'short' , 'signed' , 'sizeof' , 'static' , 'struct' , 'switch' , 'template' , 'this' , 'throw' , 'true' , 'try' , 'typedef' , 'typeid' , 'typename' , 'union' , 'unsigned' , 'using' , 'virtual' , 'void' , 'volatile' , 'while']

wrong = 0
ra = -1

################################################################### Widgets ( Labels )

title_label = Label(root , text = " " , font = "Arial 25 bold" , fg = "white" , bg = "red" , width = 30 , bd = 10)
title_label.place(x=0 , y=10)
sliding_word()
title_label.configure()

score_label = Label(root , text = "Score : " , font = "Arial 25 bold" , fg = "white" , bg = "black")
score_label.place(x=10 , y=100)

score_value = Label(root , text = '' , font = "Arial 25 bold" , fg = "white" , bg = "black")
score_value.place(x=130 , y=103)

time_label = Label(root , text = "Time : " , font = "Arial 25 bold" , fg = "white" , bg = "black")
time_label.place(x=420 , y=100)

time_value = Label(root , text = time , font = "Arial 25 bold" , fg = "white" , bg = "black")
time_value.place(x=530 , y=100)

target_label = Label(root , text = "" , font = "Arial 25 bold" , bg = "black" , fg = "white")
target_label.place(x=180 , y=190)

inp_label = Entry(root , textvariable = ip , font = "Arial 15 bold" , fg = "white" , bg = "purple" , justify = "center" , bd = 10 , width = 25) 
inp_label.place(x=160 , y=250)
inp_label.focus()

instruction_label = Label(root , text = " Press 'Enter' For Start the Game " , bg = "light grey" , fg = "purple" , font = "Arial 20 bold")
instruction_label.place(x=90 , y=330)

bottom_frame = Frame(root , bg = "blue" , bd = 15 , width = 600 , height = 70 , relief = RAISED)
bottom_frame.place(x=0 , y=430)

bottom_label = Label(bottom_frame , text = "Status Bar" , fg = "black" , bg = "white" , font = "Arial 20 bold")
bottom_label.place(x=180 , y=0)

root.bind('<Return>' , startgame)


root.mainloop()