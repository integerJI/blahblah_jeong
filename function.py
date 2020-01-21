# 문자열 함수
a = "Happy"

# 문자열 길이 구하기 (len)
len(a) >>> 5

# 문자 개수 세기(count)
a.count('p') >>> 2

# 위치 알려주기1(find)
a.find('a') >>> 1
a.find('q') >>> -1 # 문자열이 존재하지 않는다면 -1을 반환

# 위치 알려주기2(index)
a.index('a') >>> 1
a.index('q') >>> error # 문자열이 존재하지 않는다면 오류 발생

# 문자열 삽입(join)
",".join('abcd') >>> 'a,b,c,d'
",".join(['a', 'b', 'c', 'd']) >>> 'a,b,c,d' # 튜플도 가능

# 소문자를 대문자로 바꾸기(upper)
a.upper() >>> 'HAPPY'

# 대문자를 소문자로 바꾸기(lower)
a.lower() >>> 'happy'

# 공백 지우기(strip)
a = " hi "
a.strip() >>> 'hi' # 공백 지우기
a.lstrip() >>> 'hi ' # 왼쪽 공백 지우기
a.rstrip() >>> ' hi' # 오른쪽 공백 지우기

# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg") >>> 'Your leg is too short'

# 문자열 나누기(split)
a = "Life is too short"
a.split() >>> ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':') >>> ['a', 'b', 'c', 'd'] # 지정된 문자 기준으로 나눌 수 있다.

print("="*50)

# 리스트 함수
a = [1,2,3]

# 리스트에 요소 추가(append)
a.append(4) 
a >>> [1,2,3,4]
a.append([5,6])
a >>> [1,2,3,4,[5,6]] # 리스트 추가 가능

# 리스트 정렬(sort)

a = [5,3,7,2]
a.sort()
a >>> [2,3,5,7] # 알파벳도 가능

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
a >>> ['b', 'c', 'a']

# 위치 반환(index)
a = [1,2,3]
a.index(3) >>> 2
a.index(1) >>> 0
a.index(0) >>> error # 없는 값을 부를경우 오류(ValueError)가 난다.

# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
a >>> [4, 1, 2, 3] # 0번째 위치에 4를 추가해라
a.insert(3, 5)
a >>> [4, 1, 2, 5, 3] # 3번째 위치에 5를 삽입해라

# 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a >>> [1, 2, 1, 2, 3] # 맨 첫번째 부터 제거된다.

# 리스트 요소 끄집어내기(pop)
a = [1,2,3]
a.pop() >>> 3
a >>> [1, 2] # 맨 마지막을 제거한다.
a.pop(1) >>> 2
a >>> [1] # pop(x) x의 위치에 있는 값을 리스트에서 제거한다.

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
a.count(1) >>> 2 # 1이 두개있다고 알려준다.

# 리스트 확장(extend)
a = [1,2,3]
a.extend([4,5]) # == a += [4,5]와 동일하다.
a >>> [1, 2, 3, 4, 5] # extend(x)는 x의 값에 리스트만 올수있다.


