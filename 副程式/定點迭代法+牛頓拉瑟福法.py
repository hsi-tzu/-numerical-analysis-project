#6.3
#(a)Fixed-point iteration
import numpy as np
es=0.05
x=5
xold=5
print('Fixed-point iteration\n') #印出標題
while True:
  x=(1.8*x+2.5)**(1/2) #將原本的方程式移項得到這個式子 ,x0=5代入得新的x
  ea=abs(((x-xold)/x))*100 #ea的值
  print('x=','{:<19}'.format(x),'ea=',ea)
  xold=x #將x的值存到xold以便下個迴圈計算ea
  if ea<es: #如果ea<es，則跳出迴圈
    break
#(b)The Newton-Raphson program 
print('\nThe Newton-Raphson program\n') #印出標題
a=5
aold=5
while True:
  a=a-((-a**2+1.8*a+2.5)/(-2*a+1.8)) #將題目的方程式套入課本的公式
  ea2=abs(((a-aold)/a))*100 #ea的值
  print('x2=','{:<19}'.format(a),'ea2=',ea2)
  aold=a #將x的值存到xold以便下個迴圈計算ea
  if ea2<es: #如果ea<es，則跳出迴圈
    break