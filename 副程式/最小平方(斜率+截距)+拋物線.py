#Q17.6
#(a)
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
y=np.array([1.0,1.5,2.0,3.0,4.0,5.0,8.0,10.0,13.0])
n=9
sumx=0
sumy=0
sumxy=0
sumx2=0
sumy2=0
st=0
sr=0

for i in range(0,9): #計算各種會用到的數值(課本公式)
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
x_axis=np.linspace(1,9,100)#x_axis從1到9生成100個數的等間隔數列
def f(x):  #定義y的回歸直線
  return a0+a1*x
for i in range(0,n): #畫圖
  plt.scatter(x[i],y[i]) #各個點
  plt.plot(x_axis,f(x_axis)) #回歸直線
plt.show

#----------------------------------------------------------------(b)

a=np.zeros((3,3), dtype=np.float)
b=np.zeros((3,1), dtype=np.float)
c=np.zeros((3,1), dtype=np.float)
a[0,0]=n
order=2
for i in range(0,order+1): #計算多項式回歸的矩陣值
  for j in range(0,i+1):
    k=i+j
    sum=0
    for l in range(0,n): #a矩陣的值
      sum=sum+x[l]**k
    a[i,j]=sum #插入a矩陣
    a[j,i]=sum
  sum=0
  for l in range(0,n): #b矩陣的值
    sum=sum+y[l]*(x[l]**(i))
  b[i,0]=sum #插入b矩陣

#LU消去--------------------
a1=np.zeros((3,3), dtype=np.float)
n=3
#Cholesky decomposition
for k in range(0,n):  #L矩陣
  for i in range(0,k):
    sum=0
    for j in range(0,i):  #課本的公式
      sum=sum+a[i,j]*a[k,j] 
    a[k,i]=(a[k,i]-sum)/a[i,i]
  sum=0
  for j in range(0,k):
    sum=sum+a[k,j]*a[k,j]
  a[k,k]=(a[k,k]-sum)**(1/2)
#print("L矩陣=\n",a)
for i in range(0,n): #L的轉置矩陣=U矩陣
  for j in range(0,n):
    h=a[j,i]
    a1[j,i]=a[i,j]
    a1[i,j]=h
#print("U矩陣=\n",a1)


b[0,0]=b[0,0]/a[0,0]
for k in range(1,n): #求d1,d2,d3的值
  sum=b[k,0]
  for j in range(0,k):
    sum=sum-a[k,j]*b[j,0]
  b[k,0]=sum/a[k,k]
#print("b=\n",b)



c[2,0]=(b[2,0]/a1[2,2])
for k in range(1,-1,-1): #用上三角矩陣算出x的值
     s=0
     for j in range(k+1,n):
       s+=(a1[k,j]*c[j,0])
    
     c[k]=(b[k,0]-s)/a1[k,k]
#print("a0,a1,a2=\n",c)
n=9
m=2
sr2=0
for i in range(0,n):  #計算多項式回歸的sr
  sr2=sr2+(y[i]-c[0]-c[1]*x[i]-c[2]*x[i]**2)**2 
syx2=sr2/(n-(m+1))
r=((st-sr2)/st)**(1/2)
print("標準差2=",sr2,"\n相關係數2=",r)
print("\n拋物線的相關性較高")
def f2(x):  #定義多項式迴歸的函數(課本公式)
  return c[0]+c[1]*x+c[2]*x**2
x_axis=np.linspace(1,9,100)#x_axis從1到9生成100個數的等間隔數列
for i in range(0,n): #畫拋物線
  plt.plot(x_axis,f2(x_axis))

plt.show