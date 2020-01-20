## 점프 투 파이썬 - 숫자형

# 정수형
a = 123
a = -123
a = 0

# 실수형
a = 1.2
a = -1.2

# 8진수 0o 또는 0O로 시작한다.
a = 0o177

# 16진수 0x로 시작한다.
a = 0x8ff
a = 0xABC

# 사칙연산
a + b - c * d / e
a ** b = a^b
a % b = 나머지
a // b = 몫

# 사칙연산의 활용
b = 369 자리수 구하기
b % 10 = 1의 자리
(b % 100)//10 = 10의 자리
(b // 100) = 100의 자리

## 점프 투 파이썬 - 문자열 자료형
# 문자열의 활용 ( ' ' / " " / ''' ''' / """ """ )

# \ 의 활용
str = "Life is too short \\ You need python"
print(str) = Life is too short \ You need python

# 줄바꿈
\n의 사용
str = "Life is too short\nYou need python"
print(str) = Life is too short
             You need python

or

# 작은따옴표 3개 큰따옴표 3개
str = """
Life is too short
You need python
"""

# 이스케이프 코드
\n  	문자열 안에서 줄을 바꿀 때 사용
\t  	문자열 사이에 탭 간격을 줄 때 사용
\\  	문자 \를 그대로 표현할 때 사용
\'  	작은따옴표(')를 그대로 표현할 때 사용
\"  	큰따옴표(")를 그대로 표현할 때 사용
\r  	캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
\f  	폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
\a  	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b  	백 스페이스
\000	널 문자

\n, \t, \\, \', \" 활용빈도가 높다.

# 문자열의 덧셈 곱셈
a = "a"
b = "b"
a + b
"ab"
a * 2
"aa"

# 응용
print("="*5)
print("python")
print("="*5)
=====
python
=====

# 문자열의 인덱싱
a = "Life is too short, You need Python"
a[3] >>> 'e'
a[-1] >>> 'n' # -1은 맨 뒤의 값을 가져온다.
a[-0] >>> 'L' # 그냥 첫번째

# 문자열의 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b >>> 'Life'

a[0:4] >>> 'Life' # 0번부터 3번까지
a[5:7] >>> 'is' # 4번부터 6번까지
a[:17] >>> 'Life is too short, You need Python' # 시작번호 생략하면 처음부터. 끝번호 생략하면 끝까지

a[1] = 'L' >>> "LLfe is ..." # 문자열 바꾸기

# 문자열 포매팅
"I eat %d apples." % 3
>>> 'I eat 3 apples.'

# 포매팅 응용
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
>>> 'I ate 10 apples. so I was sick for three days.'

# 문자열 포맷 코드
%s	문자열(String)
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)

%s는 어떠한 값이라도 들어간다.
%%는 같은 문자열 안에 %가 있으면 %를 출력하게 도와준다.

# 포매팅을 이용한 정렬과 공백
"%10s" % "hi" >>> '        hi' # 문자열에 대입되는 값을 오른쪽으로 정렬하여 왼쪽에 10개의 공백
"%-10sjane." % 'hi' >>> 'hi        jane.' # 왼쪽으로 정렬하여 왼쪽에 10개의 공백

# 포매팅을 이용한 소수점 표현하기
"%0.4f" % 3.42134234 >>> '3.4213'
"%10.4f" % 3.42134234 >>> '    3.4213' # 정렬까지

# format 함수를 이용한 포매팅
"I eat {0} apples".format(3) >>> 'I eat 3 apples'
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
>>> 'I ate 10 apples. so I was sick for three days.'

# format 함수를 이용한 정렬 및 채우기
"{0:<10}".format("hi") >>> 'hi        ' # 왼쪽
"{0:>10}".format("hi") >>> '        hi' # 오른쪽
"{0:^10}".format("hi") >>> '    hi    ' # 가운데
"{0:=^10}".format("hi") >>> '====hi====' # 채우기
"{0:!<10}".format("hi") >>> 'hi!!!!!!!!' # 채우기 2

# format 함수를 이용한 소수점 표현
y = 3.42134234
"{0:0.4f}".format(y) >>>'3.4213'
"{0:10.4f}".format(y) >>> '    3.4213' # 자리수를 10으로 맞춘다.

# {} 표현 방법
"{{ and }}".format() >>> '{ and }'

# f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
>>> '나의 이름은 홍길동입니다. 나이는 30입니다.'
f'나는 내년이면 {age+1}살이 된다.' # 연산 가능
>>> '나는 내년이면 31살이 된다.'

# 딕셔너리 가볍게
d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
>>> '나의 이름은 홍길동입니다. 나이는 30입니다.'