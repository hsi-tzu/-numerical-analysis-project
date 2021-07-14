#11.13
import numpy as np
a=np.array([[-8.0,1.0,-2.0],[2.0,-6.0,-1.0],[-3.0,-1.0,7.0]])
b=np.array([[-20.0],[-38.0],[-34.0]])
x=np.array([[0.0],[0.0],[0.0]])
x1=np.array([[0.0],[0.0],[0.0]])
n=3
lam=1.2
es=0.05*100
imax=10
for i in range(0,n): #要算出x1
  dum=a[i,i]
  for j in range(0,n):
   a[i,j]=a[i,j]/dum
  b[i,0]=b[i,0]/dum
#print(a,b)
for i in range(0,n):  #第一次迭代
  sum=b[i,0]
  for j in range(0,n):
    if i!=j:
      sum=sum-a[i,j]*x[j,0]
    x[i,0]=sum
iter=2
print("\nitem=%d\n"%(iter-1),"\n",x)
while True: #無限迭代
  s=1
  print("\nitem=%d\n"%iter)
  for i in range(0,n):
    old=x[i,0]  #將x[i,0]存入old
    sum=b[i,0]  #一樣
    for j in range(0,n): #算x1,x2,x3
      if i!=j:
        sum=sum-a[i,j]*x[j,0]
    x[i,0]=lam*sum+(1-lam)*old #relaxation
  
    if s==1 and x[i,0]!=0:  #確認ea值和es的大小
     ea=abs((x[i,0]-old)/x[i,0])*100
     if ea>es:
       s=0
    ea=abs((x[i,0]-old)/x[i,0])*100  #計算ea
    print("ea%d="%i,ea)
  print(x)
  iter=iter+1
  if s==1 or iter>imax: #如果ea<es或超過次數就停止
    break
#-------------------------------------------------------------
print("\n沒有Use overrelaxation")
for i in range(0,n): #要算出x1
  dum=a[i,i]
  for j in range(0,n):
   a[i,j]=a[i,j]/dum
  b[i,0]=b[i,0]/dum
#print(a,b)
for i in range(0,n):  #第一次迭代
  sum=b[i,0]
  for j in range(0,n):
    if i!=j:
      sum=sum-a[i,j]*x[j,0]
    x[i,0]=sum
iter=2
print("\nitem=%d\n"%(iter-1),"\n",x)
while True: #無限迭代
  s=1
  print("\nitem=%d\n"%iter)
  for i in range(0,n):
    old=x[i,0]  #將x[i,0]存入old
    sum=b[i,0]  #一樣
    for j in range(0,n): #算x1,x2,x3
      if i!=j:
        sum=sum-a[i,j]*x[j,0]
    x[i,0]=sum   #直接代sum進去
  
    if s==1 and x[i,0]!=0:  #確認ea值和es的大小
     ea=abs((x[i,0]-old)/x[i,0])*100
     if ea>es:
       s=0
    ea=abs((x[i,0]-old)/x[i,0])*100  #計算ea
    print("ea%d="%i,ea)
  print(x)
  iter=iter+1
  if s==1 or iter>imax: #如果ea<es或超過次數就停止
    break