
#Q10.8
import numpy as np
a=np.array([[15.0,-3.0,-1.0],[-3.0,18.0,-6.0],[-4.0,-1.0,12.0]])
a0=np.array([[15.0,-3.0,-1.0],[-3.0,18.0,-6.0],[-4.0,-1.0,12.0]])
a1=np.array([[15.0,-3.0,-1.0],[-3.0,18.0,-6.0],[-4.0,-1.0,12.0]])
b1=np.array([[3300.0],[1200.0],[2400.0]])
b2=np.array([[0.0],[0.0],[0.0]])
b3=np.array([[3300.0],[1200.0],[2400.0]])
x=np.array([[30.0],[63.0],[73.0]])
x2=np.array([[30.0],[63.0],[73.0]])
x0=np.array([[30.0],[63.0],[73.0]])
o=[]
s=[]
ai=[]
n=3
er=0
tol=0.05
for i in range(0,n):
  o.append(i)  #將i加入o矩陣
  s.append(abs(a[i,1])) #將a[i,0]加入s矩陣
  for j in range(1,n):
    if abs(a[i,j])>s[i]: #如果同一列有數大於s[i](同一列第一個被加進去的數)，較大的就取代之，直到s矩陣是每一列最大的數
      s[i]=abs(a[i,j])

for k in range(0,n-1):
  p=k
  big=abs(a[k,k]/s[k]) #pivot=對角線數/最大值
  for l in range(k+1,n): #從下一列開始比較(k+1列)，找pivot最大的列
    dummy=abs(a[l,k]/s[l]) #假設dum=某列的值/某列最大值
    if dummy>big:  #如果dum>big，即某列值/最大值>原列值/最大值
      big=dummy #pivot值改成dum
      p=l #p由k列改成l
    c=o[p]  #o矩陣互換
    o[p]=o[k]
    o[k]=c
  if abs(a[k,k]/s[k])<tol: #確定每一列pivot係數不為0，若為0則停止
    er=-1
    print(a[k,k/s[k]]) 
    break
  for i in range(k+1,n): #LU矩陣
    f=(a[i,k])/(a[k,k]) #pivot要的乘a21/a11
    a[i,k]=f #L矩陣
    for j in range(k+1,n):
      a[i,j]=a[i,j]-((a[k,j])*f) #U矩陣

if abs(a[k,k]/s[k])<tol:  #確定每一列pivot係數不為0，若為0則停止
  er=-1
  print([k,k]/s[k])
#print(a)
if er==0:  #下三角矩陣求逆矩陣
  for i in range(0,n):
    for j in range(0,n):#使b矩陣第一次為1.0.0第二次為0.1.0，依此類推
      if i==j:  
        b2[j,0]=1
      else:
        b2[j,0]=0
    #print(b2)

    for k in range(1,n): #求d1,d2,d3的值
      sum=b2[k,0]  #從第二式開始算d2
      for j in range(0,k):
        sum=sum-(a[k,j]*b2[j,0]) #依序算出d2.d3
        
      b2[k,0]=sum #將d存入b2
    #print(b2)
#----------------------------------------------------
    x[2,0]=(b2[2,0]/a[2,2])
    #print("x2=",x[2,0])
    for k in range(1,-1,-1): #用上三角矩陣算出x的值
      s=0
      for j in range(k+1,n):
        s+=(a[k,j]*x[j,0])
    
      x[k]=(b2[k,0]-s)/a[k,k]


    for j in range(0,n):#x存入a0矩陣，a0為逆矩陣
      a0[j,i]=x[j]
else:
  print("ill")
print("[a]^-1=\n",a0)
#---------------------------------------------------------
for i in range(0,3): #用U矩陣和D矩陣算出x
  x1=0
  for j in range(0,3):
    x1=x1+a0[i,j]*b1[j,0]
    x0[i,0]=x1
print("x=\n",x0)

#------------------------------------------------------
#第3小題
x0[0,0]=x0[0,0]+10 #令c1=c1+10

for i in range(0,3):
  x1=0
  for j in range(0,3): #算出第三式的 the rate of mass input to reactor 3
    x1=x1+a1[i,j]*x0[j,0] 
    b3[i,0]=x1
print("b=\n",b3)
print("%dg/day"%(b3[2,0]-b1[2,0]))
#-----------------------------------------------------
#第4小題
b1[0,0]=b1[0,0]-700
b1[1,0]=b1[1,0]-350
for i in range(0,3):
  x1=0
  for j in range(0,3):
    x1=x1+a0[i,j]*b1[j,0] #算出 the concentration in reactor 3 be reduced
    x2[i,0]=x1
print("x=\n",x2)
print("%fg/m^3"%(x2[2,0]-x0[2,0]))