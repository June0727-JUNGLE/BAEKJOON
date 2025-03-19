x, y = input().split()  # 두 숫자를 문자열로 입력받음

# 문자열 슬라이싱을 사용하여 뒤집은 후, 정수형으로 변환
X = int(x[::-1])
Y = int(y[::-1])

# 두 값 중 큰 값을 출력
if X > Y:
    print(X)
else:
    print(Y)
