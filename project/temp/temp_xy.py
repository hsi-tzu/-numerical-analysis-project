import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import cartopy.crs as crs
import numpy as np
from matplotlib.tri import Triangulation
import shapefile as shp

 
templevel=[i for i in range(-1,40)]
level=[i for i in range(-1,39,2)]
level.append(38)
cwbcr = ["#42808D","#1F7E94","#2E899C","#3C93A7","#4C9DB0","#5DA8BF","#6DB4C3","#76BECC","#87CBD8","#96D4E3","#A4E0EB","#B1EBF6",
"#0C924D","#1C9A53","#2FA257","#42AA5E","#50B164","#61B86A","#74C171","#86CA77","#95D07C","#A8D884","#B9DF88","#C9E68E","#D8F092",
"#F1F3C2","#F6E68E","#F2D376","#F1C361","#EFB14C","#EB9D3B","#E68C2A","#E2770C","#EC5037","#EE165B","#AB0739","#760005","#9A68AE","#854C99","#71278E"]
def triangles(lon,lat,tri,temp):
    temp=np.array(temp).astype('float32')
    for i in tri.triangles:
        lon_ap=np.sum(lon[i])/3
        lat_ap=np.sum(lat[i])/3
        lon=np.append(lon,lon_ap)
        lat=np.append(lat,lat_ap)
        w1=(lat[i[1]]-lat[i[2]])*(lon_ap-lon[i[2]])+(lon[i[2]]-lon[i[1]])*(lat_ap-lat[i[2]])
        w1=w1/((lat[i[1]]-lat[i[2]])*(lon[i[0]]-lon[i[2]])+(lon[i[2]]-lon[i[1]])*(lat[i[0]]-lat[i[2]]))
        w2=(lat[i[2]]-lat[i[0]])*(lon_ap-lon[i[2]])+(lon[i[0]]-lon[i[2]])*(lat_ap-lat[i[2]])
        w2=w2/((lat[i[1]]-lat[i[2]])*(lon[i[0]]-lon[i[2]])+(lon[i[2]]-lon[i[1]])*(lat[i[0]]-lat[i[2]]))
        w3=1-w1-w2
        t=temp[i[0]]*w1+temp[i[1]]*w2+temp[i[2]]*w3
        temp=np.append(temp,t)
    return lon,lat,temp
data=pd.read_csv(r".\station2.csv")
stno=data["stno"]
loctime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
year=loctime[0:4]
mon=loctime[5:7]
day=int(loctime[8:10])-1
#print(year,mon,day)
temp=[]
nonstn=[]
path_t=r".\mapdata202008310842\COUNTY_MOI_1090820.shp" #縣界shapefile
for st in stno:
    url="http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station="+str(st)+"&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker="
    url=url+str(year)+"-"+str(mon)+"-"+str(day).zfill(2)
    response = requests.get(url)
    #print(url)
    # 一般python會自動編成big5，網頁的utf-8會變亂碼
    response.encoding = 'utf-8'
    # 解析HTML,lxml解析器速度較html.parser快
    soup = BeautifulSoup(response.text, "html.parser")
    # 讀取表格
    table = soup.find(id='MyTable').tbody
    # 抓取所有標題
    titles = table.find('tr', 'second_tr').find_all('th')
    title = []
    weather={}
    for j in range(0, len(titles)):
        result = titles[j].text
        title.append(result)
    # 抓取特定欄位下每筆資料
    rows = table.find_all('tr')
    for col in range(0, 4, 1):
        # 創建暫存list，存取每項資料的所有數值
        d = []
        #  只取海平面氣壓, 溫度, 濕度, 濕度, 風速, 風向降水量,日照
        if  col == 3 :
            # 讀取每一行，從最上面標題行之後開始
            for r in rows[2:]:
                # 每欄資料中間都隔了一個<br>
                index = col * 2 + 1
                value = r.contents[index].string
                # 去除字串尾部\xa0 空白字元,split不帶參數時為自動去除換行符...等
                # 存進字典中
                value = "".join(value.split())
                d.append(value)
            weather[d[0]] = d[1::]
    # # 轉換非數字的欄位
    v = weather["Temperature"]
    num = v.count('T')
    while (num > 0):
        i = v.index('T')
        v[i] = '0.1'
        num = num - 1
    num1 = v.count('X')
    num2 = v.count('')
    num3 = v.count('...')
    num4 = v.count('/')
    numt=num1+num2+num3+num4
    if  (numt > 0):
        a=weather["Temperature"]
        a=["-9999"if x == "X" else x for x in a]
        a=["-9999" if x == '' else x for x in a]
        a=["-9999" if x == "..." else x for x in a]
        a=["-9999" if x == "/" else x for x in a]
        weather["Temperature"]=a                  
    if weather["Temperature"] == []:
        nonstn.append(st)
    elif weather["Temperature"][-1] == "-9999":
        nonstn.append(st)
    else:
        temp.append(weather["Temperature"][-1])
    #print(temp)
for i in nonstn:
    data=data[data["stno"]!=i]
lon=np.array(data["lon"])
lat=np.array(data["lat"])
t=Triangulation(lon,lat)
lon_n,lat_n,temp_n=triangles(lon,lat,t,temp)
#print(lon_n,"\n",lon)
tr=Triangulation(lon_n,lat_n)
#fig =plt.figure(figsize=(16,12)) 
#proj=crs.LambertConformal(125,25)
 #= fig.add_subplot(1,1,1,projection=proj) #子圖位置
#xticks = np.arange(-180, 181, 1)
#yticks = np.arange(-90, 91, 1)
#ax.set_xticks(xticks, crs=proj)
#ax.set_yticks(yticks, crs=proj)
#ax.set_xlim(118, 122.5)
#ax.set_ylim(21.8, 25.5)
#sf=shp.Reader(path_t)
#for shape in sf.shapeRecords(): #就是把shapefile檔的各部份分開畫
    #for i in range(len(shape.shape.parts)):
        #i_start = shape.shape.parts[i]
        #if i==len(shape.shape.parts)-1:
            #i_end = len(shape.shape.points)
        #else:
            #i_end = shape.shape.parts[i+1]
        #x = [i[0] for i in shape.shape.points[i_start:i_end]]
        #y = [i[1] for i in shape.shape.points[i_start:i_end]]
        #plt.plot(x,y,color="black",linewidth=1.5) #畫出地形圖
#contour=ax.tricontourf(tr,temp_n,levels=templevel,colors=cwbcr,extend="both")
#plt.plot(lon_n,lat_n,"o",color="black")
#plt.colorbar(contour,ticks=level)
#plt.title("temp.")
#plt.show()
y=121.7447344
x=25.08097003
distan=[]
for i in range(0,np.size(lon_n),1):
    distan.append(((y-lon_n[i])**2+(x-lat_n[i])**2)**(1/2))
   #if (y+0.1)>=lon_n[i] and (y-0.1)<=lon_n[i] and (x+0.1)>=lat_n[i] and (x-0.1)<=lat_n[i] :
       #print(lon_n[i],i)
       #print(lat_n[i],i)
       #lon_y.append(lon_n[i])
       #lat_x.append(lat_n[i])
       #sum1=abs(lon_n[i]-y)+abs(lat_n[i]-x)
       #con.append(sum1)
print(temp_n[distan.index(min(distan))])
#print(tempxy(121.683628,25.10962028))