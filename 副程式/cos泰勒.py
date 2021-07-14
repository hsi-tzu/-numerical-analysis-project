import math #導入math函式
#x = float(input('請輸入x(x要小於2pi弧度)：'))#輸入x的值
def taylor_cos(x):
 x= (x*math.pi/180)
 es=(0.5*10**(2-16)) #es的定義，n=16,有16位有效位數(依照跑出來的有效位數去算的)
 print('es=',es)
 n=1 #第一項為n=1,開始進入迴圈
 while True: #無限迴圈
  
   def factorial(n): #定義階乘
     f=1       #第一項
     for i in range(1,n+1): #從1開始到n+1
       f*=i  #就是f=f*i
     return f  #回傳f
  
   def taylor(n): #定義cos泰勒展開式
     s=0  #s的初始值=0
     for k in range(n): #泰勒的迴圈
       s=s+((-1)**k)*(x**(2*k))/(factorial(2*k)) 
     return s #回傳s
   print('n=',n,'true=',math.cos(x),'approximation=',taylor(n)) #印出值

   ea=((taylor(n)-taylor(n-1))/taylor(n))*100  #ea=(現在的值-先前的值)/現在的值
   et=((taylor(n)-math.cos(x))/math.cos(x))*100 #et=(現在的值-真的值)/真的值
   if ea==1.0:  #如果ea=1
     print('ea=nan','et=',et) #印出ea=nan,et印出et的值
   else:     #否則
     print('ea=',ea,'et=',et)  #印出ea=ea的值,et=et的值
   n=n+1 #回傳n=n+1,讓迴圈往下一項跑
   if abs(ea)<es: #如果ea的絕對值小於es
     break #停止迴圈
print(taylor_cos(60))