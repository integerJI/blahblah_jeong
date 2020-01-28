## 점프 투 파이썬 - 집합 자료형

# 집합 자료형
s1 = set([1,2,3]) # 집합 자료형은 set 키워드를 사용해 만들 수 있다.
s1 >>> {1,2,3}

s = set() # 빈 집합

# 집합 자료형의 특징
s2 = set("Hello") # 문자열도 가능하다. 
s2 >>> {'e','H','l','o'} # 중복을 허용하지않는다. + 순서가 없다.

s1 = set([1,2,3])
l1 = list(s1) # set 자료형에는 순서가 없다.
l1 >>> [1,2,3] # 그래서 인덱싱도 없다.
l1[0] >>> 1 # 그래서 튜플 혹은 리스트로 묶어줘야 인덱싱으로 접근이 가능하다.

t1 = tuple(s1)
t1 >>> (1,2,3)
t1[0] >>> 1

# 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2 >>> {4,5,6} # & 기호를 사용해 교집합을 사용한다.
s1.intersection(s2) >>> {4,5,6} # intersection 함수를 사용해도 가능하다. (거꾸로 써도 값은 같다.)

s1 | s2 >>> {1,2,3,4,5,6,7,8,9} # | 기호를 사용해 합집합을 사용한다.
s1.union(s2) >>> {1,2,3,4,5,6,7,8,9} # union 함수를 사용해도 가능하다. (거꾸로 써도 값은 같다.)

s1 - s2 >>> {1,2,3} # - 기호를 사용해 차집합을 사용한다.
s2 - s1 >>> {8,9,7} # 거꾸로는 불가능

s1.difference(s2) >>> {1,2,3} # difference 함수를 사용해도 가능하다.
s2.difference(s1) >>> {8,9,7} # 거꾸로는 불가능

## 점프 투 파이썬 - 불 자료형

# 불 자료형
a = True # - 참, 첫 문자를 항상 대문자로 사용해야 한다.
b = False #- 거짓, 불 자료형은 참과 거짓 두가지 값만을 가질 수 있다.

type(a) >>> <<class 'bool'>> # 문자열을 따옴표로 감싸지 않았지만 불 자료형으로 지정된것을 확인할수있다.

1 == 1 >>> True # 1은 1과 같다. 그러므로 True를 돌려준다.
1 is 1 >>> True # is로도 사용이 가능하다.

# 자료형의 참과 거짓
값          참 or 거짓
"python"	참
""      	거짓
[1, 2, 3]	참
[]      	거짓
()	        거짓
{}	        거짓
1       	참
0	        거짓
None	    거짓

# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 거짓이 된다. 당연히 비어있지 않으면 참
# 숫자는 그 값이 0일때 거짓이 된다. 
# None는 그저 거짓이다.

# 불 연산
bool('python') >>> True # 'python'은 빈 문자열이 아니므로 True다.
bool('') >>> False # 비엇다.

## 점프 투 파이썬 - 자료형의 값을 저장하는 공간, 변수

# 변수 만드는 방법
a = 1 # 변수를 만들 때는 = 기호를 사용한다.
b = 'python' # python은 변수를 저장할때 값을 스스로 판단하여 자료형을 지정한다.
c = [1,2,3] # 변수 이름 = 변수에 저장할 값 (객체)

# 변수란
# 파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말할 수 있다. 
# 객체란 우리가 지금껏 보아 온 자료형과 같은 것을 의미하는 말이다

# 변수가 가리키는 메모리 주소 확인하기.
a = [1,2,3]
id(a) >>> 4303029896 # id라는 내장함수를 통하여 메모리 주소를 확인할 수 있다. 리스트의 주소값은 4303029896이다.

# 리스트의 복사 (리스트할때 알려주지 ;;;)
a = [1,2,3]
b = a # 거꾸로 하면 안됨
b >>> [1,2,3] # 짜잔 복사 

id(a) >>> 4303029896 # 값을 복사하면 메모리 주소값은 똑같다.(?!)
id(b) >>> 4303029896

a is b >>> True # 같다.

a[1] = 4
a >>> [1,4,3]
b >>> [1,4,3] # a를 바꿔도 b도 같이 변한다. 동일한 리스트를 가리키고 있기 때문이다.

# 메모리 주소를 다르게 복사하기 1
a = [1,2,3]
b = a[:]
a[1] = 4
a >>> [1, 4, 3]
b >>> [1, 2, 3] # [:]를 사용하면 메모리주소는 다르게 복사가 가능하다.

id(a) >>> 64876496
id(b) >>> 64885064

# 메모리 주소를 다르게 복사하기 2
from copy import copy
b = copy(a) # : 사용과 동일하다. copy 모듈을 가져와 사용한다.

b is a >>> False # 다르다

# 변수를 만드는 여러가지 방법
a, b = ('hi','hello') # 튜플로 a,b를 동시에 대입할수있다.
(a,b) = 'hi','hello' # 튜플로 지정하기때문에 괄호를 생략할수있다. 위의 결과와 같다.
[a,b] = ['hi','hello'] # 리스트도 가능
a = b = 'hi' # 여러개의 변수에 같은 값을 대입할수도있다.

a = 3
b = 5
a,b = b,a # 이 문장을 통하여 값을 바꿀수도 있다. 문자 타입도 상관없음
a >>> 5
b >>>s 3
