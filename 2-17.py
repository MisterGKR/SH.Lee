weightpd=float(input("몸무게를 파운드로 입력하세요 : "))
heightinch=float(input("키를 인치로 입력하세요 : "))
weightkg=weightpd*0.45359237
heightm=heightinch*0.0254
BMI=weightkg/heightm**2
print("BMI는 %f 입니다." %(BMI))