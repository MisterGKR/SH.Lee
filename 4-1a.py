from math import sqrt
a ,b, c = input('a,b,c 숫자를 입력 : ').split()
a = float(a)
b = float(b)
c = float(c)
d = b**2 - 4*a*c
if d > 0:
    r1 = -b+sqrt(d)/(2*a)
    r2 = -b-sqrt(d)/(2*a)
    print("실근은 %0.5f %0.5f 입니다."%(r1,r2))
elif d == 0:
    r3=(-b+sqrt(d))/2*a
    print('실근은 %f 입니다.'%(r3))
else :
    print("실근을 갖지 않습니다.")