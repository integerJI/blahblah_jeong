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
