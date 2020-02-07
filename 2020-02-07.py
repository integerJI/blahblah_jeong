## 점프 투 파이썬 - 예외 처리 

이번에는 오류를 무시하고 싶을 때 사용하는 걸 배운다. 
ex ) try, except 

# 오류는 어떤 때 발생하는가? 
실제 프로그램에서 자주 발생하는 오류를 중심으로 기록. 

>>> f = open("나없는파일", 'r') 
Traceback (most recent call last): 
  File "", line 1, in  
FileNotFoundError: [Errno 2] No such file or directory: '나없는파일' 

디렉터리 안에 없는 파일을 열려고 할 때 발생하는 오류 -FileNotFoundError- 

>>> 4 / 0 
Traceback (most recent call last): 
  File "", line 1, in  
ZeroDivisionError: division by zero 

0으로 다른 숫자를 나누는 경우 -ZeroDivisionError- 

>>> a = [1,2,3] 
>>> a[4] 
Traceback (most recent call last): 
  File "", line 1, in  
IndexError: list index out of range 

리스트에 없는 값을 얻으려고 할 때 -IndexError - 

이 외에도 처리하다 생기는 오류는 적어놔야겠다. 

# 오류 예외 처리 기법 

# try, except문 
try, except문의 기본 구조 

try: 
    ... 
except [발생 오류[as 오류 메시지 변수]]: 
    ... 

try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.  
하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다. 

except [발생 오류 [as 오류 메시지 변수]]: 

위 구문을 보면 [ ] 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다. 

except 구문의 사용방법 3가지 

1. try, except만 쓰는 방법 
try: 
    ... 
except: 
    ... 

이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다. 

2. 발생 오류만 포함한 except문 
try: 
    ... 
except 발생 오류: 
    ... 

이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다. 

3. 발생 오류와 오류 메시지 변수까지 포함한 except문 
try: 
    ... 
except 발생 오류 as 오류 메시지 변수: 
    ... 

이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다. 

3번째 방법의 예 
try: 
    4 / 0 
except ZeroDivisionError as e: 
    print(e) >>> division by zero 

위처럼 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고 변수 e에 담기는 오류 메시지를 다음과 같이 출력한다. 

# try .. finally 
try문에는 finally절을 사용할 수 있다. finally 절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.  
finally절은 사용한 리소스를 close 해야 할 때에 많이 사용한다. 

try .. finally의 예 
f = open('foo.txt', 'w') 
try: 
    # 무언가를 수행한다. 
finally: 
    f.close() 

foo.txt 파일을 쓰기 모드로 연 후에 try문을 수행한 후 예외 발생 여부와 상관없이  
finally절에서 f.close()로 열린 파일을 닫을 수 있다. 

# 여러개의 오류 처리하기
try문 안에서 여러 개의 오류를 처리하기 위해 다음 구문을 사용한다. 
try: 
    ... 
except 발생 오류 1:
   ...  
except 발생 오류 2:
   ... 

즉 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다. 

try: 
    a = [1,2] 
    print(a[3]) 
    4/0 
except ZeroDivisionError: 
    print("0으로 나눌 수 없습니다.") 
except IndexError: 
    print("인덱싱 할 수 없습니다.") 

a는 2개의 요솟값을 가지고 있기 때문에 a[3]은 IndexError을 발생시킨다. 
인덱싱 오류가 먼저 발생해서 4/0으로 발생되는 ZeroDivisionError:는 발생하지 않는 것이다.

try: 
    a = [1,2] 
    print(a[3]) 
    4/0 
except ZeroDivisionError as e: 
    print(e) 
except IndexError as e: 
    print(e) 

해당 코드를 실행하면 "list index out of range" 오류 메시지가 나온다. 

이를 ZerroDivisionError와 IndexError를 함께 처리할 수도 있다. 

try: 
    a = [1,2] 
    print(a[3]) 
    4/0 
except (ZeroDivisionError, IndexError) as e: 
    print(e) 

2개 이상의 오류를 동시에 처리하기 위해서는 위와 같이 괄호를 사용하여 함께 묶어 처리하면 된다. 

# 오류 회피하기 

try: 
    f = open("나없는파일", 'r') 
except FileNotFoundError: 
    pass 

try문 안에 FileNotFoundError가 발생한 경우 pass를 사용하여 오류를 pass 한다.
오류 : 지나가요~ 

# 오류 일부러 발생시키기 
코드를 작성하다 보면 종종 오류를 일부러 발생시켜야 할 때도 생긴단다. 
오류를 발생시키려면 raise명령어를 사용해 발생시킬 수 있다. 

Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우 (강제로 그렇게 하고 싶은 경우) 

class Bird: 
    def fly(self): 
        raise NotImplementedError # 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다. 

Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여 준다. 
만약 자식 클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면? 

class Eagle(Bird): 
    pass 

eagle = Eagle() 
eagle.fly() 

Eagle 클래스는 Bird 클래스를 상속받는다.  
그런데 Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird 클래스의 fly 함수가 호출된다.  
그리고 raise문에 의해 NotImplemented Error가 발생할 것이다. 

* 상속받는 클래스에서 함수를 재구현하는 것을 메서드 오버 라이딩이라고 부른다. 

NotImplemented Error가 발생되지 않게 하려면 Eagle 클래스에 fly 함수를 반드시 구현해야 한다. 
Traceback (most recent call last): 
  File "...", line 33, in  
    eagle.fly() 
  File "...", line 26, in fly 
    raise NotImplementedError 
NotImplementedError 

fly 함수를 구현한 후 프로그램을 실행하면 오류가 없이 정상 출력된다. 
class Eagle(Bird): 
    def fly(self): 
        print("very fast") 

eagle = Eagle() 
eagle.fly() 

>>> very fast 

# 예외 만들기 
프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다.  
직접 예외를 만들려면 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다. 

Exception을 상속하는 class MyError를 만든다. 
class MyError(Exception): 
    pass 

별명을 출력해 주는 함수 생성 
def say_nick(nick): 
    if nick == '바보': 
        raise MyError() 
    print(nick) 

say_nick 함수를 호출 
say_nick("천사") 
say_nick("바보") 

실행해 보면 "천사"가 한번 출력된 후 MyError가 발생한다. 
천사 
Traceback (most recent call last): 
  File "...", line 11, in  
    say_nick("바보") 
  File "...", line 7, in say_nick 
    raise MyError() 
__main__.MyError 

# 직접 만든 MyError를 예외 처리해보기
try: 
    say_nick("천사") 
    say_nick("바보") 
except MyError: 
    print("허용되지 않는 별명입니다.") 

실행해 보면 설정한 print문이 나오게 된다. 
천사 
허용되지 않는 별명입니다. 

만약 오류 메시지를 사용하고 싶다면 예외처리를 하면 된다. 
try: 
    say_nick("천사") 
    say_nick("바보") 
except MyError as e: 
    print(e) 
요로캐

하지만 프로그램을 실행해 보면 print(e)로 오류 메시지가 출력되지 않는다. 
오류 메시지를 출력했을 대 오류 메시지가 보이게 하려면 오류 클래스에 __str__ 메서드를 구현해야 한다. 
__str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다. 

class MyError(Exception): 
    def __str__(self): 
        return "허용되지 않는 별명입니다." 

다시 실행하 보면 return문이 정상 출력이 된다. 