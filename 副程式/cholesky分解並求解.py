
#Q11.5
import numpy as np
a=np.array([[6.0,15.0,55.0],[15.0,55.0,225.0],[55.0,225.0,979.0]])
a1=np.array([[6.0,15.0,55.0],[15.0,55.0,225.0],[55.0,225.0,979.0]])
x=np.array([[1.0],[1.0],[4.0]])
b=np.array([[152.6],[585.6],[2488.8]])
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
print("L矩陣=\n",a)
for i in range(0,n): #L的轉置矩陣=U矩陣
  for j in range(0,n):
    h=a[j,i]
    a1[j,i]=a[i,j]
    a1[i,j]=h
print("U矩陣=\n",a1)


b[0,0]=b[0,0]/a[0,0]
for k in range(1,n): #求d1,d2,d3的值
  sum=b[k,0]
  for j in range(0,k):
    sum=sum-a[k,j]*b[j,0]
  b[k,0]=sum/a[k,k]
print("b=\n",b)



x[2,0]=(b[2,0]/a1[2,2])
for k in range(1,-1,-1): #用上三角矩陣算出x的值
     s=0
     for j in range(k+1,n):
       s+=(a1[k,j]*x[j,0])
    
     x[k]=(b[k,0]-s)/a1[k,k]
print("a0,a1,a2=\n",x)