list1 = input("숫자들의 모임을 입력하세요 :").split()
list1 = [int(x) for x in list1]
list2 = set(list1)
print("중복을 제외한 숫자 : " + str(list2))