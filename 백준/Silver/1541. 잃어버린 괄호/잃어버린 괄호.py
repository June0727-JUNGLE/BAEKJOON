expr = input().strip()

parts = expr.split('-')  # - 기준으로 나누기
total = 0

# 첫 덩어리는 무조건 더함
first = sum(map(int, parts[0].split('+')))
total += first

# 나머지는 모두 괄호로 묶어서 뺌
for part in parts[1:]:
    total -= sum(map(int, part.split('+')))

print(total)
