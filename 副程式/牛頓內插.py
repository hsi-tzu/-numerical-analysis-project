
#Q18.6
def f1(y1,y0,x1,x0): #定義方程式,才不用一直寫一些很複雜的東西
  return (y0-y1)/(x0-x1)
 #將對應數字帶入課本公式18.15和18.17
 
#first order"
print("x0=3,x1=5")
x0=3
y0=19
f10=f1(99,19,5,3)
f21=f1(6,99,2,5)
f1_4=y0+(4-x0)*f10
f210=f1(f10,f21,3,2)
r1=f210*(4-3)*(4-5)
print("f1(4)=",f1_4,"R1=",r1)

#second order
print("\nx0=2,x1=3,x2=5")
f2_4=6+(4-2)*f1(6,19,2,3)+(4-2)*(4-3)*f1(f1(6,19,2,3),f1(19,99,3,5),2,5)
f21=f1(99,19,5,3)
f10=f1(19,6,3,2)
f210=f1(f21,f10,5,2)
f32=f1(291,99,7,5)
f321=f1(f32,f21,7,3)
f3210=f1(f321,f210,7,2)
r2=f3210*(4-3)*(4-5)*(4-2)
print("f2(4)=",f2_4,"R2=",r2)

#third order
print("\nx0=2,x135,x2=5,x3=7")
f3_4=6+(4-2)*f10+(4-2)*(4-3)*f210+(4-2)*(4-3)*(4-5)*f3210
f43=f1(444,291,8,7)
f432=f1(f43,f32,8,5)
f4321=f1(f432,f321,8,3)
f43210=f1(f4321,f3210,8,2)
r3=f43210*(4-2)*(4-3)*(4-5)*(4-7)
print("f3(4)=",f3_4,"R3=",r3)

#fourth order
print("\nx0=2,x135,x2=5,x3=7,x4=8")
f4_4=6+(4-2)*f10+(4-2)*(4-3)*f210+(4-2)*(4-3)*(4-5)*f3210+(4-2)*(4-3)*(4-5)*(4-1)*f43210
f54=f1(3,444,1,8)
f543=f1(f54,f43,1,7)
f5432=f1(f543,f432,1,5)
f54321=f1(f5432,f4321,1,3)
f543210=f1(f54321,f43210,1,0)
r4=f543210*(4-2)*(4-3)*(4-5)*(4-7)*(4-8)
print("f3(4)=",f4_4,"R3=",r3)