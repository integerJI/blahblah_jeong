## 점프 투 파이썬 - 내장 함수 2

isinstance - 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

class Person: pass
a = Person()
isinstance(a, Person) >>> True

# a는 Person 클래스가 만든 인스턴스이다.

b = 3
isinstance(b, Person) >>> False

# b는 Person 클래스가 만든 인스턴스가 아니다.

len - 입력값의 길이를 돌려주는 함수이다. ( 요소의 전체 개수 )
len("python") >>> 6
len([1,2,3]) >>> 3
len((1, 'a')) >>> 2

list >>> 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
list("python") >>> ['p', 'y', 't', 'h', 'o', 'n']
list((1,2,3)) >>> [1, 2, 3]

a = [1, 2, 3]
b = list(a)
b >>> [1, 2, 3]

map - map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result) >>> [2, 4, 6, 8]

two_times 함수는 리스트 요소를 입력받아 각 요소에 2를 곱한 결괏값을 돌려준다.

map 함수를 사용하면
def two_times(x): 
    return x*2
list(map(two_times, [1, 2, 3, 4])) >>> [2, 4, 6, 8]

map의 결과를 리스트로 보여 주기위해 list 함수를 사용하여 출력하였다.
리스트의 첫 번째 요소인 1이 two_times 함수의 입력값으로 들어가고 1 * 2의 과정을 거쳐서 2가 된다. 
리스트의 두 번째 요소인 2가 2 * 2 의 과정을 거쳐 4가 된다. 
따라서 결괏값 리스트는 이제 [2, 4]가 된다. 총 4개의 요솟값이 모두 수행되면 마지막으로 [2, 4, 6, 8]을 돌려준다.

lambda를 사용하면 
list(map(lambda a: a*2, [1, 2, 3, 4])) >>> [2, 4, 6, 8]

max - 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.
max([1, 2, 3]) >>> 3
max("python") >>> 'y'

min - max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.
min([1, 2, 3]) >>> 1
min("python") >>> 'h'

oct - 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
oct(34) >>> '0o42'
oct(12345) >>> '0o30071'

open - open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다. 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
w	쓰기 모드로 파일 열기
r	읽기 모드로 파일 열기
a	추가 모드로 파일 열기
b	바이너리 모드로 파일 열기

f = open("binary_file", "rb")

rb는 "바이너리 읽기 모드"

fread = open("read_mode.txt", 'r')
fread2 = open("read_mode.txt")

둘은 동일한 방법이며 모드 부분을 생략하면 기본값으로 읽기 모드 r를 갖게 된다.

fappend = open("append_mode.txt", 'a')

추가모드(a)로 파일을 여는 법

ord - 문자의 아스키 코드 값을 돌려주는 함수이다. ( chr 함수와는 반대. )
ord('a') >>> 97
ord('0') >>> 48

pow - pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
pow(2, 4) >>> 16
pow(3, 3) >>> 27

range - range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다. ( for문에서 자주 쓰임 )

list(range(5)) >>> [0, 1, 2, 3, 4]

list(range(5, 10)) >>> [5, 6, 7, 8, 9]
끝 숫자는 해당 범위에 포함되지 않는다.

list(range(1, 10, 2)) >>> [1, 3, 5, 7, 9]
list(range(0, -10, -1)) >>> [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

round - round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다. ( [, ndigits]는 ndigits가 있을 수도 있고 없을 수도 있다는 말이다. )
round(4.6) >>> 5
round(4.2) >>> 4

round(5.678, 2) >>> 5.68 ( ndigits는 반올림하여 표시하고 싶은 소수점의 자릿수이다. )

sorted - 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
sorted([3, 1, 2]) >>> [1, 2, 3]
sorted(['a', 'c', 'b']) >>> ['a', 'b', 'c']
sorted("zero") >>> ['e', 'o', 'r', 'z']
sorted((3, 2, 1)) >>> [1, 2, 3]

리스트 자료형에도 sort 함수가 잇지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.

str - 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
str(3) >>>'3'
str('hi') >>> 'hi'
str('hi'.upper()) >>> 'HI'

sum - 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
sum([1,2,3]) >>> 6
sum((4,5,6)) >>> 15

tuple - 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
tuple("abc") >>> ('a', 'b', 'c')
tuple([1, 2, 3]) >>> (1, 2, 3)
tuple((1, 2, 3)) >>> (1, 2, 3)

type - 입력값의 자료형이 무엇인지 알려 주는 함수이다.
type("abc") >>> <class 'str'>
type([ ]) >>> <class 'list'>
type(open("test", 'w')) >>> <class '_io.TextIOWrapper'>

zip - zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다. ( *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미 )
list(zip([1, 2, 3], [4, 5, 6])) >>> [(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) >>> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def")) >>> [('a', 'd'), ('b', 'e'), ('c', 'f')]








