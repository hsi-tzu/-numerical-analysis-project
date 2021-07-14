import numpy as np
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


#-------------------------牛頓內插
print("\n牛頓內插")
def new(a,b,c,d,e,f,g,h,k):
 y=np.array([a,b,c,d])
 x=np.array([e,f,g,h])
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
   xterm=xterm*(k-x[order-1])  #計算(x-x0),(x-x0)(x-x1).....
   #print(x[order-1])
   yint2=yint[order-1]+fdd[0,order]*xterm #計算fn(x)
   ea.append(yint2-yint[order-1]) #算誤差
   yint.append(yint2) #將yint2存入yint
 print(yint[n-1])
 
new(h[8],h[9],h[10],h[11],e_147[8],e_147[9],e_147[10],e_147[11],20)
new(h[8],h[9],h[10],h[11],e_156[8],e_156[9],e_156[10],e_156[11],20)
new(h[8],h[9],h[10],h[11],e_165[8],e_165[9],e_165[10],e_165[11],20)
new(h[8],h[9],h[10],h[11],e_180[8],e_180[9],e_180[10],e_180[11],20)
new(h[8],h[9],h[10],h[11],w_170[8],w_170[9],w_170[10],w_170[11],20)
new(h[8],h[9],h[10],h[11],w_155[8],w_155[9],w_155[10],w_155[11],20)
new(h[8],h[9],h[10],h[11],w_140[8],w_140[9],w_140[10],w_140[11],20)
new(h[8],h[9],h[10],h[11],w_125[8],w_125[9],w_125[10],w_125[11],20)
new(h[8],h[9],h[10],h[11],w_110[8],w_110[9],w_110[10],w_110[11],20)
new(h[8],h[9],h[10],h[11],w_95[8],w_95[9],w_95[10],w_95[11],20)
#拉格朗日內插
print("拉格朗日")
def lar(x2,x1,n,xx):
    y=[]
    x=[]
    for i in range(8,12):
        y.append(x1[i])
        x.append(x2[i])
    s=0
    p=0
    for i in range(0,n):
        p=y[i]
        #print(p)
        for j in range(0,n):
            if i!=j:
                if x[i]==x[j]:
                    p=p*((xx-x[j])/0.0001)
                else:
                    #print(x[i],x[j])
                    p=p*((xx-x[j])/(x[i]-x[j]))
                    #print(p)
        s=s+p
    large=s
    print(large)
lar(e_147,h,4,20)
lar(e_156,h,4,20)
lar(e_165,h,4,20)
lar(e_180,h,4,20)
lar(w_170,h,4,20)
lar(w_155,h,4,20)
lar(w_140,h,4,20)
lar(w_125,h,4,20)
lar(w_110,h,4,20)
lar(w_95,h,4,20)
