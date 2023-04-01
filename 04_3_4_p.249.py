max_value = 0
a = 0
b = 0

# continue 키워드를 이용하여 반복문 사용
# i * j의 값이 이전의 max_value보다 작거나 같으면, 무시하고 반복 진행

n = int(input("숫자를 정해주세요 > "))

for i in range(1, n+1):
    j = n - i
    if i*j <= max_value:
        continue
    else:
        max_value = i * j
        a = i
        b = j

print("최대가 되는 경우: {0} * {1} = {2}".format(a, b, max_value))





# max_value = 0
# a = 0
# b = 0

# a, b, max 값에 대한 리스트를 생성하고
# sort()를 이용하여 차순으로 전개 후, 특정 인덱스에 해당되는 값을 색출

# dictionary = {}
# list_max_value = []
# n = int(input("숫자를 정해주세요 > "))

# for i in range(1, n+1):
#    j = n - i
#    list_max_value.append(i*j)
#    dictionary[i*j]=i

#list_max_value.sort()
#max_value = list_max_value[-1]
#a = dictionary[max_value]
#b = n - a
#print("최대가 되는 경우: {0} * {1} = {2}".format(a, b, max_value))