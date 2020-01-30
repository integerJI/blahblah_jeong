## 점프 투 파이썬 - 사용자 입력과 출력

# input의 사용
a = input() >>> Life is too short, you need python

a >>> 'Life is too short, you need python'

number = input("숫자를 입력하세요: ") >>> 숫자를 입력하세요:  3

print(number) >>> 3

# print 자세히 알기

a = 123
print(a) >>> 123

a = "Python"
print(a) >>> Python

a = [1, 2, 3]
print(a) >>> [1, 2, 3]

# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short") >>> lifeistoo short  # 1

print("life"+"is"+"too short") >>> lifeistoo short # 2

# 위 예에서 1과 2는 완전히 동일한 결괏값을 출력한다. 즉 따옴표로 둘러싸인 문자열을 연속해서 쓰면 + 연산을 한 것과 같다.

# 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short") >>> life is too short

# 한 줄에 결괏값 출력하기
for i in range(10):
print(i, end=' ') >>> 0 1 2 3 4 5 6 7 8 9

for문을 배울 때 만들었던 구구단 프로그램에서 보았듯이 한 줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다.

 * 휴 .. 오늘은 야근.. 지하철역에서 급하게 깃푸시한다.
