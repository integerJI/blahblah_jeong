## 점프 투 파이썬 - 외장 함수 ( 1 )

여러 가지 라이브러리를 살펴보자. 

sys - 변수와 함수를 직접 제어할 수 있게 해 준다.

명령 행에서 인수 전달하기 - sys.argv 

#test.py 
import sys 
print(sys.argv) 

C:/User/home > python test.py abc pey guido 
['test.py', 'abc', 'pey', 'guido'] 

# 명령 프롬프트 창에서는 /, \든 상관없지만, 소스코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다. 

강제로 스크립트 종료하기 - sys.exit 
sys.exit 

Ctrl+Z나 Ctrl+D를 눌러서 대화형 인터프리터를 종료하는 것과 같다.  
프로그램 파일 안에서 사용하면 프로그램을 중단시킨다. 

자신이 만든 모듈 불러와 사용하기 - sys.path 

import sys 
sys.path 

['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs',  
'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages'] 

sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다.  
''는 현재 디렉터리를 말한다. 

경로 이름 추가하기 - sys.path.append 
import sys 
sys.path.append("C:/doit/mymod") 

추가하면 디렉터리에 있는 파이썬 모듈을 불러와 사용할 수 있다. 

pickle - 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.  
import pickle 
f = open("test.txt", 'wb') 
data = {1: 'python', 2: 'you need'} 
pickle.dump(data, f) 
f.close() 


pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여 준다. 

import pickle 
f = open("test.txt", 'rb') 
data = pickle.load(f) 
print(data) 
{2:'you need', 1:'python'} 

pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러온다. 
딕셔너리 객체를 사용했지만 어떤 자료형 이든 저장하고 불러올 수 있다. 

os - 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다. 

내 시스템의 환경 변수값을 알고 싶을 때 - os.environ 
import os 
os.environ 
environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …}) 

os.environ은 환경 변수에 대한 정보를 딕셔너리 객체로 돌려준다. 

os.environ['PATH'] 
'C:\\ProgramData\\Oracle\\Java\\javapath;...생략...' 

객체가 딕셔너리이기 때문에 이렇게 호출할 수 있다. 

디렉터리 위치 변경하기 - os.chdir 
os.chdir("C:\WINDOWS") 

현재 디렉터리 위치를 변경할 수 있다. 

디렉터리 위치 돌려받기 - os.getcwd 

os.getcwd() 
'C:\WINDOWS' 

자신의 디렉터리 위치를 돌려준다. 

시스템 명령어 호출하기 - os.system 

os.system("dir") 

시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다.  
os.system("명령어")처럼 사용한다. 다음은 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예이다. 

실행한 시스템 명령어의 결괏값 돌려받기 - os.popen 

f = os.popen("dir") 

시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다. 

print(f.read()) 

읽어 들인 파일 객체의 내용을 보기 위한 방법이다. 

기타 유용한 os 관련 함수 

함수 설명 
os.mkdir(디렉터리) 디렉터리를 생성한다. 
os.rmdir(디렉터리) 디렉터리를 삭제한다. 단, 디렉터리가 비어있어야 삭제가 가능하다. 
os.unlink(파일) 파일을 지운다. 
os.rename(src, dst) src라는 이름의 파일을 dst라는 이름으로 바꾼다. 

shutil - 파일을 복사해 주는 파이썬 모듈이다. 

import shutil 
shutil.copy("src.txt", "dst.txt") 

src라는 이름의 파일을 dst로 복사한다. 
dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사한다. 
동일한 파일 이름이 있을 경우 덮어쓴다.

glob - 디렉터리에 있는 파일들을 리스트로 만든다. 
import glob 
glob.glob("c:/doit/mark*") 
['c:/doit\\marks1.py', 'c:/doit\\marks2.py', 'c:/doit\\marks3.py'] 

C:/doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어 들인다.
glob 모듈은 디렉터리 안의 파일들을 읽어서 돌려준다. *, ? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다. 

tempfile - 파일을 임시로 만들어서 사용할 때 유용한 모듈이다. 
import tempfile 
filename = tempfile.mkstemp() 
filename 
'C:\WINDOWS\TEMP\~-275151-0' 
tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다. 

import tempfile 
f = tempfile.TemporaryFile() 
f.close() 

tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.  
이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.  
f.close()가 호출되면 이 파일 객체는 자동으로 사라진다. 