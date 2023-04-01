# try except 구문을 이용해서 예외 발생하지 않게 코드 실행하기
numbers = [52, 273, 32, 103, 90, 10 ,275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
numbers = 10000
try:
    print("- {}는 {} 위치에 있습니다.".format(numbers, numbers.index(numbers)))

except:
    print("- 리스트 내부에 없는 값입니다.")
print()

print("--- 정상적으로 종료되었습니다. ---")