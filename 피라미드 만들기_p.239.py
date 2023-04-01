# 반복문으로 피라미드 만들기

n = int(input("피라미드의 높이를 정해주세요 > "))+1
count = ""

# i는 피라미드 층 
# j는 공백의 개수
# k는 *의 개수

for i in range(1, n):
    for j in range(i, n-1):
        count += " "
    for k in range(0, 2*i-1):
        count += "*"
    count += '\n'

print(count)