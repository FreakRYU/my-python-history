# random 모듈을 이용하여 csv 파일 만들기
import random
name = list("ABCDEFGHIJKLMNOPQRST")

파일 = open("human.txt", "w") # 파일을 열고 쓰기 모드로 전환
파일.write("이름,몸무게,키\n")
for i in range(1000):
    이름 = random.choice(name) + random.choice(name)
    몸무게 = random.randrange(40, 120)
    키 = random.randrange(140, 200)
    파일.write(f"{이름},{몸무게},{키}\n")
파일.close()

# 다시 파일을 열어서 BMI 분석하기
파일 = open("human.txt", "r")

for 한줄 in 파일:
    # 파일에서 색출한 한줄은 2행으로 구성되어 있다.
    # strip 함수로 양쪽 공백을 제거하여 1행으로 만들고
    # 그렇게 만든 한줄의 문자열을 split 함수를 이용해
    # 쉼표로 구분하여 리스트를 만들고 각 요소를 다중할당한다.
    이름,몸무게,키 = (한줄.strip().split(",")) 

    # 첫 번째 해더가 '이름,몸무게,키' 이므로 이를 무시해본다.
    if not 몸무게.isdigit(): # 몸무게 값이 숫자로 구성되어 있다면,
        continue # 조건문을 통과한다.
    몸무게 = int(몸무게)
    키 = int(키) # BMI 연산을 위해 몸무게, 키를 int 자료형으로 변환

    bmi = 몸무게 / (키 / 100) ** 2

    결과 = ""

    if 25 <= bmi:
        결과  = "과체중"
    elif 18.5 <= bmi:
        결과 = "정상체중"
    else:
        결과 = "저체중"

    print("\n".join([
        f"이름:{이름}",
        f"몸무게:{몸무게}",
        f"키:{키}",
        f"BMI:{bmi}",
        f"결과:{결과}",""
    ]))
파일.close()