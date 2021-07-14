#5.18
import numpy as np
import math
#o=int(input('enter o(8,10,12)=')) #輸入值
#tu=40+273.15 #題目給的值
#tl=0+273.15

def osf_two(o,tu,tl):
 Ea=0.05
 n=np.log(40/0.05)/np.log(2) #需迭代次數的公式，課本有
 print('需迭代次數n=',math.ceil(n)) #印出無條件進位的n
 print('\n') #空一行
 def osf(o,ta):  #定義兩未知數的函數
   return -139.34411+((1.575701*(10**5))/ta-(6.642308*10**7)/ta**2+(1.243800*10**10)/ta**3-(8.621949*10**11)/(ta**4))-np.log(o)  #回傳值，公式課本有
 n=0
 while True:
   tr=(tl+tu)/2 #二分法
   Ea2=tu-tl #Ea的值
   print('n=','{:<2}'.format(n),'tl(℃)=','{:<12}'.format(tl-273.15),'tu(℃)=','{:<12}'.format(tu-273.15),'tr(℃)=','{:<12}'.format(tr-273.15),'Ea=','{:<12}'.format(Ea2)) #印出值
   if (osf(o,tl)*osf(o,tr))<0: #如果(osf(o,tl)*osf(o,tr))<0，則tu=tr
     tu=tr
   if (osf(o,tl)*osf(o,tr))>0: #如果(osf(o,tl)*osf(o,tr))>0，則tl=tr
     tl=tr
   if (osf(o,tl)*osf(o,tr))==0: #如果(osf(o,tl)*osf(o,tr))==0，則跳出迴圈
     break
   if Ea2<0.05: #如果Ea2<0.05，則跳出迴圈
     break
   n+=1 #n=n+1繼續下個迴圈
   
osf_two(8,40+273.15,0+273.15)