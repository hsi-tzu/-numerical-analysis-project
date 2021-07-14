
import math #導入math函式
import click #導入click函式
#a= int(click.prompt('輸入es計算需要的有效位數(按enter用預設值):',default=16)) #輸入a值，用click.prompt設定預設值16
#maxit =int(click.prompt('請輸入maxit(按enter用預設值)：',default=100))    #輸入maxit的值，用click.prompt設定預設值100
#x= float(click.prompt("輸入x(角度)(按enter用預設值):",default=60))      #輸入x的值，用click.prompt設定預設值60

def maclaurin_cos(a,maxit,x):
 x= (x*math.pi/180) #x弧度轉角度

 es=(0.5*10**(2-a))  #es的公式
 print('es=',es)  #印出es
 ans,ansold=0,0
 def factorial(n): #定義階乘

   f=1       #第一項
   for i in range(1,n+1): #從1開始到n+1
     f*=i  #就是f=f*i 
   return f  #回傳f
  
 def taylor(x,n): #定義cos泰勒展開式
 
   return ((-1)**n)*(x**(2*n))/(factorial(2*n))  #回傳cos的展開 

 for n in range(maxit):  #迴圈，maxit為輸入值，要跑幾次迴圈
   ans+=taylor(x,n)  #ans=ans+taylor(x,n)
   ea=abs(((ans-ansold)/(ans))*100)  #ea=(現在的值-先前的值)/現在的值 的絕對值
   et=abs(((ans-math.cos(x))/ans)*100) #et=(現在的值-真的值)/真的值 的絕對值
   if ea==100:  #如果ea=1
     print('n=',n+1,'true=',math.cos(x),'approximation=',ans,'\t\tea(%)=nan\t\t','et(%)=',et) #印出如前的數值
   else:     #否則
     print('n=',n+1,'true=',math.cos(x),'approximation=',ans,'ea(%)=',ea,'et(%)=',et)  #印出ea=ea的值,et=et的值
   if ea< es: #如果ea的絕對值小於es
     break #停止迴圈
   ansold=ans #令ans的數，存到ansold裡
maclaurin_cos(16,100,60)