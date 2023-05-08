# 문자열 연결 연산자: +
# 방법 : "문자열" + "문자열"
print("안녕"+"하세요")
print("안녕하세요"+"!")

# 만약 문자열과 숫자를 (+)연산자를 이용하여 출력한다면?
print("안녕하세요"+1)
# TypeErro: can only concatenate str (not "int") to str
# 번역 : 문자끼리만 연결할 수 있고 숫자와 연결이 불가능하다는 의미.

# 따라서 숫자도 큰따옴표를 이용하여 문자열로 변환시켜줘야 한다.
print("안녕하세요"+"1")

#------------------------------------------------------------------------#
# 문자열 반복 연산자: *
# (*)를 사용하면 문자열을 숫자만큼 반복할 수 있다.
print("안녕하세요"*5)

#------------------------------------------------------------------------#
# 문자 선택 연산자(인덱싱): []
# 문자 선택 연산자는 문자열 내부의 문자 하나를 선택하는 연산자임.
# 제로 인덱스: 0부터 셈  <- 파이썬이 이용하는 유형임.
# 원 인덱스: 1부터 셈
print("문자 선택 연산자")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

# 대괄호 안에 숫자를 음수(-1, -2, -3, -4...)로 입력하면 역순이 됨.
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

#------------------------------------------------------------------------#
# 문자열 범위 선택 연산자(슬라이싱): [:]
print("안녕하세요"[1:4])
# 출력값 : 녕하세
# 파이썬은 '마지막 숫자를 포함하지 않음'으로 적용함.
# 따라서 [1:4]이면 1번째+2번째+3번째 글자까지만 추출됨. 

print("안녕하세요"[1:])
# 출력값 : 녕하세요
# 0 / 1 2 3 4 번째만 선택

print("안녕하세요"[:3])
# 출력값 : 안녕하
# 0 1 2 번째만 선택/ 3 4

# [] 연산자를 이용해 문자열의 특정 위치에 있는 문자를 참조하는 것을 인덱싱이라 함.
# [:] 연산자를 이용해 문자열의 일부를 추출하는 것을 슬라이싱이라 함.

#------------------------------------------------------------------------#
# IndexError(index out of range) 예외
# 리스트/문자열의 수를 넘는 요소/글자를 선택할 때 발생.
print("안녕하세요"[10])