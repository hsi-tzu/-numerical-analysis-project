#5.27
import numpy as np
import matplotlib.pyplot as plt
def false_position():
 def f(x): #定義函數f(x)
   return (x**10)-1 #回傳值
 es=0.01
 iu=0 #xu的次數
 il=0 #xl的次數
 n=1
 xl=0
 xu=1.3
 fl=f(xl)
 fu=f(xu)
 xrold=0
 ea2=[]
 et2=[]
 print('{:<3}'.format('n='),'{:<19}'.format('xl='),'{:<19}'.format('xu='),'{:<19}'.format('xr='),'{:<23}'.format('f(xr)='),'{:<23}'.format('ea(%)='),'{:<23}'.format('et(%)=')) #印出標題
 while True:
   xr=xu-(fu*(xl-xu)/(fl-fu)) #試位法公式
   fr=f(xr)
   ea=abs(((xr-xrold)/xr)*100)
   et=abs((1-xr)/1*100)
   ea2.append(ea) #將ea加入矩陣ea2
   et2.append(et) #將et加入矩陣et2
   xrold=xr #將xr的值存到xrold以便下個迴圈計算ea
   if f(xl)*f(xr)<0: #如果f(xl)*f(xr)<0
     xu=xr #將xr變成新的xu去計算
     fu=fr #一樣
     iu=0 #和下面兩行是計數，如果滿足f(xl)*f(xr)<0，iu=0，il=il+1
     il=il+1
     if il>=2: #如果il累加到>=2時，則fl=fl/2
       fl=fl/2
   if f(xl)*f(xr)>0: #如果f(xl)*f(xr)>0
     xl=xr #將xr變成新的xl去計算
     fl=fr #一樣
     il=0 #和下面兩行是計數，如果滿足f(xl)*f(xr)>0，il=0，iu=iu+1
     iu=iu+1
     if iu>=2:#如果iu累加到>=2時，則fu=fu/2
       fu=fu/2
   print('{:<3}'.format(n),'{:<19}'.format(xl),'{:<19}'.format(xu),'{:<19}'.format(xr),'{:<23}'.format(f(xr)),'{:<23}'.format(ea),'{:<19}'.format(et)) #印出值
   if ea<es or n>100: #如果ea<es or n>100則跳出迴圈
     break
   n=n+1 #n=n+1繼續下個迴圈

 x=np.linspace(0,n,n) #在0~1.3建立n個點(n=12)
 y1=ea2 #y1的座標=ea2
 y2=et2 #y2的座標=et2

 plt.plot(x,y1,label='ea') #畫出ea的線
 plt.plot(x,y2,label='et') #畫出et的線
 plt.legend() #顯示圖例
 plt.show() #顯示圖
 
false_position()