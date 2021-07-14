#Q3.13

#a=float(input('輸入a,(a不可小於0)=')) #輸入a
def square_root(a):
 es=(0.5*10**(2-16))/100 #es的值
 x=1  #x0的位置，可填任意數字，這裡填1
 while True: #無限迴圈
   xold=x #x回傳至xold，這樣才可計算ea
   x=(x+(a/x))/2  #迭代公式
   print('a的平方根=',x)
   ea=((x-xold)/x) #ea的值
   print('ea=',ea)
   if abs(ea)<es: #ea的絕對值小於es就跳出迴圈
     break
