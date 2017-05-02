temp = float(input("화씨 -58도와 41도 사이의 온도를 입력하십시오. :"))
if temp>=41:
    print("41도 이상은 측정할 수 없습니다.")
elif temp<=-58:
    print("-58도 이하는 측정할 수 없습니다.")
else:
    v = float(input("풍속을 시간 당 마일 단위로 입력하십시오. :"))
    if v<3:
        print("3 이상의 풍속을 입력해야 합니다.")
    else:
        twc=35.74+(0.6215*temp)-(35.75*(v**0.16))+(0.4275*temp*(v**0.16))
        print("체감온도는 %f ℉입니다." %(twc))