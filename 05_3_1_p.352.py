# 자주 틀림

numbers = [1, 2, 3, 4, 5, 6]


print("::".join(list(map(str, numbers))))

# map 함수를 이용하여 리스트의 요소들을 하나씩 꺼내어 str()을 이용해 자료형을 문자열로 변환해준다.
# 꺼낸 요소들은 이터레이터 이므로 list 함수를 사용하여 list로 바꿔준다.
# '구분자'.join(리스트)는 리스트의 요소를 일렬로 나열하여 문자열로 바꾸어준다. 요소 사이에는 구분자가 첨가된다.