# pip install image
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

def image_to_see():
	filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image file", filetype=(("JPG FILE", "*.jpg"),("PNG FILE", "*.png")))
	img_1 = Image.open(filename)
	img_1 = ImageTk.PhotoImage(img_1)
	lbl_final.configure(image=img_1)
	lbl_final.image = img_1

root = Tk()

cover = Frame(root)
cover.pack(side=BOTTOM,padx=15,pady=15)

lbl_final = Label(root)
lbl_final.pack()

btn_1 = Button(cover, text = "Select Image", command=image_to_see)
btn_1.pack(side=tk.LEFT)

btn_2 = Button(cover, text = "Exit", command = lambda:exit())
btn_2.pack(side=tk.LEFT, padx=12)

root.title("MY OWN IMAGE VIEWER")
root.geometry("500x500")
root.mainloop()
