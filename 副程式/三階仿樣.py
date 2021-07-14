
#Q18.29(b)
import numpy as np
import math
import matplotlib.pyplot as plt

def f(t):
  return (np.sin(t))**2
c=np.linspace(0,(math.pi)*2,8) #x_axis從0到pi生成8個數的等間隔數列
y=[]
for i in range(0,8): #將x逐一帶入f(x)，並存進矩陣
  y.append(f(c[i]))


x=np.array([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0]]) #v先建立f''(x)的矩陣
n=8
b=np.zeros((n-2,1), dtype=np.float)  #建立公式18.37右式的值的矩陣
h=np.zeros((n-2,n-2), dtype=np.float) #公式18.37左式的係數

s=[]
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
n=6
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
  return ((x[i,0]/(6*h1))*((c[i+1]-g)**3)) +((x[i+1,0]/(6*h1))*((g-c[i])**3)) +(((y[i]/h1)-((x[i,0]*h1)/6))*(c[i+1]-g)) +(((y[i+1]/h1)-((x[i+1,0]*h1)/6))*(g-c[i]))

for i in range(0,n+1): #畫圖
  a=np.linspace(c[i],c[i+1],100) #從c[i]到c[i+1]生成很多個數的等間隔數列
  f=f1(a) #一段一段帶入上面100個數
  #print(f)
  plt.plot(a,f,label=str(i)) #畫圖

plt.ylim(-0.5,1)
plt.legend()
plt.show
  