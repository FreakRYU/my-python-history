# 10. 도전문제 
# 10-1. 구의 부피와 겉넓이
print('# 10-1. 구의 부피와 겉넓이')
pi=3.141592
r=int(input("구의 반지름을 입력해주세요: "))
V=(4/3)*pi*(r**3)
S=4*pi*(r**2)
string_a="=구의 부피는 {}입니다.".format(V)
string_b="=구의 겉넓이는 {}입니다.".format(S)
print(string_a)
print(string_b)
print()

# 10-2. 피타고라스의 정리
print('# 10-2. 피타고라스의 정리')
a=int(input("밑변의 길이를 입력해주세요: "))
b=int(input("높이의 길이를 입력해주세요: "))
c=((a**2)+(b**2))**(1/2)
answer="= 빗변의 길이는 {}입니다.".format(c)
print(answer)