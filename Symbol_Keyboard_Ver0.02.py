import tkinter as tk
from tkinter import ttk, Frame, filedialog, font
from tkinter import *
import pyperclip as pc


root = tk.Tk()

root.title('OnScreen Charactor Keyboard JH APPs')


root.geometry('1200x800')

frm1 = ttk.Frame(root, height=20, width=100)
frm1.grid(row=0, column=1, columnspan=2)
##frm1.columnconfigure(0, weight=0)
##frm1.columnconfigure(1, weight=0)
frm4 = ttk.Frame(root,height=10, width=100)
frm4.grid(row=2, column=0)
frm2 = ttk.Frame(root, height=800, width=1000)
frm2.grid(row=4, column=0, columnspan=10, rowspan=3)
frm2.columnconfigure(0, weight=2)
frm2.columnconfigure(1, weight=2)

frm3 = ttk.Frame(root, height=300, width=180)
frm3.grid(row=10, column=0, columnspan=3)

frm3.columnconfigure(0, weight=10)
frm3.columnconfigure(1, weight=10)


text=tk.Text(frm1, height=5, font=('Arial', 12, 'bold'), bd=20, bg='seashell')
text.grid(row=0, column=1, pady=20, sticky='e')


def clear():
  text.delete(1.0, tk.END)


def cut():
  pypc = text.get(1.0, tk.END)
  pc.copy(pypc)
  text.delete(1.0, tk.END)
   
 

def copy():
    pypc = text.get(1.0, tk.END)
    pc.copy(pypc)
 

def paste():
  pc.paste()
 

 


  
def save(event=None):
    
    file_name = tk.filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'),('Text Documents', '*.txt')])
    
        
    def write_to_file(file_name):
        
        try:

            content = text.get(1.0, 'end')

            with open(file_name, 'w') as the_file:

                the_file.write(content)

        except IOError:

            pass
    write_to_file(file_name)





    

menubar = tk.Menu(root)
menubar.add_command(label='Save', command=save)
menubar.add_command(label='Cut', command=cut)
menubar.add_command(label='Copy', command=copy)
menubar.add_command(label='Paste', command=paste)
menubar.add_command(label='Clear', command=clear)
##menubar.add_command(label='', command=None)
##menubar.add_command(label='3', command=None)
##menubar.add_command(label='4', command=None)
##menubar.add_command(label='5', command=None)
root.config(menu=menubar)
 
 

 	
 	
	

def char1():
    ur = '\u0394'
    text.insert(tk.END, ur)
    return ur

def char2():
    ur = '\u03C0'  
    text.insert(tk.END, ur)
    return ur

def char3():
    ur = '\u03BB'
    text.insert(tk.END, ur)
    return ur

def char4():
    ur = '\u03F4'
    text.insert(tk.END, ur)
    return ur

def char5():
    ur = '\u03B8' 
    text.insert(tk.END, ur)
    return ur

def char6():
    ur = '\u03B1' 
    text.insert(tk.END, ur)
    return ur

def char7():
    ur = '\u03B2' 
    text.insert(tk.END, ur)
    return ur


def char8():
    ur = '\u03B3' 
    text.insert(tk.END, ur)
    return ur


def char9():

    ur = '\u03B4' 
    text.insert(tk.END, ur)
    return ur


def char10():
    ur = '\u03B5' 
    text.insert(tk.END, ur)
    return ur


def char11():
    ur = '\u03B6' 
    text.insert(tk.END, ur)
    return ur




def char12():
    ur = '\u03B7' 
    text.insert(tk.END, ur)
    return ur
def char13():
    ur = '\u2116' 
    text.insert(tk.END, ur)
    return ur
def char14():
    ur = '\u2126' 
    text.insert(tk.END, ur)
    return ur
  
def char15():
    ur = '\u2122' 
    text.insert(tk.END, ur)
    return ur
def char16():
    ur = '\u222B' 
    text.insert(tk.END, ur)
    return ur

def char17():
    ur = '\u222C' 
    text.insert(tk.END, ur)
    return ur

def char18():
    ur = '\u222D' 
    text.insert(tk.END, ur)
    return ur



def char19():
    ur = '\u2125' 
    text.insert(tk.END, ur)
    return ur



def char20():
    ur = '\u1E9E' 
    text.insert(tk.END, ur)
    return ur        

def char21():
    ur = '\u221A' 
    text.insert(tk.END, ur)
    return ur


def char22():
    ur = '\u2211' 
    text.insert(tk.END, ur)
    return ur        

def char23():
    ur = '\u221B' 
    text.insert(tk.END, ur)
    return ur        

  
def char24():
    ur = '\u221C' 
    text.insert(tk.END, ur)
    return ur


def char25():
    ur = '\u221D' 
    text.insert(tk.END, ur)
    return ur


def char26():
    ur = '\u221F' 
    text.insert(tk.END, ur)
    return ur
  
def char27():
    ur = '\u2220' 
    text.insert(tk.END, ur)
    return ur
  
def char28():
    ur = '\u2221' 
    text.insert(tk.END, ur)
    return ur
  
def char29():
    ur = '\u2222' 
    text.insert(tk.END, ur)
    return ur

  
def char30():
    ur = '\u2227' 
    text.insert(tk.END, ur)
    return ur
  
def char31():
    ur = '\u2228' 
    text.insert(tk.END, ur)
    return ur
  
def char32():
    ur = '\u2229' 
    text.insert(tk.END, ur)
    return ur
  
def char33():
    ur = '\u2282' 
    text.insert(tk.END, ur)
    return ur
  
def char34():
    ur = '\u22283' 
    text.insert(tk.END, ur)
    return ur
  
def char35():
    ur = '\u2284'
    text.insert(tk.END, ur)
    return ur
  
def char36():
    ur = '\u2285'
    text.insert(tk.END, ur)
    return ur

def char37():
  ur = '\u2286'
  text.insert(tk.END, ur)
  return ur

def char38():
  ur = '\u22BB'
  text.insert(tk.END, ur)
  return ur

def char39():
  ur = '\u22BC'
  text.insert(tk.END, ur)
  return ur

def char40():
  ur = '\u22BD'
  text.insert(tk.END, ur)
  return ur

def char41():
  ur = '\u22BF'
  text.insert(tk.END, ur)
  return ur

def char42():
  ur = '\u263C'
  text.insert(tk.END, ur)
  return ur

def char43():
  ur = '\u263D'
  text.insert(tk.END, ur)
  return ur

def char44():
  ur = '\u2263E'
  text.insert(tk.END, ur)
  return ur

def char45():
  ur = '\u263F'
  text.insert(tk.END, ur)
  return ur

def char46():
  ur = '\u2640'
  text.insert(tk.END, ur)
  return ur

def char47():
  ur = '\u2641'
  text.insert(tk.END, ur)
  return ur

def char48():
  ur = '\u2642'
  text.insert(tk.END, ur)
  return ur

def char49():
  ur = '\u2643'
  text.insert(tk.END, ur)
  return ur

def char50():
  ur = '\u2644'
  text.insert(tk.END, ur)
  return ur

def char51():
  ur = '\u2645'
  text.insert(tk.END, ur)
  return ur

def char52():
  ur = '\u22646'
  text.insert(tk.END, ur)
  return ur

def char53():
  ur = '\u2647'
  text.insert(tk.END, ur)
  return ur

def char54():
  ur = '\u039b'
  text.insert(tk.END, ur)
  return ur

def char55():
  ur = '\u2669'
  text.insert(tk.END, ur)
  return ur

def char56():
  ur = '\u266A'
  text.insert(tk.END, ur)
  return ur

def char57():
  ur = '\u266B'
  text.insert(tk.END, ur)
  return ur

def char58():
  ur = '\u266C'
  text.insert(tk.END, ur)
  return ur

def char59():
  ur = '\u266D'
  text.insert(tk.END, ur)
  return ur

def char60():
  ur = '\u266E'
  text.insert(tk.END, ur)
  return ur

def char61():
  ur = '\u266F'
  text.insert(tk.END, ur)
  return ur

def char62():
  ur = '\u221E'
  text.insert(tk.END, ur)
  return ur

def char63():
  ur = '\u2208'
  text.insert(tk.END, ur)
  return ur

def char64():
  ur = '\u2648'
  text.insert(tk.END, ur)
  return ur

def char65():
  ur = '\u2649'
  text.insert(tk.END, ur)
  return ur

def char66():
  ur = '\u264A'
  text.insert(tk.END, ur)
  return ur

def char67():
  ur = '\u264B'
  text.insert(tk.END, ur)
  return ur

def char68():
  ur = '\u264C'
  text.insert(tk.END, ur)
  return ur

def char69():
  ur = '\u264D'
  text.insert(tk.END, ur)
  return ur

def char70():
  ur = '\u264E'
  text.insert(tk.END, ur)
  return ur


def char71():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char72():
  ur = '\u2650'
  text.insert(tk.END, ur)
  return ur

def char73():
  ur = '\u2651'
  text.insert(tk.END, ur)
  return ur

def char74():
  ur = '\u2652'
  text.insert(tk.END, ur)
  return ur

def char75():
  ur = '\u2653'
  text.insert(tk.END, ur)
  return ur

def char76():
  ur = '\u2654'
  text.insert(tk.END, ur)
  return ur

def char77():
  ur = '\u2655'
  text.insert(tk.END, ur)
  return ur

def char78():
  ur = '\u2656'
  text.insert(tk.END, ur)
  return ur

def char79():
  ur = '\u2657'
  text.insert(tk.END, ur)
  return ur

def char80():
  ur = '\u2658'
  text.insert(tk.END, ur)
  return ur

def char81():
  ur = '\u2659'
  text.insert(tk.END, ur)
  return ur

def char82():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char83():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char84():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char85():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char86():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char87():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char88():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char89():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char90():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char91():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char92():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char93():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char94():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char95():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char96():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char97():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char98():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur

def char99():
  ur = '\u264F'
  text.insert(tk.END, ur)
  return ur


 

b1 = tk.Button(frm2, text='\u0394', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char1)
b1.grid(row=4, column=2)
b2 = tk.Button(frm2, text='\u03C0', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char2)
b2.grid(row=5, column=2)
b3 = tk.Button(frm2, text='\u03BB', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char3)
b3.grid(row=6, column=2)
b4 = tk.Button(frm2, text='\u03F4', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char4)
b4.grid(row=7, column=2)
b5 = tk.Button(frm2, text='\u03B8', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char5)
b5.grid(row=8, column=2)
b6 = tk.Button(frm2, text='\u03B1', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char6)
b6.grid(row=9, column=2)
b7 = tk.Button(frm2, text='\u03B2', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char7)
b7.grid(row=10, column=2)
b8 = tk.Button(frm2, text='\u03B3', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char8)
b8.grid(row=11, column=2)
b10 = tk.Button(frm2, text='\u03B4', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char9)
b10.grid(row=12, column=2)
b21 = tk.Button(frm2, text='\u03B5', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char10)
b21.grid(row=13, column=2)
b31 = tk.Button(frm2, text='\u03B6' , width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char11)
b31.grid(row=14, column=2)
b41 = tk.Button(frm2, text='\u03B7', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char12)
b41.grid(row=15, column=2)
b51 = tk.Button(frm2, text='\u2116', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='azure', command=char13)
b51.grid(row=16, column=2)

btn1 = tk.Button(frm2, text='\u2126', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char14)
btn1.grid(row=4, column=3)
btn2 = tk.Button(frm2, text='\u2122', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char15)
btn2.grid(row=5, column=3)
btn3 = tk.Button(frm2, text='\u222B', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char16)
btn3.grid(row=6, column=3)
btn4 = tk.Button(frm2, text='\u222C', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char17)
btn4.grid(row=7, column=3)
btn5 = tk.Button(frm2, text='\u222D', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char18)
btn5.grid(row=8, column=3)
btn6 = tk.Button(frm2, text='\u2125', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char19)
btn6.grid(row=9, column=3)
btn7 = tk.Button(frm2, text='\u1E9E', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char20)
btn7.grid(row=10, column=3)
btn8 = tk.Button(frm2, text='\u221A', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char21)
btn8.grid(row=11, column=3)
btn10 = tk.Button(frm2, text='\u2211', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char22)
btn10.grid(row=12, column=3)
btn21 = tk.Button(frm2, text='\u221B', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char23)
btn21.grid(row=13, column=3)
btn31 = tk.Button(frm2, text='\u221C', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char24)
btn31.grid(row=14, column=3)
btn41 = tk.Button(frm2, text='\u221D', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char25)
btn41.grid(row=15, column=3)
btn51 = tk.Button(frm2, text='\u221F', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='linen', command=char26)
btn51.grid(row=16, column=3)






but1 = tk.Button(frm2, text='\u2220', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char27)
but1.grid(row=4, column=6)
but2 = tk.Button(frm2, text='\u2221', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char28)
but2.grid(row=5, column=6)
but3 = tk.Button(frm2, text='\u2222', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char29)
but3.grid(row=6, column=6)
but4 = tk.Button(frm2, text='\u2227', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char30)
but4.grid(row=7, column=6)
but5 = tk.Button(frm2, text='\u2228', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char31)
but5.grid(row=8, column=6)
but6 = tk.Button(frm2, text='\u2229', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char32)
but6.grid(row=9, column=6)
but7 = tk.Button(frm2, text='\u2282', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char33)
but7.grid(row=10, column=6)
but8 = tk.Button(frm2, text='\u2283', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char34)
but8.grid(row=11, column=6)
but10 = tk.Button(frm2, text='\u2284', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char35)
but10.grid(row=12, column=6)
but21 = tk.Button(frm2, text='\u2285', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char36)
but21.grid(row=13, column=6)
but31 = tk.Button(frm2, text='\u2286', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char37)
but31.grid(row=14, column=6)
but41 = tk.Button(frm2, text='\u22BB', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char38)
but41.grid(row=15, column=6)
but51 = tk.Button(frm2, text='\u22BC', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='light yellow', command=char39)
but51.grid(row=16, column=6)




butt1 = tk.Button(frm2, text='\u22BD', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char40)
butt1.grid(row=4, column=7)
butt2 = tk.Button(frm2, text='\u22BF', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char41)
butt2.grid(row=5, column=7)
butt3 = tk.Button(frm2, text='\u263C', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char42)
butt3.grid(row=6, column=7)
butt4 = tk.Button(frm2, text='\u263D', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char43)
butt4.grid(row=7, column=7)
butt5 = tk.Button(frm2, text='\u263E', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char44)
butt5.grid(row=8, column=7)
butt6 = tk.Button(frm2, text='\u263F', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char45)
butt6.grid(row=9, column=7)
butt7 = tk.Button(frm2, text='\u2640', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char46)
butt7.grid(row=10, column=7)
butt8 = tk.Button(frm2, text='\u2641', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char47)
butt8.grid(row=11, column=7)
butt10 = tk.Button(frm2, text='\u2642', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char48)
butt10.grid(row=12, column=7)
butt21 = tk.Button(frm2, text='\u2643', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char49)
butt21.grid(row=13, column=7)
butt31 = tk.Button(frm2, text='\u2644', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char50)
butt31.grid(row=14, column=7)
butt41 = tk.Button(frm2, text='\u2645', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char51)
butt41.grid(row=15, column=7)
butt51 = tk.Button(frm2, text='\u2646', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='alice blue', command=char52)
butt51.grid(row=16, column=7)





but11 = tk.Button(frm2, text='\u2647', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char53)
but11.grid(row=4, column=8)
but21 = tk.Button(frm2, text='\u039b', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char54)
but21.grid(row=5, column=8) 
but31 = tk.Button(frm2, text='\u2669', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char55)
but31.grid(row=6, column=8)
but41 = tk.Button(frm2, text='\u266A', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char56)
but41.grid(row=7, column=8)
but51 = tk.Button(frm2, text='\u266B', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char57)
but51.grid(row=8, column=8)
but61 = tk.Button(frm2, text='\u266C', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char58)
but61.grid(row=9, column=8)
but71 = tk.Button(frm2, text='\u266D', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char59)
but71.grid(row=10, column=8)
but81 = tk.Button(frm2, text='\u266E', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char60)
but81.grid(row=11, column=8)
but110 = tk.Button(frm2, text='\u266F', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char61)
but110.grid(row=12, column=8)
but211 = tk.Button(frm2, text='\u221E', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char62)
but211.grid(row=13, column=8)
but311 = tk.Button(frm2, text='\u2208', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char63)
but311.grid(row=14, column=8)
but411 = tk.Button(frm2, text='\u2648', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char64)
but411.grid(row=15, column=8)
but511 = tk.Button(frm2, text='\u2649', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char65)
but511.grid(row=16, column=8)


bbu1 = tk.Button(frm2, text='\u264A', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char66)
bbu1.grid(row=4, column=9)
bbu2 = tk.Button(frm2, text='\u264B', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char67)
bbu2.grid(row=5, column=9)
bbu3 = tk.Button(frm2, text='\u264C', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char68)
bbu3.grid(row=6, column=9)
bbu4 = tk.Button(frm2, text='\u264D', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char69)
bbu4.grid(row=7, column=9)
bbu5 = tk.Button(frm2, text='\u264E', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char70)
bbu5.grid(row=8, column=9)
bbu6 = tk.Button(frm2, text='\u264F', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char71)
bbu6.grid(row=9, column=9)
bbu7 = tk.Button(frm2, text='\u2650', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char72)
bbu7.grid(row=10, column=9)
bbu8 = tk.Button(frm2, text='\u2651', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char73)
bbu8.grid(row=11, column=9)
bbu10 = tk.Button(frm2, text='\u2652', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char74)
bbu10.grid(row=12, column=9)
bbu21 = tk.Button(frm2, text='\u2653', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char75)
bbu21.grid(row=13, column=9)
bbu31 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char76)
bbu31.grid(row=14, column=9)
bbu41 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char77)
bbu41.grid(row=15, column=9)
bbu51 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char78)
bbu51.grid(row=16, column=9)


bb44 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char79)
bb44.grid(row=4, column=10)
bb442 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char80)
bb442.grid(row=5, column=10)
bb443 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char81)
bb443.grid(row=6, column=10)
bb444 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char82)
bb444.grid(row=7, column=10)
bb445 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char83)
bb445.grid(row=8, column=10)
bb446 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char84)
bb446.grid(row=9, column=10)
bb447 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char85)
bb447.grid(row=10, column=10)
bb448 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char86)
bb448.grid(row=11, column=10)
bb4410 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char87)
bb4410.grid(row=12, column=10)
bb4421 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char88)
bb4421.grid(row=13, column=10)
bb4431 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char89)
bb4431.grid(row=14, column=10)
bb4441 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char90)
bb4441.grid(row=15, column=10)
bb4451 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char91)
bb4451.grid(row=16, column=10)

butt91 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char92)
butt91.grid(row=4, column=11)
butt92 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char93)
butt92.grid(row=5, column=11)
butt93 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char94)
butt93.grid(row=6, column=11)
butt94 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char95)
butt94.grid(row=7, column=11)
butt95 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char96)
butt95.grid(row=8, column=11)
butt96 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char97)
butt96.grid(row=9, column=11)
butt97 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char98)
butt97.grid(row=10, column=11)
butt98 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=char99)
butt98.grid(row=11, column=11)
butt910 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
butt910.grid(row=12, column=11)
butt921 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
butt921.grid(row=13, column=11)
butt931 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
butt931.grid(row=14, column=11)
butt941 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
butt941.grid(row=15, column=11)
butt951 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
butt951.grid(row=16, column=11)

bu112 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu112.grid(row=4, column=12)
bu245 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu245.grid(row=5, column=12)
bu332 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu332.grid(row=6, column=12)
bu478 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu478.grid(row=7, column=12)
bu500 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu500.grid(row=8, column=12)
bu656 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu656.grid(row=9, column=12)
bu777 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu777.grid(row=10, column=12)
bu824 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu824.grid(row=11, column=12)
bu150 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu150.grid(row=12, column=12)
bu251 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu251.grid(row=13, column=12)
bu351 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu351.grid(row=14, column=12)
bu461 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu461.grid(row=15, column=12)
bu561 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bu561.grid(row=16, column=12)

btn14 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn14.grid(row=4, column=13)
btn25 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn25.grid(row=5, column=13)
btn36 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn36.grid(row=6, column=13)
btn47 = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn47.grid(row=7, column=13)
btn59 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn59.grid(row=8, column=13)
btn62 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn62.grid(row=9, column=13)
btn71 = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn71.grid(row=10, column=13)
btn8r = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn8r.grid(row=11, column=13)
btn10r = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn10r.grid(row=12, column=13)
btn21r = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn21r.grid(row=13, column=13)
btn31r = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn31r.grid(row=14, column=13)
btn41r = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn41r.grid(row=15, column=13)
btn51r = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
btn51r.grid(row=16, column=13)

bt14a = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt14a.grid(row=4, column=14)
bt25a = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt25a.grid(row=5, column=14)
bt36a = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt36a.grid(row=6, column=14)
bt47a = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt47a.grid(row=7, column=14)
bt59a = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt59a.grid(row=8, column=14)
bt62a = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt62a.grid(row=9, column=14)
bt71a = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt71a.grid(row=10, column=14)
bt8ra = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt8ra.grid(row=11, column=14)
bt10ar = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt10ar.grid(row=12, column=14)
bt21ar = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt21ar.grid(row=13, column=14)
bt31ar = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt31ar.grid(row=14, column=14)
bt41ar = tk.Button(frm2, text='     ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt41ar.grid(row=15, column=14)
bt51ar = tk.Button(frm2, text='    ', width=1,height=1,font=('arial',12,'bold'),bd=4,bg='lavender', command=None)
bt51ar.grid(row=16, column=14)









if __name__ == '__main__':

  root.mainloop()
