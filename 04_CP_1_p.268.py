# 1. 숫자의 종류
# 다음 리스트에서 몇 가지 종류의 숫자가 사용되었는지 구하는 프로그램을 작성하시오.
# [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

list = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dictionary = {}
count = 0

for number in list:
    if number in dictionary:
        dictionary[number] = dictionary[number] + 1
    else:
        dictionary[number] = 1

# 딕셔너리 자료형도 len()를 이용하여 키의 개수를 구할 수 있다.
print("""{0}에서
사용된 숫자의 종류는 {1}개 입니다.
참고: {2}""".format(list, len(dictionary), dictionary))