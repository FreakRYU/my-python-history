# 리스트를 조합하여 딕셔너리 만들기

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]]=value_list[i]

print(character)