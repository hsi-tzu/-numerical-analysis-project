import numpy as np
s=[]
er=0
tol=0.05
d=[]
a=np.array([[1.0,2.0,-1.0],[5.0,2.0,2.0],[-3.0,5.0,-1.0]])
b=np.array([[2.0],[9.0],[1.0]])
x=np.array([[3.0],[3.0],[3.0]])  #x的值隨便設，反正之後會變
n=3
for i in range(0,n,1):
  s.append(abs(a[i,0])) #將a[i,0]加入s矩陣
  #print(s[i])
  for j in range(1,n):
    if abs(a[i,j])>s[i]: #如果同一列有數大於s[i](同一列第一個被加進去的數)，較大的就取代之，直到s矩陣是每一列最大的數
      s[i]=(abs(a[i,j]))
#eliminate
for k in range(0,n-1): #交換+前消
#pivot
  p=k  #p為列號
  big=abs(a[k,k]/s[k]) #pivot=對角線數/最大值
  for o in range(k+1,n): #從下一列開始比較(k+1列)，找pivot最大的列
    dummy=abs(a[o,k]/s[o]) #假設dum=某列的值/某列最大值
    if dummy>big:  #如果dum>big，即某列值/最大值>原列值/最大值
      big=dummy #pivot值改成dum
      p=o #p由k列改成o
  if p!=k:  #如果p不等於k:
    for m in range(k,n):#把第一列和下面的列數比較，若p不等於k則每一列元素和原本的互換，
      d=a[p,m] #a矩陣的互換
      a[p,m]=a[k,m]
      a[k,m]=d
    c=b[p,0]  #b矩陣互換
    b[p,0]=b[k,0]
    b[k,0]=c
    
    e=s[p]  #s矩陣互換
    s[p]=s[k]
    s[k]=e

  if abs(a[k,k]/s[k])<tol: #確定每一列pivot係數不為0，若為0則停止
    er=-1
    break
  
  for i in range(k+1,n):  #前消，使pivot equ以下每列第一項係數=0
    f=(a[i,k])/(a[k,k]) #pivot要的乘a21/a11
    #print(f)
    for j in range(k+1,n):
      a[i,j]=a[i,j]-((a[k,j])*f) #後式-前式*f(就是消去)
      #print(a)
    b[i]=b[i]-((b[k])*f)  #一樣消去
if abs(a[n-1,n-1]/s[n-1])<tol: #確定每一項pivot係數不接近0，若為0則停止
  er=-1
print("a=\n",a,"\n","b=\n",b)
if er!=-1: #替代

  #sub
  x[2,0]=(b[2,0]/a[2,2]) #先算出x3的值
  #print(x[2,0])
  for i in range(1,-1,-1):
    sum=0
    for j in range(i+1,n):
      sum=sum+a[i,j]*x[j,0] #把後項x帶入方程式
    x[i]=(b[i]-sum)/a[i,i]  #b扣掉其他的(sum)後除以係數，得到x

print("x=\n",x)