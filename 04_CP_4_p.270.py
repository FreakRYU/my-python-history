# 2차원 리스트 평탄화 작업

# 입력한 리스트는 자료형이 문자열이므로, 결국 문자열의 필요한 것들을 색출해야 함.
# 모든 대괄호 


list_a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
list_b = []

for element in list_a:
    if type(element) == list:
        for i in element:
            list_b.append(i)
    else:
        list_b.append(element)
                

print("""{0}를 평탄화하면
{1}입니다.""".format(list_a,list_b))
