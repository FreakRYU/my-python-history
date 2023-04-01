# 리스트나 딕셔너리가 중첩되어 있다면, 반복문을 두 번 적용해야 한다.

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"   
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str:
        print("{0} : {1}".format(key, character[key]))

    elif type(character[key]) is dict:
        for key_1 in character[key]:  # 키 변수를 다르게 해준다.
            print("{0} : {1}".format(key_1, character[key][key_1]))

    elif type(character[key]) is list:
        for elemant in character[key]:
            print("{0} : {1}".format(key, elemant))
    else: # int 자료형이 여기로 빠짐.
        print("{0} : {1}".format(key, character[key]))