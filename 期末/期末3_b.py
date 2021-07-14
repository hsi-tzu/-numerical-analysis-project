import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg

x = np.array([30.0, 27.0, 35.0, 13.0, 20.0, 10.0, 25.0, 47.0, 26.0, 38.0, 38.0, 23.0, 40.0, 39.0, 23.0, 33.0, 31.0, 20.0, 37.0, 44.0])
x1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y = np.array([2.7, 1.9, 5.5, 0.6, 0.7, 0.3, 1.4, 38.9, 1.7, 9, 8.9, 1, 12.5, 10.4, 1.1, 4.1, 3.2, 0.8, 7.8, 23.8])
def bubblesort(data,y):
    # 定義資料長度
    n = len(data)
    for i in range(n-2):                   # 有 n 個資料長度，但只要執行 n-1 次
        for j in range(n-i-1):             # 從第1個開始比較直到最後一個還沒到最終位置的數字 
            if data[j] > data[j+1]:        # 比大小然後互換
                data[j], data[j+1] = data[j+1], data[j]
                y[j],y[j+1]=y[j+1],y[j]

bubblesort(x,y)
#print(x)
def good(co2,year,n):
  #x的長度
 #for no in range(2,6):
 no=9  #階數-1
 a=np.zeros((n,no), dtype=np.float)
 at=np.zeros((no,n), dtype=np.float)
 y=np.zeros((n,1), dtype=np.float)


 for i in range(0,n):
         a[i,0]=1
         a[i,1]=year[i]
         if (no>2):
             for j in range(0,n):
                 for k in range(2,no):
                     a[j,k]=year[j]**(k)
        
         #print(a)
         for l in range(0,n): #L的轉置矩陣=U矩陣
             y[l,0]=co2[l]
             for j in range(0,no):
                 at[j,l]=a[l,j]
    
 z=at.dot(a)
 b=at.dot(y)
 x0=(np.linalg.inv(z)).dot(b)
 yr=a.dot(x0)
 #print(x0)
 plt.plot(year,yr)
 plt.scatter(year,co2,s=2,label="true",color="r") #畫原本的點
 plt.legend() #顯示圖例
 plt.show
good(y,x,20)

