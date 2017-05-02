start_minute=int(input("분에 대한 숫자를 입력하십시오 : "))
year=start_minute/60/24/365 # 년 -> 월 -> 일 -> 시 -> 분
year_to_days=float(year)-int(year) 
days=year_to_days*365
days_to_hours=float(days)-int(days)
hours=days_to_hours*24
hours_to_minutes=float(hours)-int(hours)
end_minute=hours_to_minutes*60
print("%d분은 약 %d년 %d일 %d시간 %d분 입니다." %(start_minute, year, days, hours, end_minute))