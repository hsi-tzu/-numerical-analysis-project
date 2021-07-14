#6.11
import numpy as np
x=int(input('enter 2,6,8=')) #輸入值
xold=x #將x存入xold以便計算第一次ea
es=(0.5*10**(2-16))
if x==6 or x==8: #如果輸入6或8就跑下面的迴圈，因為會一直跑所以要有對策
  i=0
  for i in range(5):#建立跑5次的迴圈，不然會一直跑
    x=x-(((np.exp(-0.5*x))*(4-x)-2)/(-2*(np.exp(-0.5*x))-(np.exp(-0.5*x))+0.5*x*(np.exp(-0.5*x)))) #將題目代入牛頓-拉瑟福法的公式，課本有
    ea=abs(((x-xold)/x))*100
    print('x=','{:<19}'.format(x),'ea=',ea)
    xold=x #將x的值存到xold以便下個迴圈計算ea
    if ea<es: #如果ea<es，則跳出迴圈
      break
    i=i+1 #i=i+1繼續下個迴圈
  print('f(x)微分趨近0，迭代發散')
else:
  while True:
    x=x-(((np.exp(-0.5*x))*(4-x)-2)/(-2*(np.exp(-0.5*x))-(np.exp(-0.5*x))+0.5*x*(np.exp(-0.5*x)))) #將題目代入牛頓-拉瑟福法的公式，課本有
    ea=abs(((x-xold)/x))*100
    print('x=','{:<19}'.format(x),'ea=',ea)
    xold=x #將x的值存到xold以便下個迴圈計算ea
    if ea<es: #如果ea<es，則跳出迴圈
      break