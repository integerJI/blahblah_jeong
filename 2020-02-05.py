## 점프 투 파이썬 - 모듈

모듈? - 함수나 변수, 클래스를 모아놓은 파일이다.

# 모듈 만들기
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

위와 같이 간단한 함수로 만들어진 파이썬파일 *.py를 모듈이라고 한다. 

# 모듈 불러오기

위의 모듈의 이름을 mod.py라 하고 불러오겠다.

C:\Users\pahkey>cd C:\doit # 해당 파일이 있는 디렉터리로 이동
C:\doit>dir
...
2014-09-23 오후 01:53 49 mod1.py
...
C:\doit>python 파이썬 실행

import mod
print(mod.add(3, 4)) >>> 7
print(mod.sub(4, 2)) >>> 2

mood를 불러오기 위해 import를 하였다. * mod.py라고 풀네임하지 않기
이제 함수를 사용하기위해 mod.add를 사용한다.

import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다. 
파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.

# import의 사용법
import 모듈이름

import를 할고 우리는 함수를 사용하기위해 mod.add 등 mod를 지정해주어야 헀다. 
이를 안하고 하는 방법도있다.

from 모듈이름 import 모듈함수

정확한 경로를 입력해주어

from mod import add
add(3,4) >>> 7

하지만 문제는 위와같이 하면 add함수만 사용할수 있다.

이를 해결하기 위해

from mod import add, sub 처럼 여러개를 불러올수 있지만

from mod import * 하고 모든 함수를 불러올 수 있다.

# if __name__ == "__main__": 의 의미
mod.py를 변경한다.
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

print(add(1, 4))
print(sub(4, 2))

add와 sub를 출력하는 print문을 추가하였다.

C:\doit>python mod.py
>>> 5
>>> 2

실행하면 결괏값이 나온다.

그런데 이 mod.py 파일의 add와 sub 함수를 사용하기 위해 mod 모듈을 import할 때는 좀 이상하다. 

C:\Users\pahkey> cd C:\doit
C:\doit> python
Type "help", "copyright", "credits" or "license" for more information.
import mod1
>>> 5
>>> 2

import mod을 수행하는 순간 mod.py가 실행이 되어 결괏값을 출력한다. 
우리는 단지 mod.py 파일의 add와 sub 함수만 사용하려고 했는디

이러한 문제를 해결하려면 혹은 방지하려면

def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))

다음과 같이 __name__ == "__main__"를 사용하면 된다.
이는 C:\doit>python mod.py처럼 직접 이 파일을 실행했을때 if문으로 걸러준다. * 아래 자세한 설명

다시 실행해 보면

import mod
>>>

아무것도 출력되지 않는다.

# __name__ 변수란?
파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 
만약 C:\doit>python mod.py처럼 직접 mod.py 파일을 실행할 경우
mod.py의 __name__ 변수에는 __main__ 값이 저장된다. 
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod을 import 할 경우에는 
mod.py의 __name__ 변수에는 mod.py의 모듈 이름 값 mod이 저장된다.

# 클래스나 변수 등을 포함한 모듈
지금까지의 모듈은 함수만 포함했지만 클래스나 변수 등을 포함할수도 있다.
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def add(a, b): 
    return a+b 

이 파일은 원의 넓이를 계산하는 Math 클래스와 두 값을 더하는 add 함수 그리고 원주율 값에 해당되는 PI 변수처럼 클래스, 함수, 변수 등을 모두 포함하고 있다.

파일 이름을 mod2.py로 하고 C:\doit 디렉터리에 저장했다 가정하고 실행을 하게되면

C:\Users\pahkey> cd C:\doit
C:\doit> python
Type "help", "copyright", "credits" or "license" for more information.
import mod2
print(mod2.PI) >>> 3.141592

위 예에서 볼 수 있듯이 mod2.PI처럼 입력해서 mod2.py 파일에 있는 PI 변수 값을 사용할 수 있다.

mod2.py에 있는 Math 클래스를 사용하는 방법

a = mod2.Math()
print(a.solv(2)) >>> 12.566368

모듈 안에 있는 클래스를 사용하려면 "."(도트 연산자)로 클래스 이름 앞에 모듈 이름을 먼저 입력해야 한다.

print(mod2.add(mod2.PI, 4.4)) >>> 7.541592

add 함수도 당연히 사용할 수 있다. 

# 다른 파일에서 모듈 불러오기
python.py파일과 python2.py 파일이 동일한 디렉터리에 있으면 어디서든 불러올수있다.

# sys.path.append(모듈을 저장한 디렉터리) 사용하기
sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다. 
이 sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.

sys.path >>> 
['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages']

sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다. 
만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다. 

# sys.path에 추가하기
sys.path.append("모듈이 있는 경로 xxx")
sys.path # 확인

sys.path.append명령어로 추가할수있다. path로 경로를 확인해 보면 무사히 들어간걸 볼수 있다.

이제 import xxx를 이용해 사용할 수 있다.

# PYTHONPATH 환경 변수 사용하기
C:\doit> set PYTHONPATH=C:\doit\mymod
C:\doit> python

set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\doit\mymod 디렉터리를 설정한다. 
그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mod2 모듈을 불러와서 사용할 수 있다.

#나는 PATH환경변수 설정에 울렁증이 있나보다 보기가싫다 나는 sys.path로 추가할래..