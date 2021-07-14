
#Q17.9

import numpy as np
import matplotlib.pyplot as plt
x=np.array([0.4,0.8,1.2,1.6,2.0,2.3])
y=np.array([800.0,975.0,1500.0,1950.0,2900.0,3600.0])
z=np.array([800.0,975.0,1500.0,1950.0,2900.0,3600.0])
n=6
sx=0
sz=0
sx2=0
sxz=0
for i in range(0,n):  #將y取log變成z變成z
 z[i]=np.log(y[i])

for i in range(0,n):#計算各種會用到的數
  sx=sx+x[i]
  sz=sz+z[i]
  sx2=sx2+x[i]**2
  sxz=sxz+x[i]*z[i]
xm=sx/n
zm=sz/n
a1=a1=(n*sxz-sx*sz)/(n*sx2-sx*sx)
a0=zm-a1*xm

A1=np.exp(a0)  #將算出的a0取e會得到A1
B1=a1 #B1=a1
def f(x):  #定義函數(課本公式17.12)
  return A1*(np.exp(B1*x))
def f2(x):  #定義直線函數
  return a0+a1*x

x_axis=np.linspace(0.4,2.3,100) #x_axis從0.4到2.3生成100個數的等間隔數列
for i in range(0,n):#畫圖
  plt.subplot(121) #畫兩張圖-1
  plt.title("y=%f*e**(%f*x)"%(A1,B1)) #標題
  plt.scatter(x[i],y[i],color="r") #畫原本的點
  plt.plot(x_axis,f(x_axis)) #畫原本的函數
  plt.subplot(122) #畫兩張圖-2
  plt.title("y=%f+%f*x"%(a0,a1)) #標題
  plt.scatter(x[i],z[i],color="b") #畫線性化後的點
  plt.plot(x_axis,f2(x_axis)) #線性化後的線
plt.show
