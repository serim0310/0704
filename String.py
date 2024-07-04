# hello_world = "엄마가 말했다. '밥 먹었니?'"
# print(hello_world)
#
name = "정세림"
# print("안녕하세요. " + name + " 님, 반갑습니다.")
#
# money = 100
# print("입력하신 금액은", money, "원 입니다.")

# 데이터 출력 시 % 기호 사용하는 방법
print("안녕하세요. 저의 이름은 %s입니다." % name)

money = 10000
print("입력하신 금액은 %d원 입니다." % money)

# 문자열 길이 구하기
hello_world = "엄마가 말했다. '밥 먹었니?'"
print(len(hello_world))

# 문자열 슬라이싱
a = "집에 가고싶다."
print(len(a))
print(a[0:2])

# 문자열 치환
date = "2024.07.04"
date = date.replace(".", "-")
print(date)

#  문자열 여러 줄 출력하기
a = "집에 가고싶다. 눕고 싶어요. \n오늘 저녁은 꼭 치킨을 먹어야 힘이 날 것 같아요. 그리고 누워서 유튭 보다가 잠들고 싶"
print(a)