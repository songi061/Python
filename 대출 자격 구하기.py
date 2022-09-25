salary = int(input("연봉 ? :"))
job_term = int(input("근무 기간? : "))
if salary >= 40000000:
    if job_term >= 2:
        print("대출 자격 있음")
    else:
        print("재직기간 2년 이상 필요")
else:
    print("연봉 4천만 이상 필요")
