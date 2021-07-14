import tkinter as tk
from tkinter import ttk 
from tkinter import *
from PIL import Image,ImageTk
import PIL.Image
import numpy as np
from random import choice
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import cartopy.crs as ccrs
from metpy.interpolate import interpolate_to_grid, remove_nan_observations
import avgmean
import usemodel
import project2
import temp_xy



TWplace=["使用經緯度","基隆","臺北","新北","桃園","新竹","苗栗","彰化","臺中","南投","雲林","嘉義","臺南","高雄","屏東","臺東","花蓮","宜蘭","澎湖","連江","金門"]

path='./植物23333.txt'  #讀檔路徑
with open(path,'r', encoding = 'utf-8')as f:  #讀檔
  data=f.readline()  #讀掉第一行的T(C)
  data1=f.read().split()  #讀之後的全部資料，並用空白鍵把每個資料做分割
#print(data1)

word=["別對自己要求太高\n畢竟你也做不到","雨天了,怎麼辦?\n帶傘啊","我不討厭人\n討厭我的都不是人","大家總說要跨出舒適圈\n但我連跨都沒跨進去過","因為明天不一定更好\n所以今天更要快樂","比起彩虹,我更期待\n你有和我一起淋濕的勇氣","我最大的不足\n就是餘額不足",
"人生就像香菜\n什麼都沒做也會被討厭","無論走到生命的哪個階段\n都該喜歡那段時光","昨天吃了條鮭魚\n今天他在我胃食道逆流"]

def variable(): #取得植物資料
    plant = str(comboExample.get())
    places = str(comboExample2.get())
    if (places!="") or (places!="使用經緯度"):
                temp_place=avgmean.ave(places)
                temp=temp_place
                print(temp_place)
    if (places==None) or (places=="使用經緯度"):
                temp_y = float(lon.get())
                temp_x = float(lat.get())
                print(temp_y)
                temp_lonlat=temp_xy.tempxy(temp_y,temp_x)
                temp=temp_lonlat
                places="當地"
                remind3.configure(text="")
                print(temp_y)
    for i in range(0,105,7):
        if data1[i]==plant:
            #print("選擇的植物",data1[i])
            for j in range(i+1,i+6,1):
                data1[j]=float(data1[j])
            #print(data1[i:i+7])
            water2.configure(text =data1[i+6] ,font=("Microsoft YaHei Light", 12, "roman"),fg="#62b6cb")
            chance=usemodel.rain_chances(places)
            place_tem.configure(text="%s昨日的平均溫度是 %.1f度"% (places,temp),bg="#ffffff",fg="#588157",font=("Microsoft New Tai Lue", 15, "roman",))
            if temp<data1[i+1]:
                remind2.configure(text="(%s適合的溫度為%d~%d)\n%s能忍受的最低溫是%d度,\n趕快把它收到室內保暖~不然可能會死掉"% (data1[i],data1[i+3],data1[i+4],data1[i],data1[i+1]),bg="#ffffff",fg="#3a5a40",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
            if temp>=data1[i+1] and temp<data1[i+3]:
                remind2.configure(text="(%s適合的溫度為%d~%d)\n溫度略低於適合%s生長的溫度，\n想要讓%s長得好的話，\n記得將%s移進室內保暖~"% (data1[i],data1[i+3],data1[i+4],data1[i],data1[i],data1[i]),bg="#ffffff",fg="#3a5a40",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
            if temp>=data1[i+3] and temp<=data1[i+4]:
                remind2.configure(text="(%s適合的溫度為%d~%d)\n溫度適合%s生長,\n希望你的植物能頭好壯壯~\n"% (data1[i],data1[i+3],data1[i+4],data1[i]),bg="#ffffff",fg="#3a5a40",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
            if temp>data1[i+4] and temp<=data1[i+2]:
                remind2.configure(text="(%s適合的溫度為%d~%d)\n溫度略高於適合%s生長的溫度，\n想要讓%s長得好的話，\n嘗試將溫度降至%d度"% (data1[i],data1[i+3],data1[i+4],data1[i],data1[i],data1[i+4]),bg="#ffffff",fg="#3a5a40",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
            if temp>data1[i+2]:
                remind2.configure(text="(%s適合的溫度為%d~%d)\n%s能忍受的最高溫是%d度,\n趕快嘗試降溫~不然可能會死掉"% (data1[i],data1[i+3],data1[i+4],data1[i],data1[i+2]),bg="#ffffff",fg="#3a5a40",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
            if places!="當地":
                if chance<30:
                    remind3.configure(text="%s降雨機率是百分之%d,\n可以考慮給植物澆水~"% (places,chance),bg="#ffffff",fg="#4f5d75",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
                if chance>=30 and chance<=50:
                    remind3.configure(text="%s降雨機率是百分之%d,\n可以依狀況給植物澆水~"% (places,chance),bg="#ffffff",fg="#4f5d75",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
                if chance>50:
                    remind3.configure(text="%s降雨機率是百分之%d,\n放在室外讓雨幫你澆水~"% (places,chance),bg="#ffffff",fg="#4f5d75",font=("Microsoft New Tai Lue", 25, "roman"),justify = 'left')
            #--------------------------------------------------------------------------
            
def talking():
    labelTalk.configure(text =choice(word) ,font=("Microsoft YaHei Light", 12, "roman"),fg="#006d77")
    
def temper():

    new=tk.Toplevel(w)
    new.geometry('600x600')
    canvas = Canvas(new, 
           width=1200, 
           height=700)
    canvas.pack()

    img22 = ImageTk.PhotoImage(file="背景.gif")
    canvas.create_image(0,0, anchor=NW, image=img22)
    a,f,maxi,mini=project2.ncu()
    def CE():
                fig=plt.figure(figsize=(6,3),dpi=100)
                f_plot=fig.add_subplot(111)
                canvas_spice=FigureCanvasTkAgg(fig,new)
                canvas_spice.get_tk_widget().place(x=0,y=200)
                x=a
                y=f
                f_plot.clear()
                plt.plot(x,y)
                plt.xlabel("time(hr)",labelpad=-10)
                plt.ylabel("temp.(C)",rotation=0)
                plt.grid()
                canvas_spice.draw()
    ma=tk.Label(new,text="昨天溫度最大值為%.2f度,最小值為%.2f度"%(maxi,mini),bg="#ffffff",fg="#3a506b",font=("Microsoft New Tai Lue", 16, "roman"))
    ma.place(x=50,y=120)
    draw= tk.Button(new,text="顯示圖表",command=CE,bg="#3a506b",fg="#c6eff7",font=("Microsoft New Tai Lue", 13, "roman"))
    draw.place(x=480,y=120)
    

    new.mainloop()
    
def temp_tai():
    import temp_draw
    new2=tk.Toplevel(w)
    new2.geometry('700x900')
    canvas = Canvas(new2, 
           width=1200, 
           height=900)
    canvas.pack()

    img22 = ImageTk.PhotoImage(file="背景2.gif")
    canvas.create_image(0,0, anchor=NW, image=img22)
    def DE():
            img = PIL.Image.open('temp.png') #打開圖檔
            photo = ImageTk.PhotoImage(img)
            imglabel = tk.Label(new2, image=photo) #選擇視窗放圖
            imglabel.place(x=-100,y=50) #圖有點大所以位置很怪
            new2.mainloop()
    
    draw= tk.Button(new2,text="顯示圖表",command=DE,bg="#3a506b",fg="#c6eff7",font=("Microsoft New Tai Lue", 13, "roman"))
    draw.place(x=480,y=120)
    

    new2.mainloop()
    


w = tk.Tk()
w.geometry('1200x600')
w.configure(bg='#f4f1de')
w.title("植物語")
canvas = Canvas(w, 
           width=1200, 
           height=600)
canvas.pack()

img = ImageTk.PhotoImage(file="plant4.gif")
canvas.create_image(0,0, anchor=NW, image=img)

photo1 = tk.PhotoImage(file="植物2.gif")
labelTop = tk.Label(w,text = "選擇植物",bg="#e07a5f",font=("Microsoft New Tai Lue", 16, "roman"),height=27, width=175,fg="#f4f1de",image=photo1,compound="left")
labelTop.place(x = 10+100, y = 40)

comboExample = ttk.Combobox(w,values=["菊花","空氣鳳梨","百合","辣椒","蓮花","迷迭香","虎尾蘭","桂花","金錢樹","玫瑰","白木水","牽牛花","雞蛋花","袖珍椰子","玉簪"])
#comboExample.current(0)
comboExample.place(x = 200+100, y = 45)

photo2 = tk.PhotoImage(file="地圖5.gif")
labelTop2 = tk.Label(w,text = "選擇地區(擇一)",bg="#81b29a",font=("Microsoft New Tai Lue", 16, "roman"),height=27, width=175,fg="#f4f1de",image=photo2,compound="left")
labelTop2.place(x = 400+100, y = 40)

comboExample2 = ttk.Combobox(w,values=TWplace,)
comboExample2.place(x = 590+100, y = 40)


photo3 = tk.PhotoImage(file="花.gif")
start= tk.Button(w,text="開始",bg="#f5cac3",command=variable,font=("Microsoft New Tai Lue", 12), width=100,fg="#9a031e",relief="flat",image=photo3,compound="left")
start.place(x = 850+100, y = 40)

photo4 = tk.PhotoImage(file="仙人掌.gif")
talk= tk.Button(w,text="",bg="#ffffff",relief="flat",image=photo4,command=talking)
talk.place(x = 950, y = 350)

photo5 = tk.PhotoImage(file="溫度.gif")
rain= tk.Button(w,text="中央大學專用",bg="#D6F9FF",font=("Microsoft New Tai Lue", 12, "roman"),height=100,width=100,relief="flat",fg="#197278",image=photo5,compound="bottom",command=temper)
rain.place(x = 950, y = 100)

photo7 = tk.PhotoImage(file="taiwan.gif")
tai= tk.Button(w,text="台灣昨日\n24:00溫度",bg="#ffe5d9",font=("Microsoft New Tai Lue", 12, "roman"),height=100,width=100,relief="flat",fg="#9a031e",image=photo7,compound="bottom",command=temp_tai)
tai.place(x = 950, y = 210)

labelTalk = tk.Label(w,bg="#ffffff")
labelTalk.place(x = 780, y = 450)

remind= tk.Label(w,text = "今日需注意的狀況:",bg="#ffffff",font=("Microsoft New Tai Lue", 20, "roman"),width=15,fg="#3a5a40",borderwidth=0)
remind.place(x = 160, y = 100)

photo6 = tk.PhotoImage(file="水.gif")
water = tk.Label(w,text = "水量小提醒：",bg="#62b6cb",font=("Microsoft New Tai Lue", 16, "roman"),fg="#ffffff",image=photo6,compound="left")
water.place(x = 200+70, y = 500-50)

water2 = tk.Label(w,bg="#ffffff")
water2.place(x = 360+70, y = 500-50)

place_tem = tk.Label(w,bg="#ffffff")
place_tem.place(x = 670, y = 120)

remind2 = tk.Label(w,bg="#ffffff")
remind2.place(x = 260, y = 170)

remind3 = tk.Label(w,bg="#ffffff")
remind3.place(x = 260, y = 350)

lon = tk.Entry(w,bg="#a8dadc")
lon.insert(0, "0")
lon.place(x = 590+100, y = 70)

lat = tk.Entry(w,bg="#a8dadc") 
lat.insert(0, "0")
lat.place(x = 590+100, y = 90)

lon_r = tk.Label(w,text="經度",bg="#ffffff")
lon_r.place(x = 840, y = 70)

lat_r = tk.Label(w,text="緯度",bg="#ffffff")
lat_r.place(x = 840, y = 90)
w.mainloop()