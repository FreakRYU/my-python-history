# lambda 함수를 이용하여 짧게 작성

numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda i : i % 2 == 1, numbers )))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x : 3 <= x < 7, numbers)))
print()

print("제곱해서 50미만 추출하기")
print(list(filter(lambda x : x * x <50, numbers)))
