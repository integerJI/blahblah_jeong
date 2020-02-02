## 점프 투 파이썬 - 클래스

# 클래스가 필요한 이유

굳이 클래스가 없어도 프로그램은 충분히 만들 수 있다. 그러므로 프로그램 작성을 위해 꼭 필요한 요소는 아니다.
하지만 클래스를 적재적소에 사용하면 훨씬 많은 이익을 얻을 수 있다.

계산기로 예를 들어보자. 계산기에 3을 입력하고 +기호를 눌러 4를 입력하면 7이 나온다.
다시한번 + 기호와 3을 입력하면 10이 나온다.

즉 계산기는 이전에 계산한 결괏값을 항상 메모리 어딘가에 저장하고 있어야 한다는 소리이다.

# 더하기 기능의 함수

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3)) >>> 3
print(add(4)) >>> 7

# 이전에 계산한 결괏값을 유지하기 위해 result 전역변수를 사용했다.
# 그런데 만일 2개의 계산기가 필요한 상황이 발생하면 계산기는 각각의 결괏값을 유지하기 때문에 add함수 하나만으로는 결괏값을 따로 유지할 수 없다.

# 2개의 값을 받기 위한 add 함수

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3)) >>> 3
print(add1(4)) >>> 7
print(add2(3)) >>> 3
print(add2(7)) >>> 10

# add1의 결괏값이 add2에 아무 영향을 끼치지 않음을 확인할수 있지만 계산기가 2개 이상으로 많이 필요해진다면? 더욱더 빼기나 곱하기 기능을 추가해야한다면 코드는 더욱더 복잡하고 어려워질것이다.

# 그래서 클래스를 사용한다.

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3)) >>> 3
print(cal1.add(4)) >>> 7
print(cal2.add(3)) >>> 3
print(cal2.add(7)) >>> 10

# Calculator 클래스로 만든 별개의 계산기 cal1,cal2(객체)가 각각 역할을 수행해 독립된 값을 유지할수 있게 된다.
# 클래스를 사용하면 계산기 대수가 늘어나더라도 객체를 생성만 하면 되기 때문에 함수를 사용하는 경우와 달리 매우 간단해진다.

# 빼기가 필요한 경우

    def sub(self, num):
        self.result -= num
        return self.result

# 뺄셈 기능을 추가해주면 된다.

# 클래스와 객체

클래스는 틀이다. 객체는 틀에서 나온 과자이다. >>> 제일 많이들었던 붕어빵틀들 ;;

여기서 클래스란 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면이고
객체란 클래스로 만든 피조물을 뜻한다.

클래스로 만든 객체에는 중요한 특징이 있다.
그것은 객체마다 고유한 성격을 가진다는 뜻이다.
하나의 붕어빵틀로 슈크림 붕어빵도 만들고 팥빵 붕어빵도 만들수있다는 소리이다.

# 클래스의 예
class Cookie:
   pass

아무 기능이 없는 클래스 Cookie를 만들었다. 이제 이 클래스는 많은 객체를 만들어낼 수 있다.
a = Cookie()
b = Cookie()

Cookie()의 결괏값을 돌려받은 a와 b가 바로 객체이다.

# 객체와 인스턴스의 차이
클래스로 만든 객체를 인스턴스라고도 한다.
 a = Cookie() 이렇게 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다. 즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다. "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 "a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.
라고한다.

# 어렵네;






















