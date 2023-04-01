# 결과값 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

# numbers 에서 요소를 하나씩 꺼낸다
for number in numbers:
    # output[]을 이용하여 리스트안에 리스트를 꺼낸다.
    # output[0]은 숫자들을 3으로 나눴을 때, 나머지가 1이어야 한다.
    # output[1]은 숫자들을 3으로 나눴을 때, 나머지가 2이어야 한다.
    # output[2]은 숫자들을 3으로 나눴을 때, 나머지가 0이어야 한다.
    output[number%3-1].append(number) # 요소의 순서는 0부터 시작

print(output)
