# 삼각형 면적구하는 프로그램[
# 1. 밑변과 높이를 입력받는다.
# 2. 밑변과 높이를 곱한 후 2로 나눈다.
# 3. 결과를 출력한다.
# ]
#
# 밑변 = int(input("밑변을 입력하세요: "))
# 높이 = int(input("높이를 입력하세요: "))
# 면적 = 밑변 * 높이 / 2
# print("삼각형의 면적은", 면적, "입니다.")

def triangle_area(base, height):
    return base * height / 2

print(triangle_area(3, 4))

