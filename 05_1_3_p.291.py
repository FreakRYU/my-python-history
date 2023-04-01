# 다음 중 오류가 발생하는 코드를 고르시오.
# 괄호 안에 지정한 매개변수와 호출한 함수의 매개변수 개수는 같아야 한다.

# 1
def fuction_1(*values, valueA, valueB): # 가변 매개변수 뒤에 매개변수가 오면 안된다.
    pass
# fuction_1의 전달값은 모두 가변 매개변수로 들어간다.
# 따라서 valueA 와 valueB 는 정의가 되지 않기 때문에 오류가 발생한다.
fuction_1(1, 2, 3, 4, 5)

# 2
def fuction_2(*values, valueA=10, valueB=20):
    pass
fuction_2(1, 2, 3, 4, 5)

# 3
def fuction_3(valueA, valueB, *value):
    pass
fuction_3(1, 2, 3, 4, 5)

# 4
def fuction_4(valueA=10, valueB=20, *values):
    pass
fuction_4(1, 2, 3, 4, 5)