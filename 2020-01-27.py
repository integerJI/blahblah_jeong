## 점프 투 파이썬 - for문

# for문의 기본 구조
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ... # 처음 봤을땐 어려웠지만 이젠 익숙. 리스트를 in 변수에 끝 -

# for문의 예제
test_list = ['one', 'two', 'three'] 
for i in test_list: # 리스트에 있는 값들을 i에 넣어라
    print(i) # i 출력
one 
two 
three # 다 돌면 끝난다. 

a = [(1,2), (3,4), (5,6)]
for (first, last) in a: # 두개씩 따로 넣을수도 있다.
    print(first + last) # 그 값을 더할수도 있음
3
7
11 # 끝

# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."
marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 # 몇 번째 학생인지 카운트 한다.
    if mark >= 60: # for문 안의 if 문
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
>>>
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.

# for문과 continue
marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue # mark의 값이 60보다 이하면 지나간다. 
    print("%d번 학생 축하합니다. 합격입니다. " % number) # 합격한 학생만 남게되어 합격한 학생만 출력된다.
>>>
1번 학생 축하합니다. 합격입니다.
3번 학생 축하합니다. 합격입니다.
5번 학생 축하합니다. 합격입니다.

# for문과 함께 자주 사용하는 range 함수
a = range(10)
a >>> range(0, 10) # 0 부터 10 미만의 숫자를 출력한다.

# range 함수의 예시
add = 0 # add를 0으로 초기화
for i in range(1, 11): # i에 1부터 11미만의 숫자를 넣어라
    add = add + i # 마찬가지로 add += i 로 가능
print(add) >>> 55 # 1부터 10까지의 더한값이 출력

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
# len 함수는 리스트 안의 요소 개수를 돌려주는 함수이다. 
# 따라서 len(marks)는 5가 될 것이고 range(len(marks))는 range(5)가 될 것이다. 
# number 변수에는 차례로 0부터 4까지의 숫자가 대입될 것이고, marks[number]는 차례대로 90, 25, 67, 45, 80 값을 갖게 된다. 결과는 다른 for문 예제와 동일하다.

# for와 range를 이용한 구구단
for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ") # 1번 * 2번 끝나면 공백
    print('') # 한줄 계산이 끝나면 줄바꿈을 해준다.

# 리스트 내포 사용하기
# *** 좀 헷갈림 어려움
# 리스트 안에 for문을 포함하는 리스트 내포(List comprehension)를 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다. 다음 예제를 보자.
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3) # num에 3을 곱한 값을 result에 추가한다.
print(result) >>> [3, 6, 9, 12]

# 이렇게 for문을 사용하는 더 편하게 바꿀 수 있다.
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result) >>> [3, 6, 9, 12]

# if문를 추가하여 원하는 데이터 뽑아내기
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0] # 만약에 2로 나눴을때 나머지가 0이면 걸러라
print(result) >>> [6, 12]

# 리스트 내포의 일반 문법
[표현식 for 항목 in 반복가능객체 if 조건문]

# 구구단의 리스트 내포 활용
result = [x*y for x in range(2,10)
              for y in range(1,10)] # for문을 두개 이상 사용할 수 있다.
print(result)
>>>
[2, 4, 6, 8, 10, ... 45, 54, 63, 72, 81]

---
갑자기 리스트를..? 좀 당황
리스트랑 다시봐야겠다.

내일은 연습문제