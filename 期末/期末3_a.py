import numpy as np
import matplotlib.pyplot as plt
x = np.array([30.0, 27.0, 35.0, 13.0, 20.0, 10.0, 25.0, 47.0, 26.0, 38.0, 38.0, 23.0, 40.0, 39.0, 23.0, 33.0, 31.0, 20.0, 37.0, 44.0])
y = np.array([2.7, 1.9, 5.5, 0.6, 0.7, 0.3, 1.4, 38.9, 1.7, 9, 8.9, 1, 12.5, 10.4, 1.1, 4.1, 3.2, 0.8, 7.8, 23.8])
n=20
sumx=0
sumy=0
sumxy=0
sumx2=0
sumy2=0
st=0
sr=0

for i in range(0,n): #計算各種會用到的數值(課本公式)
  sumx=sumx+x[i]  
  sumy=sumy+y[i]
  sumxy=sumxy+(x[i]*y[i])
  sumx2=sumx2+x[i]*x[i]
  sumy2=sumy2+y[i]*y[i]
xm=sumx/n  #x的平均(課本公式)
ym=sumy/n
a1=(n*sumxy-sumx*sumy)/(n*sumx2-sumx*sumx) #a1的值(課本公式)
a0=ym-a1*xm  #a0的值

for i in range(0,n): #計算st和sr
  st=st+(y[i]-ym)**2
  sr=sr+(y[i]-a1*x[i]-a0)**2

syx=(sr/(n-2))**(1/2) #計算S(y/x)
r=(n*sumxy-sumx*sumy)/(((n*sumx2-(sumx**2))**(1/2))*((n*sumy2-(sumy**2))**(1/2))) #計算r

print("標準差=",syx,"\n相關係數r=",r)
x_axis=np.linspace(9,50,100)#x_axis從1到9生成100個數的等間隔數列
def f(x):  #定義y的回歸直線
  return a0+a1*x
for i in range(0,n): #畫圖
  plt.scatter(x[i],y[i]) #各個點
  plt.plot(x_axis,f(x_axis)) #回歸直線
plt.show