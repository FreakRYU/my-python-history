# p.135 / 2-4 : 숫자와 문자열의 다양한 기능

#------------------------------------------------------------------------#
# 1. 문자열의 format() 함수
# 형태 : "{}".format(숫자)
# 숫자를 문자열로 바꾸어줌.
# 중괄호 개수 = 매개변수의 개수 (안 지켜지면, Index Error)
print('# 1. 문자열의 format() 함수')

string_a="{}".format(10)
print(string_a)
print(type(string_a))
print()

#------------------------------------------------------------------------#
# 2. format() 함수의 다양한 기능
print('# 2. format() 함수의 다양한 기능')
# 2-1. 정수를 특정 칸에 출력하기
output_a="{:d}".format(52) #정수

# 특정 칸에 출력하기 (n칸을 빈 칸으로 잡고 뒤에서부터 숫자를 채움.)
output_b="{:5d}".format(52) #5칸
output_c="{:10d}".format(52) #10칸

# 빈칸을 0으로 채우기 (위와 동일하나, 빈칸을 0으로 채움, 음수는 맨 앞에 -부호 채움)
output_d="{:05d}".format(52) #양수
output_e="{:05d}".format(-52) #음수

print("#기본")
print(output_a)
print("#특정 칸에 출력하기")
print(output_b)
print(output_c)
print("#빈칸을 0으로 채우기")
print(output_d)
print(output_e)
print()

#------------------------------------------------------------------------#
# 3. format, 기호 붙여 출력하기
print('# 3. format, 기호 붙여 출력하기')

output_a="{:+d}".format(10)
output_b="{:-d}".format(-10)
output_c="{: d}".format(10)
output_d="{: d}".format(-10)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

#------------------------------------------------------------------------#
# 4. =로 기호 위치 선정
print('# 4. =로 기호 위치 선정')

output_e="{:+5d}".format(10)   # 기호 뒤로 밀기 : 양수
output_f="{:+5d}".format(-10)  # 기호 뒤로 밀기 : 음수
output_g="{:=+5d}".format(10)  # 기호 앞으로 밀기 : 양수
output_h="{:=+5d}".format(-10) # 기호 앞으로 밀기 : 음수
output_i="{:+05d}".format(10)  # 0으로 채우기 : 양수
output_j="{:+05d}".format(-10) # 0으로 채우기 : 음수
# 0으로 채우게 되면, 기호는 알아서 앞으로 감.

print(output_e)
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print(output_j)
print()

#------------------------------------------------------------------------#
# 5. {:f}를 사용하여 부동 소수점 출력하기
print('# 5. {:f}를 사용하여 부동 소수점 출력하기')

output_k="{:f}".format(52.273)
output_l="{:15f}".format(52.273)
output_m="{:+15f}".format(52.273)
output_n="{:+015f}".format(52.273)

print(output_k)
print(output_l)
print(output_m)
print(output_n)
print()

#------------------------------------------------------------------------#
# 6. 소수점 아래 자릿수 지정하기
# "{:10.nf}".format() 이면 10칸을 잡고 소수점을 n자리로 출력한다. 이때 자동으로 반올림도 일어난다.
print('# 6. 소수점 아래 자릿수 지정하기')

output_o="{:15.3f}".format(52.273)
output_p="{:15.2f}".format(52.273)
output_q="{:15.1f}".format(52.273)

print(output_o)
print(output_p)
print(output_q)
print()

# 6+. 의미 없는 소수점 제거하기
print('# 6+. 의미 없는 소수점 제거하기')

print(type(0))   
print(type(0.0)) 
print()
# 0과 0.0은 파이썬으로 출력했을 때, 자료형이 내부적으로 다르다.
# 이때 의미없는 0을 제거한 후 출력하기 위해서 { :g}를 사용한다.

output_r=52.0
output_s="{:g}".format(output_r)
print(output_r)
print(output_s)
print()

#------------------------------------------------------------------------#
# 7. 대소문자 바꾸기: upper()와 lower()
print('# 7. 대소문자 바꾸기: upper()와 lower()')

a="Hello Python Programming...!"
a_up=a.upper()
a_low=a.lower()
print(a_up)
print(a_low)
print()

#------------------------------------------------------------------------#
# 8. 문자열 양옆의 공백 제거하기: strip()
# strip() : 문자열 양옆의 공백을 제거합니다.
# lstrip() : 문자열 왼쪽의 공백을 제거합니다.
# rstrip() : 문자열 오른쪽의 공백을 제거합니다.
print('# 8. 문자열 양옆의 공백 제거하기: strip()')

input_a="""
      안녕하세요
문자열의 함수를 알아봅니다
"""
print(input_a)
print()

print(input_a.strip())
print()

#------------------------------------------------------------------------#
# 9. 문자열 찾기: find()와 rfind()
# find() : 왼쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
# rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
print('# 9. 문자열 찾기: find()와 rfind()')

string_a="안녕안녕하세요".find("안녕")
print(string_a)

string_b="안녕안녕하세요".rfind("안녕")
print(string_b)
print()

#------------------------------------------------------------------------#
# 10. 문자열과 in 연산자
# 문자열 내부에 어떤 문자여링 있는지 확인하는 용도
# 출력은 True 또는 False로 나온다.
print('# 10. 문자열과 in 연산자')

print("안녕"in "안녕하세요")
print("잘자"in "안녕하세요")
print()

#------------------------------------------------------------------------#
# 11. 문자열 자르기 : split()
# 문자열을 특정한 문자로 자를 때는 split( )함수를 이용한다. 
# split() 괄호 안에 물자열인 공백(띄어쓰기)을 기준으로 자른다.
print("# 11. 문자열 자르기 : split()")
  
a="10 20 30 40 50".split(" ")
print(a)
# 실행 결과로 리스트가 출력된다.
