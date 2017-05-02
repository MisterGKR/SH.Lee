import time
a=int(time.time()%1000000000)
h=int(a%100)
if 64<h<91:
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h)))
elif 55<=h<65:
    h_1=h+10
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_1)))
elif 45<=h<55:
    h_1=h+20
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_1)))
elif 35<=h<45:
    h_1=h+30
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_1)))
elif 25<=h<35:
    h_1=h+40
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_1)))
elif 15<=h<25:
    h_1=h+50
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_1)))
elif 5<=h<15:
    h_1=h+60
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_1)))
elif 0<=h<5:
    h_1=h+70
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_1)))
elif h>90:
    h_2=h-10
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h_2)))
else:
    print("해당하는 ASCII 문자는 %c 입니다." %(chr(h)))