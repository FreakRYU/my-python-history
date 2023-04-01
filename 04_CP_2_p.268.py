# 염기 서열을 입력했을 때 각각의 염기가 몇개 포함되어 있는지 세는 프로그램을 구현하라.
# 염기는 A(아데닌), T(티민), G(구아닌), C(사이토신)

# 깔끔한 코드는 아닌듯
dna = input("염기 서열을 입력주세요: ")

counter = {}

# 놀랍게도 for문을 이용하면 문자열에서도 한글자씩 꺼낼 수 있다.
for string in dna:
    if string not in counter:
        counter[string] = 0
    counter[string] += 1

for key in counter:
    print("{0}의 개수: {1}".format(key, counter[key]))

