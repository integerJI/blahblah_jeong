## 점프 투 파이썬 - 파일 읽고 쓰기

# 파일 생성하기

f = open("새파일.txt", 'w') # 시작 명령어 시작한 폴더에 파일이 만들어졌따(vscode사용)
f.close() # 종료

# 파일 개체 = open(파일이름, 파일열기모드) 이렇게 사용한다.

# 파일 열기 모드의 종류

파일열기모드   설명
r	읽기모드 - 파일을 읽기만 할 때 사용
w	쓰기모드 - 파일에 내용을 쓸 때 사용
a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# 특정 위치의 파일 만들기
f = open("C:/doit/새파일.txt", 'w') # 경로를 지정
f.close() # 생략 가능 하다. 프로그램을 종료할 때 파이썬 프로그램이 자동으로 닫아주기 때문이다.
# 하지만 close()를 사용해서 열려 있는 파일을 직접 닫아 주는 것이 좋다. 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 떄문이다.

# 파일 쓰기모드로 열어 출력값 적기
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 한글이 깨진다.
# f = open("readline_test", 'w', encoding='utf-8')
# 뒤에 encoding 붙여주기

# 이 코드는
'''
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
'''
# 이 코드와 동일하다. 다른점은 data를 출력하는 방법이 다르다.
# 두번째 코드는 우리가 계속 사용하는 것처럼 모니터에 출력하는 법이고
# 첫번째 코드는 파일에 결괏값을 적는 방법이다. 
# 두 방법의 차이점은 print대신 파일 객체 f의 write 함수를 사용한 것이다.

# 실행
# 파일을 확인해 보면
1 번째 줄입니다.
...
10 번째 줄입니다.

# 모니터에 출력될 내용이 적혀 있다.

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

# readline() 함수 이용하기
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

>>> 1 번째 줄입니다.

# 모든 줄이 보고싶을때
# readline_all.py
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# while를 무한으로 주어서 읽어올 readline가 없다면 break한다.

# 키보드를 이용한 입력방법
while 1:
    data = input()
    if not data: break
    print(data)

# 키보드를 이용해 종료할수있다. ( 나는 엔터로 종료됐다.)

# readlines 함수 사용하기
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# readlines 함수는 모든 줄을 읽어 각각의 줄을 요소로 갖는 리스트로 만들어준다.
# ["1 번째 줄입니다.", "2 번째 줄입니다.", ..., "10 번째 줄입니다."]
# readline와 s 하나가 다르니 주의하자

# read 함수 사용하기
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# read는 파일 전체를 문자열로 돌려준다. 

# 파일에 새로운 내용 추가하기
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 새파일을 추가모드('a')로 열고 write를 사용해 결괏값을 기존 파일 에 추가해준다.
# 추가 모드로 파일을 열었기 때문에 원래 가지고 있던 내용 바로 다음부터 결괏값이 입력된다.

# 실행
# 파일을 보면 19번째줄까지 생성됨

# with문과 함께 사용하기
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

# 계속 close를 사용했지만 with문을 사용해서 열고 닫기를 자동으로 처리해줄수있다.

# [sys 모듈로 매개변수 주기]

# DOS 환경

C:\> type a.txt

# type 명령어는 바로 뒤에 적힌 파일을 출력해준다.
# 이러한 기능은 파이썬에서도 쓸 수 있다.
import sys

args = sys.argv[1:]
for i in args:
    print(i)

# sys 모듈을 사용해 매개변수를 직접 줄 수 있다.
# sya 모듈의 argv는 명령 창에서 입력한 인수를 의미한다.
# argv[0]은 파일 이름 sys1.py가 되고 argv[1] 부터는 뒤에 따라오는 인수가 차례로 argv의 요소가 된다.

sys1.py aaa bbb ccc
argv[0] argv[1] argc[2] argc[3]

# 프로그램을 C:\doit에 저장하여 매개변수와 함께 실행하면..
C:\doit>python sys1.py aaa bbb ccc
aaa
bbb
ccc

# 짜란

# sys의 응용
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

# 문자열 관련 함수인 upeer()를 사용하여 소문자를 대문자로 바꾸어주는 프로그램이다.

# 바로 위와 같은 경로에 sys2.py가 있어야 한다.
C:\doit>python sys2.py life is too short, you need python

>>> LIFE IS TOO SHORT, YOU NEED PYTHON

# 짜란
