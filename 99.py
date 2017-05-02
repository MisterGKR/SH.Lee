x=int(input("입력받은 값의 구구단을 입력합니다. : "))
for y in range(1,10):
    print("{0} * {1} = {2}".format(x,y,x*y))