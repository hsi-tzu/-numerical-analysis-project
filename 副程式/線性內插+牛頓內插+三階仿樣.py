#Q18.28
import numpy as np
print("exact result is 7.986 \n")
# linear interpolation
print("linear interpolation")
f1=8.418+((7.305-8.418)/(32-24))*(27-24) #線性內插的公式
print(f1)

#牛頓內插
print("\n牛頓內插")
y=np.array([11.843,9.870,8.418,7.305])
x=np.array([8,16,24,32])
yint=[]
ea=[]
n=4
fdd = np.zeros((n,n), dtype=np.float)

for i in range(0,n):
  fdd[i,0]=y[i] #將f(x)存入fdd
#print(fdd)
for j in range(1,n):
  for i in range(0,n-j):
    fdd[i,j]=(fdd[i+1,j-1]-fdd[i,j-1])/(x[i+j]-x[i]) #計算係數,fdd[0,1]是f[x1,x0]依此類推
#print(fdd)
xterm=1
yint.append(fdd[0,0])
for order in range(1,n):
  xterm=xterm*(27-x[order-1])  #計算(x-x0),(x-x0)(x-x1).....
  #print(x[order-1])
  yint2=yint[order-1]+fdd[0,order]*xterm #計算fn(x)
  ea.append(yint2-yint[order-1]) #算誤差
  yint.append(yint2) #將yint2存入yint
print(yint[n-1])


#-----------------------------------------------------------------------------------
#cubic spline
y=np.array([11.843,9.870,8.418,7.305])
c=np.array([8,16,24,32])
x=np.array([[3.0],[3.0]])
n=4
b=np.zeros((n-2,1), dtype=np.float)
h=np.zeros((n-2,n-2), dtype=np.float)

s=[]
h1=8

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

for k in range(0,n-2):  #計算課本公式18.37等候右邊的值，存進b矩陣
  b[k,0]=(6/(h1))*(y[k+2]-y[k+1])+(6/(h1))*(y[k]-y[k+1])

#---------------高斯消去------------------
n=n-2
tol=0.05
er=0

for i in range(0,n,1):
  s.append(abs(h[i,0])) #將h[i,0]加入s矩陣
  #print(s[i])
  for j in range(1,n):
    if abs(h[i,j])>s[i]: #如果同一列有數大於s[i](同一列第一個被加進去的數)，較大的就取代之，直到s矩陣是每一列最大的數
      s[i]=(abs(h[i,j]))
#eliminate
for k in range(0,n-1): #交換+前消
#pivot
  p=k  #p為列號
  big=abs(h[k,k]/s[k]) #pivot=對角線數/最大值
  for o in range(k+1,n): #從下一列開始比較(k+1列)，找pivot最大的列
    dummy=abs(h[o,k]/s[o]) #假設dum=某列的值/某列最大值
    if dummy>big:  #如果dum>big，即某列值/最大值>原列值/最大值
      big=dummy #pivot值改成dum
      p=o #p由k列改成o
  if p!=k:  #如果p不等於k:
    for m in range(k,n):#把第一列和下面的列數比較，若p不等於k則每一列元素和原本的互換，
      d=h[p,m] #a矩陣的互換
      h[p,m]=h[k,m]
      h[k,m]=d
    c=b[p,0]  #b矩陣互換
    b[p,0]=b[k,0]
    b[k,0]=c
    
    e=s[p]  #s矩陣互換
    s[p]=s[k]
    s[k]=e

  if abs(h[k,k]/s[k])<tol: #確定每一列pivot係數不為0，若為0則停止
    er=-1
    break
  
  for i in range(k+1,n):  #前消，使pivot equ以下每列第一項係數=0
    f=(h[i,k])/(h[k,k]) #pivot要的乘a21/a11
    #print(f)
    for j in range(k+1,n):
      h[i,j]=h[i,j]-((h[k,j])*f) #後式-前式*f(就是消去)

    b[i]=b[i]-((b[k])*f)  #一樣消去
if abs(h[n-1,n-1]/s[n-1])<tol: #確定每一項pivot係數不接近0，若為0則停止
  er=-1
#print(b,h)
if er!=-1: #替代

  #sub
  x[n-1,0]=(b[n-1,0]/h[n-1,n-1]) #先算出x3的值
  #print(x[n-1,0])
  for i in range(n-2,-1,-1):
    sum=0
    for j in range(i+1,n):
      sum=sum+h[i,j]*x[j,0] #把後項x帶入方程式
    x[i,0]=(b[i,0]-sum)/h[i,i]  #b扣掉其他的(sum)後除以係數，得到x

#print("x=\n",x)
xi=32
xi_1=24
xx=27
h1=8
f_27=((x[1,0]/(6*h1))*(xi-xx)**3) +((0/(6*h1))*(xx-xi_1)**3) +(((y[2]/h1)-((x[1,0]*h1)/6))*(xi-xx)) +(((y[3]/h1)-((0*h1)/6))*(xx-xi_1)) #27在區間24~32將相應的數帶入課本公式18.36
print("\ncubic spline\n",f_27)