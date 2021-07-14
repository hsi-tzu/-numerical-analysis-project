import math #導入math函式
import matplotlib.pyplot as plt #導入matplotlib.pyplot函式
import numpy as np #導入numpy函式

def taylor_exp():

 es=(0.5*10**(2-16)) #es的定義，n=16,有16位有效位數(依照跑出來的有效位數去算的)

 x_axis=np.linspace(0.2,1,50) #x_axis從0.2到1生成50個數的等間隔數列
 ans,ansold=0,0
 def factorial(n): #定義階乘
   factor = 1 #第一項
   for i in range(1,n+1): ##從1開始到n+1
     factor *= i #就是f=f*i 
   return factor #回傳factor

 def taylor(x,n): #定義cos泰勒展開式
  
   s=(((-1)**n)*(np.exp(-0.2))*((x-0.2)**n))/(factorial(n)) #s=cos的泰勒展開
   return s #回傳s
  
 for i in range(4):  #設定4個迴圈
  
   ans+=taylor(x_axis,i) #ans=ans+taylor，taylor(x_axis,i)為第i階生成50個數，是矩陣型態
   ansold=ans  #ans的值存到ansold
   et=abs(((np.exp(-1)-ansold))/(np.exp(-1)))  #et=(exp的-1次方-ansold)/exp的-1次方 的絕對值
   print("order=",i,"value=",ansold[49],"et=",et[49]) #印出order和value和et,[49]為取出矩陣的第49項(0~49的49)
   plt.plot(x_axis,ans,label=str(i)) #畫圖，每一條畫出ans和x_axis以及order(i)的標籤label，共有0.1.2.3，共4條
 plt.plot(x_axis,1/np.exp(x_axis),'k',label='Ture') #畫出真值的圖，為e^-x
 plt.ylim(0,1.2) #y軸範圍0~1.2
 plt.legend() #顯示圖例
 plt.show() #顯示圖
taylor_exp()