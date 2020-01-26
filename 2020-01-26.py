## 점프 투 파이썬 - while문

# while문의 기본 구조
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ... # 조건이 참인 동안에는 while문 아래의 문장이 반복한다.

# while문의 예제
treeHit = 0 # treeHit를 0으로 만들어준다.
while treeHit < 10: # treeHit가 10보다 적다면 # 왜 10인가? 이유는 0부터 시작하기때문에 0 은 나무를 1번 찍었습니다. 이기 때문이다.
    treeHit = treeHit +1 # treeHit에 1을 더해줘라 # 동일한 표현으로는 treeHit += 1 처럼 사용할 수 있다.
    print("나무를 %d번 찍었습니다." % treeHit) # print를 해주고 treeHit + 1을 해준 값을 출력한다.
    if treeHit == 10: # treeHit가 10일경우 또한 treeHit가 10 < 10은 거짓이므로 while문을 탈출한다.
        print("나무 넘어갑니다.") # 나무가 넘어갔다고 알려준다.

나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
...
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.

# while문 만들기
number = """
1. add
2. del
3. list
4. quit

entre number : """ ### number에 """부터 시작해서 """까지 값을 동시에 넣는다.

number = 0
while number != 4: # number이 4가 아니면 계속 실행된다.
    print(prompt) # prompt가 계속 실행된다. 입력받는 값이 4가 아니라면
    number = int(input()) # number은 input받는 int정수 값이다. 이 값이 4라면 while문은 멈추게 된다.

# while문 강제로 빠져나가기
coffee = 10 # 커피는 10잔
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0: # 커피가 다 떨어진다면
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break # break문이 호출되어 while문을 빠져나가게 된다.

# while문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

"""
처음에는 무슨소리인지 몰랐다. continue?
지나가다라는 뜻이다. 
만약에 a를 2로 나눴을때 0이라면
그냥 지나가라는 뜻이었다.
그래서 결국엔 1,3,5,7,9인 홀수의 값만 출력할수 있었다.
그렇다면 pass와 다른점은 무엇일까?
pass는 단순히 실행할 코드가 없다는것을 의미한다.
continue는 다음 순번의 loop를 돌도록 강제하는것을 의미한다.
break는 그 loop에서 탈출하는 것이다.
"""

# 무한 루프
while True: 
    수행할 문장1 
    수행할 문장2
    ... # 무한루프의 기본 형태이다.

# 무한 루프 탈출법
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
.... # Ctrl + C를 누르면 무한 루프에서 빠져나올 수 있다.