#Q5.5
import numpy as np
import math
import matplotlib.pyplot as plt

def root():
 x=np.linspace(0.5,1,50)  #在0.5~1區間建立50個點
 y1=(np.sin(x))-(x**3)  

 plt.plot(x,y1) #畫出x,y1的圖
 plt.axhline(0,color= 'r') #標示y=0的位置
 plt.show() #顯示圖
 def f(x):  #定義f(x)
   return (np.sin(x))-(x**3) #回傳(sin(x))-(x**3)
 es=2
 xl=0.5
 xrold=0
 xu=1
 while True:
   xr=(xl+xu)/2 #二分法
   ea=abs((xr-xrold)/xr)*100 #ea的值，沒什麼好說
   print('xu=','{:<6}'.format(xu),'xl=','{:<7}'.format(xl),'xr=','{:<9}'.format(xr),'f(xr)=','{:<22}'.format(f(xr)),'ea=',ea) #印出值
   if (f(xl)*f(xr))<0: #如果(f(xl)*f(xr))<0，則xu=xr
     xu=xr
   if (f(xl)*f(xr))>0: #如果(f(xl)*f(xr))>0，則xl=xr
     xl=xr
   if (f(xl)*f(xr))==0: #如果(f(xl)*f(xr))==0，則跳出迴圈
     break
   if ea<es: #如果 ea<es，也跳出迴圈
     break
   xrold=xr #令xrold=xr，以便接下來算ea
   
root()