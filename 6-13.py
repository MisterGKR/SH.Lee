import fractions
n = int(input("0 이상의 숫자를 입력하세요.: "))
def fraction_nsum(n):
    fractsum = 0
    if n == 1:
        return fractions.Fraction(1,n+1)
    else :
        for i in range(1,n+1):            
            m = fractions.Fraction(i,i+1)
            fractsum += m
        return fractsum 
print("i    m(i)")
for n in list(range(1,n+1)):
    print("%d    %0.4f" %(n, float(fraction_nsum(n))))