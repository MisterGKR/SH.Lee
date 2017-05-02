value = input("10진수를 입력합니다. : ")
value = int(value)
def decimalTohex(value):
    return hex(value)
print("16진수로 변환하면 %s 가 됩니다." %decimalTohex(value))