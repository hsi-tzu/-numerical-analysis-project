import numpy as np
import matplotlib.pyplot as plt
path='./buoy.txt'
with open(path,'r')as f:
  data=f.readline()  #讀掉第一行的T(C)
  datab=f.read().split(",")  #讀之後的全部資料，並用空白鍵把每個資料做分割

h=[]
e_147=[]
e_156=[]
e_165=[]
e_180=[]
w_170=[]
w_155=[]
w_140=[]
w_125=[]
w_110=[]
w_95=[]

for i in range(0,187,11):
  h.append(float(datab[i]))
  e_147.append(float(datab[i+1]))
  e_156.append(float(datab[i+2]))
  e_165.append(float(datab[i+3]))
  e_180.append(float(datab[i+4]))
  w_170.append(float(datab[i+5]))
  w_155.append(float(datab[i+6]))
  w_140.append(float(datab[i+7]))
  w_125.append(float(datab[i+8]))
  w_110.append(float(datab[i+9]))
  w_95.append(float(datab[i+10]))
  
  #cubic spline
def cubic(kk,T,T_Z,n,o1,o2,o3):
 y=[]
 c=[]
 for i in range(0,n): #將x逐一帶入f(x)，並存進矩陣
   y.append(T[i])
   c.append(T_Z[i])
 x=np.zeros((n,1), dtype=np.float) #v先建立f''(x)的矩陣
 b=np.zeros((n-2,1), dtype=np.float)  #建立公式18.37右式的值的矩陣
 h=np.zeros((n-2,n-2), dtype=np.float) #公式18.37左式的係數

 s=[]
 h1=c[1]-c[0]

 h[0,0]=2*(c[2]-c[0]) #第一列的值[4h,h,0,0...]
 h[0,1]=c[2]-c[1]
 for i in range(1,n-2):  #將除了第一列和最後一列的值存進矩陣(帶狀矩陣)
   for j in range(0,n-3):
     if i==j:  #如果是對角線，就存入4h,對角線兩側存h
       h[i,j]=(c[j+3]-c[j+1])*2
       h[i,j+1]=c[j+3]-c[j+2]
       h[i,j-1]=c[j+2]-c[j+1]
 h[n-3,n-3]=2*(c[16]-c[14]) #最後一列的值
 h[n-3,n-4]=c[15]-c[14]
 #print(h)
 for k in range(0,n-2):  #計算課本公式18.37等號右邊的值，存進b矩陣
   b[k,0]=(6/(c[k+2]-c[k+1]))*(y[k+2]-y[k+1])+(6/(c[k+1]-c[k]))*(y[k]-y[k+1])

#-----------------高斯賽德法，解f''(x)----------------------
 n=n-2
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
#print("x=\n",x,c)

 def f1(g): #定義公式18.36
   return ((x[i,0]/(6*(c[i+1]-c[i])))*((c[i+1]-g)**3)) +((x[i+1,0]/(6*(c[i+1]-c[i])))*((g-c[i])**3)) +(((y[i]/(c[i+1]-c[i]))-((x[i,0]*(c[i+1]-c[i]))/6))*(c[i+1]-g)) +(((y[i+1]/(c[i+1]-c[i]))-((x[i+1,0]*(c[i+1]-c[i]))/6))*(g-c[i]))
 
 for i in range(0,n+1): #畫圖
   a=np.linspace(c[i],c[i+1],100) #從c[i]到c[i+1]生成很多個數的等間隔數列
   f=f1(a) #一段一段帶入上面100個數
  #print(f)
   #title=str(T)
   list=["147E","156E","165E","180E","170W","155W","140W","125W","110W","95W"]
   #print(list[0])
   plt.title(list[kk])
   plt.subplot(o1,o2,o3)
   plt.plot(f,a) #畫圖
 plt.show
 
cubic(0,e_147,h,17,2,5,1)
cubic(1,e_156,h,17,2,5,2)
cubic(2,e_165,h,17,2,5,3)
cubic(3,e_180,h,17,2,5,4)
cubic(4,w_170,h,17,2,5,5)
cubic(5,w_155,h,17,2,5,6)
cubic(6,w_140,h,17,2,5,7)
cubic(7,w_125,h,17,2,5,8)
cubic(8,w_110,h,17,2,5,9)
cubic(9,w_95,h,17,2,5,10)
