sortednumber = list(input("세 숫자를 입력하세요 : ").split())
sortednumber = [float(x) for x in sortednumber]
def displaySortedNumbers(sortednumber):
    sortednumber.sort()
displaySortedNumbers(sortednumber)
num1 = sortednumber[0]
num2 = sortednumber[1]
num3 = sortednumber[2]
print("정렬된 숫자는 {0} {1} {2} 입니다.".format(num1, num2, num3))