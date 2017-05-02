import fractions
n = int(input("0 이상의 숫자를 입력하세요.: "))
def fraction_1sum(n):
    fractsum = 0
    if n == 1:
        return fractions.Fraction(1,n)
    else :
        for i in range(1,n+1):            
            m = fractions.Fraction(1,i)
            fractsum += m
        return fractsum
print("1 / %d 까지 더했을 땐 %0.4f 입니다." %(n, float(fraction_1sum(n))))