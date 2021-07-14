#Q6.30
import numpy as np
h=3 #用3比較可以接近真實的解，用其他數字也可
hold=3 #初始值存到hold以便下個迴圈計算ea
n=0
while n<3:
  h=h-((((np.pi)*(h**2)*((3*3-h)/3))-30)/(2*h*(np.pi)*3-(np.pi)*h**2)) #牛頓-拉瑟福法的公式，課本有
  ea=abs(((h-hold)/h))*100 #ea的值
  print('h=','{:<19}'.format(h),'ea=',ea)
  hold=h #將h的值存到hold以便下個迴圈計算ea
  n+=1 #n=n+1繼續下個迴圈