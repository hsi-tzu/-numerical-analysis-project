
#10.15
import numpy as np
import math 
a1=np.array([[1.0,4.0,9.0,16.0,25.0],[4.0,9.0,16.0,25.0,36.0],[9.0,16.0,25.0,36.0,49.0],[16.0,25.0,36.0,49.0,64.0],[25.0,36.0,49.0,64.0,81.0]])
a=np.array([[1.0,4.0,9.0,16.0,25.0],[4.0,9.0,16.0,25.0,36.0],[9.0,16.0,25.0,36.0,49.0],[16.0,25.0,36.0,49.0,64.0],[25.0,36.0,49.0,64.0,81.0]])
a0=np.array([[1.0,4.0,9.0,16.0,25.0],[4.0,9.0,16.0,25.0,36.0],[9.0,16.0,25.0,36.0,49.0],[16.0,25.0,36.0,49.0,64.0],[25.0,36.0,49.0,64.0,81.0]])
a2=np.array([[1.0,4.0,9.0,16.0,25.0],[4.0,9.0,16.0,25.0,36.0],[9.0,16.0,25.0,36.0,49.0],[16.0,25.0,36.0,49.0,64.0],[25.0,36.0,49.0,64.0,81.0]])
cond_a=np.array([[1.0,4.0,9.0,16.0,25.0],[4.0,9.0,16.0,25.0,36.0],[9.0,16.0,25.0,36.0,49.0],[16.0,25.0,36.0,49.0,64.0],[25.0,36.0,49.0,64.0,81.0]])
max=[]
max1=[]
b2=np.array([[0.0],[0.0],[0.0],[0.0],[0.0]])
x=np.array([[30.0],[63.0],[73.0],[73.0],[73.0]])
x1=np.array([[30.0],[63.0],[73.0],[73.0],[73.0]])
m=[]
m1=[]
o=[]
o1=[]
n=5
sum=0
tol=0.05
for i in range(0,n):
  s=0
  for j in range(0,n):
    s=s+a[i,j]
  m.append(s)
print("m=",m)
for i in range(0,n):
  max.append(abs(a[i,1]))
  for j in range(1,n):
    if abs(a[i,j])>max[i]:
      max[i]=abs(a[i,j])
#----------------------------------------------
for k in range(0,n-1):
  p=k
  big=abs(a[k,k]/max[k]) #pivot=對角線數/最大值
  for l in range(k+1,n): #從下一列開始比較(k+1列)，找pivot最大的列
    dummy=abs(a[l,k]/max[l]) #假設dum=某列的值/某列最大值
    if dummy>big:  #如果dum>big，即某列值/最大值>原列值/最大值
      big=dummy #pivot值改成dum
      p=l #p由k列改成l
  if abs(a[k,k]/max[k])<tol: #確定每一列pivot係數不為0，若為0則停止
    er=-1
    #print(a[k,k]/max[k]) 
    break
  for i in range(k+1,n): #LU矩陣
    f=(a[i,k])/(a[k,k]) #pivot要的乘a21/a11
    a[i,k]=f #L矩陣
    for j in range(k+1,n):
      a[i,j]=a[i,j]-((a[k,j])*f) #U矩陣


 #下三角矩陣求逆矩陣
for i in range(0,n):
  for j in range(0,n):#使b矩陣第一次為1.0.0第二次為0.1.0，依此類推
    if i==j:  
      b2[j,0]=1
    else:
      b2[j,0]=0

  for k in range(1,n): #求d1,d2,d3的值
    sum=b2[k,0]  #從第二式開始算d2
    for j in range(0,k):
     sum=sum-(a[k,j]*b2[j,0]) #依序算出d2.d3
        
    b2[k,0]=sum #將d存入b2

#----------------------------------------------------
  x[4,0]=(b2[4,0]/a[4,4])
    #print("x2=",x[2,0])
  for k in range(3,-1,-1): #用上三角矩陣算出x的值
     s=0
     for j in range(k+1,n):
       s+=(a[k,j]*x[j,0])
    
     x[k]=(b2[k,0]-s)/a[k,k]


  for j in range(0,n):#x存入a0矩陣，a0為逆矩陣
    a0[j,i]=x[j]

print("[a]^-1=\n",a0)

for i in range(0,n):
  s=0
  for j in range(0,n):
    s=s+abs(a0[i,j])
  o.append(s)
#print(o)
for i in range(4):
  for j in range(0,n-1):
    m[j]
    if m[j+1]<m[j]:
     h=m[j]
     m[j]=m[j+1]
     m[j+1]=h
    if o[j+1]<o[j]:
      h=o[j]
      o[j]=o[j+1]
      o[j+1]=h
cond=m[4]*o[4]
print("\ncond[a]=",cond,"  is bigger than 1,is ill-condition")
aa=math.log10(cond)
print("up to %d digit of precision will be lost due to ill-conditioning\n"%aa)
#----------------------------------------------------------





#print(a1,max)
for i in range(0,n):
  for j in range(0,n): 
    a1[i,j]=a1[i,j]/max[i]

for i in range(0,n):
  s=0
  for j in range(0,n):
    s=s+a1[i,j]
  m1.append(s)
print("m=",m1)
for i in range(0,n):
  max1.append(abs(a1[i,1]))
  for j in range(1,n):
    if abs(a1[i,j])>max1[i]:
      max1[i]=abs(a1[i,j])
#----------------------------------------------
for k in range(0,n-1):
  p=k
  big=abs(a1[k,k]/max1[k]) #pivot=對角線數/最大值
  for l in range(k+1,n): #從下一列開始比較(k+1列)，找pivot最大的列
    dummy=abs(a1[l,k]/max1[l]) #假設dum=某列的值/某列最大值
    if dummy>big:  #如果dum>big，即某列值/最大值>原列值/最大值
      big=dummy #pivot值改成dum
      p=l #p由k列改成l
  if abs(a1[k,k]/max1[k])<tol: #確定每一列pivot係數不為0，若為0則停止
    er=-1
    #print(a[k,k]/max[k]) 
    break
  for i in range(k+1,n): #LU矩陣
    f=(a1[i,k])/(a1[k,k]) #pivot要的乘a21/a11
    a1[i,k]=f #L矩陣
    for j in range(k+1,n):
      a1[i,j]=a1[i,j]-((a1[k,j])*f) #U矩陣


 #下三角矩陣求逆矩陣
for i in range(0,n):
  for j in range(0,n):#使b矩陣第一次為1.0.0第二次為0.1.0，依此類推
    if i==j:  
      b2[j,0]=1
    else:
      b2[j,0]=0

  for k in range(1,n): #求d1,d2,d3的值
    sum=b2[k,0]  #從第二式開始算d2
    for j in range(0,k):
     sum=sum-(a1[k,j]*b2[j,0]) #依序算出d2.d3
        
    b2[k,0]=sum #將d存入b2

#----------------------------------------------------
  x1[4,0]=(b2[4,0]/a[4,4])
    #print("x2=",x[2,0])
  for k in range(3,-1,-1): #用上三角矩陣算出x的值
     s=0
     for j in range(k+1,n):
       s+=(a1[k,j]*x1[j,0])
    
     x1[k]=(b2[k,0]-s)/a1[k,k]


  for j in range(0,n):#x存入a0矩陣，a0為逆矩陣
    a2[j,i]=x1[j]

print("[a]^-1=\n",a2)

for i in range(0,n):
  s=0
  for j in range(0,n):
    s=s+abs(a2[i,j])
  o1.append(s)
#print(o)
for i in range(4):
  for j in range(0,n-1):
    m1[j]
    if m1[j+1]<m1[j]:
     h=m1[j]
     m1[j]=m1[j+1]
     m1[j+1]=h
    if o1[j+1]<o1[j]:
      h=o1[j]
      o1[j]=o[j+1]
      o1[j+1]=h
cond=m1[4]*o1[4]
print("\ncond[a]=",cond,"  is bigger than 1,is ill-condition")
aaa=np.log10(cond)
print("up to %d digit of precision will be lost due to ill-conditioning\n"%aaa)