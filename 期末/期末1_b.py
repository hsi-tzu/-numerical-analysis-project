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

def ff_fc(T,T_Z,n):
 fc=[]
 s=[]
 t=[]
 for i in range(1,n-1):
   fc.append((T[i+1]-T[i-1])/((T_Z[i+1]-T_Z[i])*2))
 s.append(abs(fc[0])) #將a[i,0]加入s矩陣
 t.append(0)
 #print(s[0])
 for j in range(1,n-2):
    if abs(fc[j])>abs(s[0]): #如果同一列有數大於s[i](同一列第一個被加進去的數)，較大的就取代之，直到s矩陣是每一列最大的數
      s[0]=(fc[j])
      t[0]=(j+1)
 print("微分絕對值最大值fc=",s[0],"i=",t[0],"h=%d~%d"%(h[t[0]-1],h[t[0]+1]))
   
ff_fc(e_147,h,17)
ff_fc(e_156,h,17)
ff_fc(e_165,h,17)
ff_fc(e_180,h,17)
ff_fc(w_170,h,17)
ff_fc(w_155,h,17)
ff_fc(w_140,h,17)
ff_fc(w_125,h,17)
ff_fc(w_110,h,17)
ff_fc(w_95,h,17)