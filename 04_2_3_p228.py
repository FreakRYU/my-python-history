# Created on iPad.

print ('Hello World!')

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    # number가 counter에 있다면, 대응 값을 +1 카운트한다.
    if number in counter:
        counter[number]=counter[number]+1
    # 만약 number가 counter에 없다면 number를 키로 정의하고
    # 그 값은 1부터 시작한다.
    else:
        counter[number]=1
print(counter) 