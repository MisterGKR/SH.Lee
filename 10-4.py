list_average = input("숫자들의 모임을 입력하세요 :").split()
list_average = [int(x) for x in list_average]
average=sum(list_average)/len(list_average)
print("%0.2f 이 평균일때" %(average))
for x in list_average:
    if int(x)>average:
        print("{0}은 평균보다 높습니다.".format(x))
    else:
        print("{0}은 평균보다 낮습니다.".format(x))