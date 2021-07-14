#9.7
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,20,500) #在0~20生成500個數的等間隔數列
x2=0.5*x+9.5
x4=(1.02*x+18.8)/2

plt.plot(x,x2,label='0.5*x1+9.5') #畫出x2的線
plt.plot(x,x4,label='(1.02*x1+18.8)/2') #畫出x4的線
plt.legend() #顯示圖例
plt.show() #顯示圖

a11=0.5
a12=-1
a21=1.02
a22=-2
b1=-9.5
b2=-18.8
a=a11*a22-a12*a21 #行列式
print("行列式值=",a)
print("第c題:接近0，是ill-conditioned")

c2=((-18.8*0.5)-(1.02*-9.5))/((0.5*-2)-(-1*1.02)) #課本公式
c1=((a22*b1)-(a12*b2))/a  #課本公式
print("x1=",round(c1,2),"x2=",round(c2,2)) #取到小數第一位，不然很長
print("\nif a11=0.52")

x5=np.linspace(-20,20,500) #在0~20生成500個數的等間隔數列
x6=0.52*x5+9.5
x7=(1.02*x5+18.8)/2

plt.plot(x5,x6,label='0.52*x1+9.5') #畫出x6的線
plt.plot(x5,x7,label='(1.02*x1+18.8)/2') #畫出x7的線
plt.legend() #顯示圖例
plt.show() #顯示圖

e11=0.52
g=e11*a22-a12*a21 #行列式公式
print("行列式值=",g)
print("第e題:也是接近0，是ill-conditioned")

h2=((e11*b2)-(a21*b1))/g #課本公式
h1=((a22*b1)-(a12*b2))/g #課本公式
print("x1=",round(h1,2),"x2=",round(h2,2))