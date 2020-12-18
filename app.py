import tkinter as tk
import tkinter
from tkinter import ttk
from spam_classifier import SpamClassifier, process_message
import numpy as np
import pandas as pd
import pickle
import os

NORM_FONT= ("Verdana", 10)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Given Text Was")
    popup.geometry("250x100")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack(padx =10,pady=20)
    popup.mainloop()

def check():
	rawText = textbox.get('1.0' , tk.END)
	pm = process_message(rawText)
	res = sc_tf_idf.classify(pm)

	if res == True:
		return popupmsg("Uh Oh look like SPAM")
	else:
		return popupmsg("cheers! NOT like SPAM")

# using the model again

model_name = "spam_ham_clf.pkl"
clf_pkl = open(model_name,'rb')
sc_tf_idf = pickle.load(clf_pkl)


class myapp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, "'SPAM or HAM' Detector")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=5)
		container.grid_columnconfigure(0, weight=5)


app = myapp()

img = tk.Image("photo", file="appicon.gif")
app.call('wm','iconphoto',app._w,img)


m_frm = tk.Frame(app,bg="#839192")
frm_info = tk.Frame(m_frm,bg="#839192")
frm_txt = tk.Frame(m_frm,bg="#839192")
frm_btns = tk.Frame(m_frm,bg="#839192")

greeting = tk.Label(master = frm_info,bg="#839192", text="Hello, User WELCOME !!",font=NORM_FONT)
greeting.pack()
greeting = tk.Label(master = frm_info,bg="#839192", text="ENTER THE TEXT BELOW TO CHECK SPAM OR HAM")
greeting.pack()


textbox = tk.Text(master = frm_txt,height = 6, width = 60)
textbox.pack(padx =20,pady=20)

btn_submit = ttk.Button(master= frm_btns ,text="Check", command=check)
btn_submit.pack(pady=10)
btn_exit = ttk.Button(master=frm_btns , text="Quit", command = quit )
btn_exit.pack(padx =20,pady=10)


m_frm.pack()
frm_info.pack()
frm_txt.pack()
frm_btns .pack()

app.mainloop()