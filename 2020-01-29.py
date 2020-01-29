## 점프 투 파이썬 - 함수

# 파이썬 함수의 구조
def 함수명(매개변수): #def는 함수를 만들 때 사용하는 예약어, 함수명은 임의로 만든다.
    <수행할 문장1> #  괄호 안의 매개변수는 함수에 입력으로 전달되는 값을 받는 변수
    <수행할 문장2> # if, while, for문 등 수행할 문장이 들어옴
    ...

# 함수의 예
def add(a, b): 
    return a + b

# 함수의 이름은 add이고 입력으로 a,b두개의 값을 받으며 결과 값은 2개의 입력값을 더한 값이다.

a = 3
b = 4
c = add(a, b)
print(c) >>> 7

# 매개변수와 인수
# 매개변수와 인수는 혼용해서 사용되어 헷갈린다.
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수이며
# 인수는 함수를 호출할 때 전달하는 입력값을 의미함

def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수

# 입력값과 결과값에 따른 함수의 형태
입력값 ---> 함수 ----> 결과값

# 오렌지 ---> 믹서기 ---> 오렌지쥬스
# 함수는 들어온 입력값을 받아 처리를 하여 결과값을 돌려준다.

# 일반적인 함수의 예
def add(a, b): # 함수이름 add, 매개변수 a, b
    result = a + b # 수행할 문장
    return result # 결과값

# 이 함수를 사용한다.
a = add(3, 4)
print(a) >>> 7

# 결과값을 받을 변수 = 함수이름(입력인수1, 입력인수2, ...)

# 입력값이 없는 함수
def say(): # 안에 매개변수가 없다.
    return 'Hi' 

# 입력값이 없는 함수 사용법
a = say()
print(a) >>> Hi

# 괄호 안에 아무 값도 안넣으면 쓸수 있다.
# 결과값을 받을 변수 = 함수이름()

# 결과값이 없는 함수
def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# 반대로 결과값이 없다.
add(3,4) >>> 3, 4의 합은 7입니다.

# 결과값이 없는 함수는 호출해도 돌려주는 값이 없기때문에 이렇게 사용한다.
# 함수이름(입력인수1, 입력인수2, ...)
a = add(3, 4)
print(a) >>> None

# 이렇게 None가 출력된다.

# 입력값도 결과값도 없는 함수
def say(): 
    print('Hi') # 더러워

say() >>> Hi

# 입력값도 결과값도 없는 함수는 그냥 쓰면 된다.
# 함수이름()

# 매개변수 지정하여 호출하기
def add(a, b):
    return a+b

result = add(a=3, b=7)  # a에 3, b에 7을 전달
print(result) >>> 10

# 이렇게 매개변수를 지정하여 사용할 수 있다.
# 매개변수를 지정하면 순서에 상관없이 사용할 수 있다는 장점이 있다. **
result = add(b=5, a=3)  # b에 5, a에 3을 전달
print(result) >>> 8

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def 함수이름(*매개변수): # 특징으로는 "*" 이 붙어있다.
    <수행할 문장>
    ...

# 여러 개의 입력값을 받는 함수 만들기 1
def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i 
    return result 

# add_many의 값이 1,2 면 3을 1,2,3 이면 6을 돌려준다. *을 붙여 모두 튜플로 만들어 주기 떄문이다.
result = add_many(1,2,3)
print(result) >>> 6

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result) >>> 55

# 여러 개의 입력값을 받는 함수 만들기 2
def add_mul(choice, *args): # *args 매개변수 앞에 choice 매개변수가 추가되었다.
    if choice == "add": 
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul": 
        result = 1 
        for i in args: 
            result = result * i 
    return result 

# 사용
result = add_mul('add', 1,2,3,4,5)
print(result) >>> 15

result = add_mul('mul', 1,2,3,4,5)
print(result) >>> 120

# 매개변수 choice에 'add'가 입력된 경우 *args에 입력되는 모든 값을 더해서 15를 돌려주고, 
# 'mul'이 입력된 경우 *args에 입력되는 모든 값을 곱해서 120을 돌려준다.

# 키워드 파라미터 kwargs
def print_kwargs(**kwargs): # 이건 또 *을 두개나 붙인다..;
        print(kwargs)
 
# 사용
print_kwargs(a=1) >>> {'a': 1}

print_kwargs(name='foo', age=3) >>> {'age': 3, 'name': 'foo'}

# 입력값 a=1 또는 name='foo', age=3이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다. 
# 즉 **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.

# 함수의 결과값은 언제나 하나이다
def add_and_mul(a,b): 
    return a+b, a*b

result = add_and_mul(3,4) # 이렇게 호출할경우 오류는 발생하지 않는다.
# 그 이유는 함수의 결괏값은 2개가 아니라 언제나 1개라는 데 있다. add_and_mul 함수의 결괏값 a+b와 a*b는 튜플값 하나인 (a+b, a*b)로 돌려준다.

>>> result = (7, 12) # 결과

# 만약 하나의 튜플 값을 2개의 결과값처럼 받고싶다면..

>>> result1, result2 = add_and_mul(3, 4)

# 또 하나의 의문점
def add_and_mul(a,b): 
    return a+b
    return a*b

# 이러한 함수는 어리석은 함수이다.
result = add_and_mul(2, 3)
print(result) >>> 5

# add_and_mul(2, 3)의 결괏값은 5 하나뿐이다. 
# 두 번째 return문인 return a*b는 실행되지 않았다는 뜻이다.

# 결국 아래의 함수와 같다.
def add_and_mul(a,b): 
    return a+b 

# return의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
def say_nick(nick): 
    if nick == "바보": 
        return 
    print("나의 별명은 %s 입니다." % nick)

# 위 함수는 '별명'을 입력으로 전달받아 출력하는 함수이다. 
# 이 함수 역시 반환 값(결과값)은 없다.
# (문자열을 출력한다는 것과 반환 값이 있다는 것은 전혀 다른 말이다. 혼동하지 말자. 함수의 반환 값은 오로지 return문에 의해서만 생성된다).
# 만약에 입력값으로 '바보'라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나간다.

say_nick('야호') >>> 나의 별명은 야호입니다.
say_nick('바보') >>>

# 매개변수에 초기값 미리 설정하기
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

# say_myself 함수는 3개의 매개변수를 받아서 마지막 인수인 man이 True이면 "남자입니다.", False이면 "여자입니다."를 출력한다.
# 매개변수는 name, old, man=True 이렇게 3개다.
# man=True 이것이 바로 함수의 매개변수 초기값을 설정하는 방법이다. 함수의 매개변수에 들어갈 값이 항상 변하는 것이 아닐 경우에는 이렇게 함수의 초기값을 미리 설정해 두면 유용하다.

# 또다른 사용법
say_myself("박응용", 27)
say_myself("박응용", 27, True)

# 입력값으로 "박응용", 27처럼 2개를 주면 name에는 "박응용"이 old에는 27이 대입된다. 그리고 man이라는 변수에는 입력값을 주지 않았지만 초기값 True를 갖게 된다.
# 따라서 위 예에서 함수를 사용한 2가지 방법은 모두 동일한 결과를 출력한다.
나의 이름은 박응용입니다.
나이는 27살입니다.
남자입니다.

# 거꾸로
say_myself("박응선", 27, False)

# 여자입니다가 출력된다.

# 매개변수에 초기값을 설정할 때 주의해야할 점
def say_myself(name, man=True, old): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.") 
    else: 
        print("여자입니다.")

# 매개변수의 위치가 중간이다.
say_myself("박응용", 27)

# 위와 같이 함수를 호출한다면 name 변수에는 "박응용"이 들어갈 것이다. 
# 하지만 파이썬 인터프리터는 27을 man 변수와 old 변수 중 어느 곳에 대입해야 할지 알 수 없게 된다.

# 초기값을 설정해 놓은 매개변수 뒤에 초기값을 설정해 놓지 않는 매개변수는 사용할 수 없다.

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)

# 함수 안에서 사용할 변수의 이름을 함수 밖에서도 동일하게 사용했다.

# a란 변수를 생성하고 1을 대입하고 다음 입력으로 들어온 값에 1을 더해 주지만 결과값은 돌려주지않는 vartest 함수를 선언한다.
# vartest 함수에 입력값으로 a를 주고 마지막으로 a를 출력하는 print(a)를 입력한다.

# 이때 당연히 vartest 함수에서 매개변수 a의 값에 1을 더하니까 2가 출력될 것 같지만
# 결과값은 1이다.
# 그 이유는 함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 "함수만의 변수"이기 때문이다.
# 즉 def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수이지 함수 밖의 변수 a가 아니라는 뜻이다.

# 따라서 vartest 함수는 다음처럼 변수 이름을 hello로 한 vartest 함수와 완전 동일하다.

def vartest(hello):
    hello = hello + 1

# 즉 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다는 뜻이다.

def vartest(a):
    a = a + 1

vartest(3)
print(a)

# vartest(3)을 수행하면 vartest 함수안에서 a는 4가 되지만 함수를 호출하고 난 뒤 print(a) 문장은 오류가 발생한다.
# 왜냐하면 print(a)에서 입력받아야 하는 a 변수를 찾을 수가 없기 때문이다.
# 결론은 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다.**

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 그렇다면 vartest라는 함수를 사용해서 함수 밖의 변수 a를 1만큼 증가시킬 수 있는 방법

# return 사용하기
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)

# vartest 함수는 입력으로 들어온 값에 1을 더한값을 돌려준다.
# 따라서 a = vartest(a)라고 대입하면 a가 vartest 함수의 결과값으로 바뀐다.
# 물론 vartest 함수 안의 a 매개변수는 함수 밖의 a와는 다른 것이다.

# global 명령어 사용하기
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)

# vartest 함수 안의 global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다. 
# 하지만 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다. 왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다.
# 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다. 그러므로 가급적 global 명령어를 사용하는 이 방법은 피하고 첫 번째 방법을 사용하기를 권한다.

# lambda
# 람다는 def와 동일한 역할로 쓰인며 한줄로 간결하게 만들 때 사용한다.
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

# lambda 사용법
lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b: a+b
result = add(3, 4)
print(result) >>> 7

# 위 함수는 처음 한 def add를 만든 함수와 동일하다.
# lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.
