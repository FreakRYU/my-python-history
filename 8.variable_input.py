# 변수와 입력

# 변수 = 값 (값을 변수에 할당한다.)
# 숫자 + "문자열" -> 오류가 발생한다.

#------------------------------------------------------------------------#
# 1. 복합 대입 연산자
# ex) += : 숫자 덧셈 후 대입
#     -= : 숫자 뺄셈 후 대입  
#     *= : 숫자 곱셈 후 대입
#     /= : 숫자 나눗셈 후 대입  
#     %= : 숫자의 나머지를 구한 후 대입  
#    **= : 숫자 제곱 후 대입    

# 간단한 예제
number=100
number+=10
number+=20
number+=30
print("number:", number)
# 출력값 : number: 160
print()

# 문자열도 마찬가지이다.
string="안녕하세요"
string+="!"
string+="!"
print("string:", string)
# 출력값 : string: 안녕하세요!!
print()

#------------------------------------------------------------------------#
# 2. 사용자 입력: input()
input("인사말을 입력하세요>")
# 이때 괄호 안에 입력한 내용을 프롬프트 문자열 이라고 한다.
print()


string=input("인사말을 입력하세요>")
print(string)
print()

#------------------------------------------------------------------------#
# 3. input() 함수의 입력 자료형
# 대입한 값의 자료형은 type()를 사용하면 된다.
print(type(string))
print()

number=input("숫자를 입력하세요")
print(type(number))
print()

#------------------------------------------------------------------------#
# 4. 문자열을 숫자로 바꾸기
# input() 함수의 입력 자료형은 항상 문자열임.
# 따라서 입력받은 문자열을 숫자로 변환해야 숫자 연산에 활용할 수 있음.
# int() : 문자열을 int 자료형으로 변환한다.
# float() : 문자열을 float 자료형으로 변환한다.

# int() 함수 활용하기
string_a=input("입력A>")
int_a=int(string_a)

string_b=input("입력B>")
int_b=int(string_b)

print("문자열 자료:", string_a+string_b)
print("숫자 자료:", int_a+int_b)
print()

# int() 함수와 float() 함수 활용하기
output_a=int("52")
output_b=float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)
print()


#------------------------------------------------------------------------#
# 5. 숫자를 문자열로 바꾸기
# str(다른 자료형) -> 문자열
output_a=str(52) 
output_b=str(52.273)
print(type(output_a), output_a) 
print(type(output_b), output_b) 
print()

#------------------------------------------------------------------------#
# 6. 섭씨온도, 화씨온도 변환기
temperature=int(input("섭씨온도를 입력해주세요> "))
print((5/9)*(temperature-32),"℉")