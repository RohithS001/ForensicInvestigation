from tkinter import messagebox,Text
from tkinter import *
import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
#nltk.download()
stop_words = set(stopwords.words('english')) 
top=Tk()
top.resizable(False, False)
top.geometry("1000x600")
top.configure(bg="#8a7d88")
top.title('Forensic Investigation System')
w_f={};r_f={}
E1 = Text(top,fg="red",width=50,height=10)
E2 = Text(top,fg="red",width=50,height=10)
def gettext():
    global w_f
    mag=E1.get("1.0",'end-1c')
    #messagebox.showinfo("",mag)
    mag_tokens = word_tokenize(mag) 
    mag_filter= [w for w in mag_tokens if not w in stop_words] 
    word_freq=[mag_filter.count(p) for p in mag_filter]
    w_f=dict(zip(mag_filter,word_freq))
    result = json.dumps(w_f)
    #E1.delete('1.0', END)
    #E1.insert(INSERT, result)

def cleartext():
    E1.delete('1.0', END)

def clearransom():
    E2.delete('1.0', END)
    

def getransom():
    global r_f
    ransom=E2.get("1.0",'end-1c')
    ran_tokens = word_tokenize(ransom) 
    ran_filter= [w for w in ran_tokens if not w in stop_words] 
    ran_freq=[ran_filter.count(p) for p in ran_filter]
    r_f=dict(zip(ran_filter,ran_freq))
    result1= json.dumps(r_f)
    E2.delete('1.0', END)
    E2.insert(INSERT, result1)

def invest():
    miss="";has=""
    for i in r_f:
        if i in w_f:
            has+=i
            has+=","
        else:
            miss+=i
            miss+=","
    l_text="words Matched : "+has
    l2_text="words Missing : "+miss
    
l_text="words Matched : "
l2_text="No.of words Missing :"
L1 = Label(top, text="Enter Magazine Data:",fg="blue",font=1)
L1.place(x=25,y=80)
L2 = Label(top, text="Enter Ransom Notes:",fg="blue",font=1)
L2.place(x=25,y=280)
L3 = Label(top,fg="red",bg="#8a7d88",font=2)
L3.config(text = l_text)

L4 = Label(top,fg="red",bg="#8a7d88",font=2)
L4.config(text = l2_text)
B = Button(top, text ="Investigate",command =invest,width=20,fg="yellow",bg="red",font=1)
#B1 = Button(top, text ="Hi", command = lambda:L1.pack())
B2 = Button(top, text ="Submit Magazine", command = gettext,width=20,fg="black",bg="cyan",font=1)
B3 = Button(top, text ="Clear Magazine", command = cleartext,width=20,fg="brown",bg="yellow",font=1)
B4 = Button(top, text ="Submit Ransom Notes", command = getransom,width=20,fg="black",bg="cyan",font=1)
B5 = Button(top, text ="Clear Ransom Notes", command = clearransom,width=20,fg="brown",bg="yellow",font=1)
L3.place(x=250,y=400)
L4.place(x=550,y=400)
E1.place(x=200,y=20)
E2.place(x=200,y=200)
B.place(x=20,y=400)
#B1.pack()
B2.place(x=650,y=70)
B3.place(x=650,y=120)
B4.place(x=650,y=240)
B5.place(x=650,y=290)
top.mainloop()
