# 1 ~ 100 사이에 있는 숫자 중 2진수로 변환했을 때
# 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드를 만드시오. 

output = [number for number in range(1, 101) if "{:b}".format(number).count("0")==1]


for i in output:
    print("{0} : {1}".format(i, "{:b}".format(i)))
print("합계:", sum(output))
