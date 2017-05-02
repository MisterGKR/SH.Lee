pop=312032486
birth=(60*60*24*365)//7
death=(60*60*24*365)//13
immi=(60*60*24*365)//45
pd=birth+immi-death
y1=pop+pd
y2=pop+pd*2
y3=pop+pd*3
y4=pop+pd*4
y5=pop+pd*5
print("처음 인구는 %d 입니다." %(pop))
print("1년차 인구는 %d 입니다." %(y1))
print("2년차 인구는 %d 입니다." %(y2))
print("3년차 인구는 %d 입니다." %(y3))
print("4년차 인구는 %d 입니다." %(y4))
print("5년차 인구는 %d 입니다." %(y5))