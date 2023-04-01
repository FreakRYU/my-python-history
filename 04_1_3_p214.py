# Created on iPad.

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# 짝수, 홀수 구분하기
for number in numbers:
    if number%2==0:
        print("{}는 짝수입니다.".format(number))
    else:
        print("{}는 홀수입니다.".format(number))

# 자릿수 세기
for number in numbers:
    print("{0}는 {1} 자릿수 입니다.".format(number, len(str(number))))