def main():
    ch1=int(input("첫번째 ASCII 코드번호를 입력합니다 : "))
    ch2=int(input("두번째 ASCII 코드번호를 입력합니다 : "))
    numberPerLine=int(input("얼마만큼 띄울건지를 결정합니다. : "))
    if 47<ch1<123:
        if 47<ch2<123:
            printChars(ch1,ch2,numberPerLine)
        else:
            print("47과 123 사이의 숫자를 입력합니다.")
    else:
        print("47과 123 사이의 숫자를 입력합니다.")
def printChars(ch1,ch2,numberPerLine):
    for i in range(ch1,ch2+1,numberPerLine):
        print(chr(i), end='')
        if i%10==7 and numberPerLine==1:
            print("\n")
        elif i%20==6 and numberPerLine==2:
            print("\n")
        elif i%10==5 and numberPerLine==3:
            print("\n")
        elif i%40==4 and numberPerLine==4:
            print("\n")
        elif i%50==43 and numberPerLine==5:
            print("\n")
        elif i%60==42 and numberPerLine==6:
            print("\n")
        elif i%70==41 and numberPerLine==7:
            print("\n")
        else:
            continue
main()
