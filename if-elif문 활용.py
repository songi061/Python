score = int(input("점수를 입력하시오 : "))
if score >= 90 :
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else :
    grade = 'F'
print("등급은 ", grade, "입니다")
