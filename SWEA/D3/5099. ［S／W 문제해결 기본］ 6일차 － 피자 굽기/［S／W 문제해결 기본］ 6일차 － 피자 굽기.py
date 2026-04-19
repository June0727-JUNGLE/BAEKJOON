from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    Ci = deque(map(int, input().split()))

    pizza = deque() #화덕을 만듬
    pizza_num = deque() #피자 번호를 저장하는 큐

    for i in range(N):
        pizza.append(Ci.popleft()) #화덕에 N개 피자 넣기
        pizza_num.append(i+1) #피자 번호 저장

    num = N

    while len(pizza) > 1: #화덕에 피자가 1개 남을 때까지 반복
        current_pizza = pizza.popleft()//2
        current_pizza_num = pizza_num.popleft()
        

        if current_pizza != 0:
            pizza.append(current_pizza) #치즈가 남았으면 다시 화덕에 넣기
            pizza_num.append(current_pizza_num)
        else:
            if Ci: #남은 피자가 있으면 화덕에 넣기
                pizza.append(Ci.popleft())
                num+=1
                pizza_num.append(num)

    print(f'#{_+1} {pizza_num[0]}')
     