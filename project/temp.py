import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import cartopy.crs as ccrs
import numpy as np
from metpy.interpolate import interpolate_to_grid, remove_nan_observations
cwblevel=[0,1,2,6,10,15,20,30,40,50,70,90,110,130,150,200,300,np.inf]
level=[0,1,2,6,10,15,20,30,40,50,70,90,110,130,150,200,300]
cwbe=[467110,467300,467350,467990,466950,467620,"C0S730","C0R270"]
cwbcr = ["#C9CBC7","#9EFBFF","#01D2F9","#01A5FF","#0276FE","#29A218","#00FD2F","#FEFB31","#FFD328","#FEA626",
"#F62D07","#DD2105","#A81900","#A722A6","#D92ED4","#FC3AF9","#FFD5FF"]
data=pd.read_csv(r".\station.csv")
for i in cwbe:
    data=data[data["stno"]!=i]
stno=data["stno"]
loctime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
year=loctime[0:4]
mon=loctime[5:7]
day=int(loctime[8:10])-2
temp=[]
nonstn=[]
# print(loctime)
# print(year,mon,day)
# star=data.loc[data["loca"].str.contains("苗")]
# print(star)
for st in stno:
    url="http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station="+str(st)+"&stname=%25E9%259E%258D%25E9%2583%25A8&datepicker=2020-12-31"
    url=url#+str(year)+"-"+str(mon)+"-"+str(day)
    print(url)
    response = requests.get(url)
    # 一般python會自動編成big5，網頁的utf-8會變亂碼
    response.encoding = 'utf-8'
    # 解析HTML,lxml解析器速度較html.parser快
    soup = BeautifulSoup(response.text, "html.parser")
    # soup = BeautifulSoup(response.text, "lxml")
    # print(soup.prettify())
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
            # print(type(weather.items()))
    # print("Json:", json.dumps(weather, indent=4, sort_keys=True))
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
    #print(temp)
    if weather["Temperature"] == []:
        nonstn.append(st)
    elif weather["Temperature"][-1] == "-9999":
        nonstn.append(st)
    else:
        temp.append(weather["Temperature"][-1])
for i in nonstn:
    data=data[data["stno"]!=i]
lon=data["lon"]
lat=data["lat"]
#print(temp)
gx,gy,g=interpolate_to_grid(lon, lat, np.array(temp).astype("float32"), interp_type='barnes', minimum_neighbors=0.01, search_radius=.2, hres=.05)
fig =plt.figure(figsize=(16,12)) 
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree()) #子圖位置
ax.coastlines()
ax.gridlines(linestyle='--')
xticks = np.arange(-180, 181, 1)
yticks = np.arange(-90, 91, 1)
ax.set_xticks(xticks, crs=ccrs.PlateCarree())
ax.set_yticks(yticks, crs=ccrs.PlateCarree())
ax.set_xlim(119.5, 122.5)
ax.set_ylim(21.8, 26)
contour=plt.contourf(gx,gy,g,levels=cwblevel,colors=cwbcr)
plt.plot(lon,lat,"o",color="black")
plt.colorbar(contour,ticks=level)
plt.title("temp.")
plt.show()