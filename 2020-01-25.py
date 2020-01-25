## 점프 투 파이썬 - if문

# if문의 기본 구조
if 조건문:
    수행할 문장1 
    수행할 문장2
수행할 문장2         # 들여쓰기로 구분하니 주의하자.
        수행할 문장2 # 들여쓰기로 구분하니 주의하자.
    ...
else:                # 조건문 뒤에 : 주의!
    수행할 문장A     # 들여쓰기를 할때 Tab or Spacebar 4개 요즘은 공백 4개 사용 권장
    수행할 문장B
    ...

# 조건을 비교하기 위한 비교 연산자
비교연산자	설명
x < y	    x가 y보다 작다
x > y	    x가 y보다 크다
x == y	    x와 y가 같다
x != y	    x와 y가 같지 않다
x >= y	    x가 y보다 크거나 같다
x <= y	    x가 y보다 작거나 같다

# 비교 연산자의 사용
# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
>>> 걸어가라

# 조건을 비교하기 위한 연산자
연산자	 설명
x or y	 x와 y 둘중에 하나만 참이면 참이다
x and y	 x와 y 모두 참이어야 참이다
not x	 x가 거짓이면 참이다

# 연산자의 사용
# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
>>> 택시를 타고 가라

# python에서 볼 수 있는 조건문 "x in s, x not in s"
in	            not in
x in 리스트	    x not in 리스트
x in 튜플	    x not in 튜플
x in 문자열	    x not in 문자열

# in의 사용
'j' not in 'python' >>> True # 'j'가 'python'안에 없는가? >>> True

# 조건문에서 아무 일도 하지 않게 설정하기
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")
>>> ... # pass라 아무것도 안나옴

# elif의 사용
# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card: 
    print("택시를 타고가라")
else:
    print("걸어가라")
>>> 택시를 타고가라

# if문 한 줄로 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식의 사용
# 기존 코드
if score >= 60:
    message = "success"
else:
    message = "failure"

# 조건부 표현식
message = "success" if score >= 60 else "failure"
# "조건문이 참인 경우" if "조건문" else "조건문이 거짓인 경우"
# 조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.