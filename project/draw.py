
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk #讀png要裝這個
import temp_draw #導入程式

w=tk.Tk()
w.title('test')
w.geometry('700x900')
w.configure(background='white')

#P=['Pa','Pb','Pc','Pd']


img = Image.open('temp.png') #打開圖檔
photo = ImageTk.PhotoImage(img)
imglabel = tk.Label(w, image=photo) #選擇視窗放圖
imglabel.place(x=-100,y=50) #圖有點大所以位置很怪
w.mainloop() #這一定要加，不然跑不出圖，目前想不到更好的解法了
            
#comboExample=ttk.Combobox(w, values=["Pa","Pb","Pc","Pd"])
#comboExample.place(x=50,y=20)
#comboExample.bind("<<ComboboxSelected>>", CE)

