m,n = input("두 숫자를 입력합니다. : ").split()
m=int(m)
n=int(n)
def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
def lcm(m,n):
    return (m/gcd(m,n)) * (n/gcd(m,n)) * gcd(m,n)
print("gcd is %d" %(gcd(m,n)))
print("lcm is %d" %(lcm(m,n)))
