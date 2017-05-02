c = int(input("ASCII 코드 문자를 입력하십시오 :"))
if 0<c<128:
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(c)))
else:
    print("0 미만의 숫자나 128 이상의 숫자는 사용할 수 없습니다.")