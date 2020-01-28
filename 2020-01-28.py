## 점프 투 파이썬 - 3장 연습문제

# 1트 - 그냥 풀기

# 1. 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# ??? 문제가 이해가 가지 않는다..

# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
a = 0
while a < 1000 :
    a += 1
    if a % 3 == 0 :
        print(a)
    else :
        continue

# 1000까지 누적을 돌리면서 3의 배수를 뽑아내는건 알겠는데 누적해서 더하는 법을 잘 모르겠다.

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
*
**
***
****
*****

a = 0s
while a < 5 :
    a += 1
    print("*"*a)

# 4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1,101):
    print(i)

# 5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

# 2번과 동일하다.. for문을 이용해서 값을 가져올순 있지만 누적해서 저장하는 방법을 모르겠다.

# 6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
'''
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
'''

numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers if num % 2 == 1]
print(result) >>> [2, 6, 10]

# result 값에 넣기 위해 일렬로 쭉 바꿧다. 

# 2트 - 노트정리 보면서 풀기

# 1. 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

shirt가 출력된다. 하지만 왜 저게 나오는지 모르겠다.

''' 정답
1. 첫 번째 조건: "wife"라는 단어는 a 문자열에 없으므로 거짓이다.
2. 두 번째 조건: "python"이라는 단어는 a 문자열에 있지만 "you" 역시 a 문자열에 있으므로 거짓이다.
3. 세 번째 조건: "shirt"라는 단어가 a 문자열에 없으므로 참이다.
4. 네 번째 조건: "need"라는 단어가 a 문자열에 있으므로 참이다.
''' 

# 문제의 이해도 차이 인것같다. 정답을 보니 이해가 간다. 가장 먼저 참이 되는 조건이 출력이 되는거였다.

# 2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
a = 0
while a < 1000 :
    a += 1
    if a % 3 == 0 :
        print(a)
    else :
        continue

''' 정답
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result) >>> 166833
''' 

# 3으로 나누는 다음에는 빈 result에 i를 더해주는것이었다. 이제 누적해서 더하는게 뭔지 알거같다.

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
*
**
***
****
*****

a = 0s
while a < 5 :
    a += 1
    print("*"*a)

''' 정답
i = 0
while True:
    i += 1 # while문 수행 시 1씩 증가
    if i > 5: break     # i 값이 5이상이면 while문을 벗어난다.
    print ('*' * i)     # i 값 개수만큼 *를 출력한다.
''' 

# break문의 활용인것같다. 다양한 방법

# 4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1,101):
    print(i)

''' 정답
for i in range(1,101):
    print(i)
''' 

# 똑같다. 사람 생각은 다 똑같나보다.

# 5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

''' 정답
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score   # A학급의 점수를 모두 더한다.

average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
print(average) >>> 평균 79.0이 출력된다.
''' 

# 이것도 2번 문제와 비슷하다고 생각한다. 왜 빈 변수를 선언해줘서 거기다 더할 생각을 못했는지 

# 6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
'''
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
'''

numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers if num % 2 == 1]
print(result) >>> [2, 6, 10]

''' 정답
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result) >>> [2, 6, 10]
''' 

# 똑같다.