# 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수 만들기

# mul 함수를 생성하고, 괄호 안에 *로 가변 매개변수를 넣어준다.
def mul(*values):
    # mul 값을 1로 지정한다
    mul = 1
    # 전달된 값들을 for문으로 하나씩 꺼낸다.
    for value in values:
        # 꺼낸 값들을 mul = 1에 하나씩 곱한다
        mul *= value
    # 반복이 끝나고 mul()함수의 결과값으로 리턴해준다.
    return mul

print(mul(5, 7, 9, 10))
