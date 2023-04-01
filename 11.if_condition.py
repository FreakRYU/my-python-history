# p. 157 / 03. 조건문
# 1. 불 자료형과 if 조건문
# Boolean은 불린 또는 불리언으로 발음한다.
# 불은 오직 True(참)와 False(거짓) 값만 가질 수 있다.
print('# 1. 불 자료형과 if 조건문')

print(True)
# 출력값 : True
print(False)
# 출력값 : False

print() 
#------------------------------------------------------------------------#
# 2. 불 만들기: 비교 연산자
# 숫자 비교 뿐만 아니라 문자열도 비교 가능하다.
print('# 2. 불 만들기: 비교 연산자')

print("가방"=="가방")
print("가방"!="하마")
print("가방"<"하마")
# 출력값 : True /이유: 사전 순서로 가방이 하마보다 앞에 있음.
print("가방">"하마")
# 출력값 : False
print()

# 2+. 범위구하기
x=25
print(10<x<30)
print(40<x<60)

print()
#------------------------------------------------------------------------#
# 3. 불 연산하기: 논리 연산자
# not / 아니다 / 불을 반대로 전환한다.
# and / 그리고 / 피연산자가 두 개가 모두 참일 때 True, 나머지는 모두 False
# or  /  또는  / 피연산자 두 개 중 하나만 참이면 True, 두 개 모두 거짓이면 False
print('# 3. 불 연산하기: 논리 연산자')

print(not True)
# 출력값 : False
print(not False)
# 출력값 : True

# 3-1. not 연산자 조합하기 
x=10
under_20=x<20                       
print("under_20:", under_20)
print("not under_20:", not under_20)  # not under_20 = x > 20 이 된다.
print()

# 3-2. and 연산자와 or 연산자
print(True and False)
# 출력값 : False / 이유 : 둘 중 하나가 False 이기 때문
print(True or False)
# 출력값 : True / 이유 : 둘 중 하나가 True가 있기 때문

print()
#------------------------------------------------------------------------#
# 4. if 조건문이란?
print('# 4. if 조건문이란?')

# 예시
if True:
    print("True입니다...!")
    print("정말 True입니다...!")

if False:
    print("False입니다...!")
# 출력값 : 아무것도 없음 / 이유 : if 뒤에 불 값이 거짓(False)이기 때문

# 4-1. 조건문의 기본 사용
number=input("정수 입력> ")
number=int(number) # 변수 number 값을 정수로 바꿈으로써 다시 갱신

if number>0:
    print("양수입니다")

if number<0:
    print("음수입니다")

if number==0:
    print("0입니다")

print()
#------------------------------------------------------------------------#
# 5. 날짜/시간 활용하기

# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now=datetime.datetime.now()

# 오전 구분
if now.hour<12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

# 오후 구분
if now.hour>12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

print()
#------------------------------------------------------------------------#
# 6. 짝수와 홀수 구분하기
number=input("정수 입력> ")

last_character=number[-1]

last_character=int(number[-1])

if last_character==0\
    or last_character==2\
    or last_character==4\
    or last_character==6\
    or last_character==8:
    print("짝수입니다")