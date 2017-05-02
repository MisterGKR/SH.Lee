from math import sqrt
a, b, c = input("a, b, c를 입력하십시오 : ").split()
a=float(a)
b=float(b)
c=float(c)
d=b**2-4*a*c
if d>0:
    print("실근이 있습니다.")
    r1=(-b+sqrt(d))/2*a
    r2=(-b-sqrt(d))/2*a
    print("실근의 값은 %0.5f %0.5f 입니다." %(r1, r2))
elif d==0:
    r3=(-b+sqrt(d))/2*a
    print("실근의 값은 %f 입니다." %(r3))
else:
    print("이 방정식은 실근이 없습니다.")