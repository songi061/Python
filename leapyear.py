#윤년 판별하기 코드

year = int(input('연도를 입력하세요 : '))

#연수가 4로 나누어 떨어지고, 100으로 나누어 떨어지는 해는 평년으로 or 400으로 나누어지는 해는 윤년으로 한다.

is_leap_year = ((year % 4 == 0 ) and (year % 100 != 0) or (year % 400 == 0))

print(year, '년은 윤년입니까?', is_leap_year)
