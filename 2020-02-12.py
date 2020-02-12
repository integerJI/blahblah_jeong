## 점프 투 파이썬 - 외장 함수

time - 시간과 관련된 time 모듈

time.time - UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.
import time
time.time() >>> 988458015.73417199

time.localtime - time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수이다.
time.localtime(time.time())
time.struct_time(tm_year=2013, tm_mon=5, tm_mday=21, tm_hour=16,
    tm_min=48, tm_sec=42, tm_wday=1, tm_yday=141, tm_isdst=0)

time.asctime - time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
time.asctime(time.localtime(time.time())) >>> 'Sat Apr 28 20:50:20 2001'

time.ctime - time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다. asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.
time.ctime() >>> 'Sat Apr 28 20:56:31 2001'

time.strftime - 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))

포맷코드	설명		예
%a	요일 줄임말	Mon
%A	요일		Monday
%b	달 줄임말		Jan
%B	달		January
%c	날짜와 시간을 출력함	06/01/01 17:22:21
%d	날(day)		[01,31]
%H	시간(hour)-24시간 출력 형태	[00,23]
%I	시간(hour)-12시간 출력 형태	[01,12]
%j	1년 중 누적 날짜	[001,366]
%m	달		[01,12]
%M	분		[01,59]
%p	AM or PM	AM
%S	초		[00,59]
%U	1년 중 누적 주-일요일을 시작으로	[00,53]
%w	숫자로 된 요일	[0(일요일),6]
%W	1년 중 누적 주-월요일을 시작으로	[00,53]
%x	현재 설정된 로케일에 기반한 날짜 출력		06/01/01
%X	현재 설정된 로케일에 기반한 시간 출력		17:22:21
%Y	년도 출력		2001
%Z	시간대 출력	대한민국 표준시
%%	문자		%
%y	세기부분을 제외한 년도 출력		01

time.strftime을 사용하는 예


import time
time.strftime('%x', time.localtime(time.time())) >>> '05/01/01'
time.strftime('%c', time.localtime(time.time())) >>> '05/01/01 17:22:21'

time.sleep - 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다. 다음 예를 보자.
import time
for i in range(10):
    print(i)
    time.sleep(1)

1초 간격으로 0부터 9까지의 숫자를 출력한다. 위 예에서 볼 수 있듯이 time.sleep 함수의 인수는 실수 형태를 쓸 수 있다. 즉 1이면 1초, 0.5면 0.5초가 되는 것이다.

calendar - 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.

calendar.calendar(연도) - 그해의 전체 달력을 볼 수 있다. 결괏값은 달력이 너무 길어 생략하겠다.
import calendar
print(calendar.calendar(2015))

==

calendar.prcal(2015)

calendar.prmonth(2015, 12)
December 2015
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
7  8  9  10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

calendar.weekday -  weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다. 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6이라는 값을 돌려준다.
calendar.weekday(2015, 12, 31) >>> 3

calendar.monthrange - 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
calendar.monthrange(2015,12) >>> (1, 31)

random - 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다.

0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려준다.
import random
random.random() >>> 0.53840103305098674


1에서 10 사이의 정수 중에서 난수 값을 돌려준다.
random.randint(1, 10) >>> 6

1에서 55 사이의 정수 중에서 난수 값을 돌려준다.
random.randint(1, 55) >>> 43

random 모듈 예
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: 
        print(random_pop(data))

결과값:
2 
3 
1 
5 
4

random_pop 함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려준다. 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.

random_pop 함수는 random 모듈의 choice 함수를 사용하여 다음과 같이 좀 더 직관적으로 만들 수도 있다.

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 돌려준다.

리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용하면 된다.
import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
data >>> [5, 1, 3, 4, 2]

webbrowser - 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다. 
웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 가게 해 준다.
import webbrowser
webbrowser.open("http://google.com")

webbrowser의 open 함수는 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동한다. 만약 웹 브라우저가 실행되지 않은 상태라면 새로 웹 브라우저를 실행한 후 해당 주소로 이동한다.

open_new - 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 한다.
webbrowser.open_new("http://google.com")

스레드를 다루는 threading 모듈
컴퓨터에서 동작하고 있는 프로그램을 프로세스(Process)라고 한다. 보통 1개의 프로세스는 한 가지 일만 하지만 스레드(Thread)를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.

ex
import time

def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("working:%s\n" % i)

print("Start")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("End")

long_task 함수는 수행하는 데 5초의 시간이 걸리는 함수이다. 위 프로그램은 이 함수를 총 5번 반복해서 수행하는 프로그램이다. 이 프로그램은 5초가 5번 반복되니 총 25초의 시간이 걸린다.

하지만 앞에서 설명했듯이 스레드를 사용하면 5초의 시간이 걸리는 long_task 함수를 동시에 실행할 수 있으니 시간을 줄일 수 있다.

수정
import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t) 

for t in threads:
    t.start()  # 스레드를 실행한다.

print("End")

수정하고 실행해 보면 25초 걸리던 작업이 5초 정도에 수행되는 것을 확인할 수 있다. threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해 주기 때문이다.

하지만 위 프로그램을 실행해 보면 "Start"와 "End"가 먼저 출력되고 그 이후에 스레드의 결과가 출력되는 것을 확인할 수 있다. 그리고 프로그램이 정상 종료되지 않는다. 우리가 기대하는 것은 "Start"가 출력되고 그다음에 스레드의 결과가 출력된 후 마지막으로 "End"가 출력되는 것이다.

해결하기 위한 수정
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")

스레드의 join 함수는 해당 스레드가 종료될 때까지 기다리게 한다. 따라서 위와 같이 수정하면 우리가 원하던 출력을 보게 된다.

