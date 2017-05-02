value = input("10진수를 입력합니다. : ")
value = int(value)
def decimalToBinary(value):
    return bin(value)
print("2진수로 변환하면 %s 가 됩니다." %decimalToBinary(value))