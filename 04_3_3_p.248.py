limit = 10000
i = 1

sum_value = 0

while sum_value < limit:
    # limit 되기 전에도 더함
    sum_value = sum_value + i
    # 위 코드 이후 limit 를 넘었으므로 while 반복문 실행 종료
    i += 1

print("{0}를 더할 때 {1}을 넘으며 그때의 값은 {2}입니다.".format(i-1, limit, sum_value))

    


#print("{0}를 더할 때 {1}을 넘으며 그때의 값은 {2}입니다.".format())