list_1to100 = list(input("숫자를 입력하세요 : ").split())
if any([1>int(x) or int(x)>100 for x in list_1to100])==False:
    list_1to100b=list(set(list_1to100))
    for x in list(list_1to100b):
        list_1to100b.sort()
        print("{0} - {1} 번 나타납니다.".format(x, list_1to100.count(x)))
else:
    print("1과 100 사이의 정수만 입력받아야 합니다.")