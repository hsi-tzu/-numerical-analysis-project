import requests
import time
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def ncu():
    loctime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    #print(loctime)
    year=loctime[0:4]
    mon=loctime[5:7]
    day=loctime[8:10]
    day=int(day)-1
    url="http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0C700&stname=%25E4%25B8%25AD%25E5%25A3%25A2&datepicker="
    url=url+str(year)+"-"+str(mon)+"-"+str(day)
    # print(url)
    response = requests.get(url)
    # 一般python會自動編成big5，網頁的utf-8會變亂碼
    response.encoding = 'utf-8'
    # 解析HTML,lxml解析器速度較html.parser快
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
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
            # print(title)
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
                    # print(value)
                weather[d[0]] = d[1::]
                # print(type(weather.items()))
                # print("Json:", json.dumps(weather, indent=4, sort_keys=True))
                # # 轉換非數字的欄位
    tempt=[]
    for v in weather.values():
            num = v.count('T')
            while (num > 0):
                i = v.index('T')
                v[i] = '0.1'
                num = num - 1
            num1 = v.count('X')
            while (num1 > 0):
                for k in weather.keys():
                    a=weather[k]
                    a=[-9999 if x == "X" else x for x in a]
                    weather[k]=a  
                break                  
            num2 = v.count('')
            while (num2 > 0):
                for k in weather.keys():
                    a=weather[k]
                    a=[-9999 if x == '' else x for x in a]
                    weather[k]=a
                break
            num3 = v.count('...')
            while (num3 > 0):
                for k in weather.keys():
                    a=weather[k]
                    a=[-9999 if x == "..." else x for x in a]
                    weather[k]=a
                break
            if weather["Temperature"] == []:
                nonstn.append(st)
            else:
                tempt.append(weather["Temperature"])
    temp=tempt[0]
    for i in range(len(temp)):
        if temp[i] == '/':
            temp[i]=temp[i-1]
        else:    
            temp[i]=float(temp[i])
        # print(temp)

#-------------------------------------------------------------------------------

    y=[]
    for i in range(0,24): #將x逐一帶入f(x)，並存進矩陣
        y.append(temp[i]) #y軸資料

    n=24
    x=np.zeros((n-2,1), dtype=np.float) #v先建立f''(x)的矩陣
    b=np.zeros((n-2,1), dtype=np.float)  #建立公式18.37右式的值的矩陣
    h=np.zeros((n-2,n-2), dtype=np.float) #公式18.37左式的係數

    s=[]
    c=np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0,22.0,23.0,24.0])
    h1=c[1]-c[0]
    h[0,0]=4*h1 #第一列的值[4h,h,0,0...]
    h[0,1]=h1
    for i in range(1,n-2):  #將除了第一列和最後一列的值存進矩陣(帶狀矩陣)
        for j in range(0,n-3):
            if i==j:  #如果是對角線，就存入4h,對角線兩側存h
                h[i,j]=h1*4
                h[i,j+1]=h1
                h[i,j-1]=h1
    h[n-3,n-3]=4*h1 #最後一列的值
    h[n-3,n-4]=h1
    #print(h)
    for k in range(0,n-2):  #計算課本公式18.37等號右邊的值，存進b矩陣
        b[k,0]=(6/(h1))*(y[k+2]-y[k+1])+(6/(h1))*(y[k]-y[k+1])

#-----------------高斯賽德法，解f''(x)----------------------
    n=22
    lam=1.2
    es=0.05*100
    imax=10
    for i in range(0,n): #要算出x1
        dum=h[i,i]
    for j in range(0,n):
        h[i,j]=h[i,j]/dum
        b[i,0]=b[i,0]/dum
    #print(h,b)
    for i in range(0,n):  #第一次迭代
        sum=b[i,0]
        for j in range(0,n):
            if i!=j:
                sum=sum-h[i,j]*x[j,0]
            x[i,0]=sum
    iter=2
    #print("\nitem=%d\n"%(iter-1),"\n",x)
    while True: #無限迭代
        s=1
        for i in range(0,n):
            old=x[i,0]  #將x[i,0]存入old
            sum=b[i,0]  #一樣
            for j in range(0,n): #算x1,x2,x3
                if i!=j:
                    sum=sum-h[i,j]*x[j,0]
            x[i,0]=lam*sum+(1-lam)*old #relaxation
  
            if s==1 and x[i,0]!=0:  #確認ea值和es的大小
                ea=abs((x[i,0]-old)/x[i,0])*100
                if ea>es:
                    s=0
            ea=abs((x[i,0]-old)/x[i,0])*100  #計算ea
            #print("\nitem=%d\n"%iter,x,"\nea%d="%i,ea)
        iter=iter+1
        if s==1 or iter>imax: #如果ea<es或超過次數就停止
            break
    d=[0.0] #要插入f''(x)第一項和最後一項的矩陣，因為兩端點的f''(x)=0
    x= np.insert(x,0,values=d,axis= 0) #插入矩陣
    x= np.insert(x,n+1,values=d,axis= 0)
    #print("x=\n",x,'\n',temp)

    def f1(g): #定義公式18.36
        return ((x[i,0]/(6*h1))*((c[i+1]-g)**3)) +((x[i+1,0]/(6*h1))*((g-c[i])**3)) +(((y[i]/h1)-((x[i,0]*h1)/6))*(c[i+1]-g)) +(((y[i+1]/h1)-((x[i+1,0]*h1)/6))*(g-c[i]))
    sumf=[]
    suma=[]
    for i in range(0,n+1): #畫圖
        a=np.linspace(c[i],c[i+1],50) #從c[i]到c[i+1]生成很多個數的等間隔數列
        f=f1(a)
        for j in range(0,50,1):
            sumf.append(f[j])
            suma.append(a[j])#一段一段帶入上面100個數

        #plt.plot(a,f) #畫圖
        #print(sum)
        #plt.ylim(-0.5,1)
        #plt.legend()
        #plt.show
    #print(sum1,sum2)
    for j in range(0,24,1):
        if temp[j]==max(temp):
            i=j
        if temp[j]==min(temp):
            k=j
        
    if i==0:
        maxi=temp[i]
    elif i==23:
        maxi=temp[i]
    else:
        t0=temp[i-1]
        t1=temp[i]
        t2=temp[i+1]
        x3=(t0*((i+1)**2-(i+2)**2)+t1*((i+2)**2-i**2)+t2*(i**2-(i+1)**2))/(2*t0*((i+1)-(i+2))+2*t1*((i+2)-i)+2*t2*(i-(i+1)))
        maxi=f1(x3)
    
    if k==0:
        maxi=temp[k]
    elif k==23:
        maxi=temp[k]
    else:
        t0=temp[k-1]
        t1=temp[k]
        t2=temp[k+1]
        x3=(t0*((k+1)**2-(k+2)**2)+t1*((k+2)**2-k**2)+t2*(k**2-(k+1)**2))/(2*t0*((k+1)-(k+2))+2*t1*((k+2)-k)+2*t2*(k-(k+1)))
        i=k
        mini=f1(x3)
    return suma,sumf,maxi,mini
#print(suma)
