## 점프 투 파이썬 - 클래스

# 사칙연산 클래스 만들기 
클래스를 구상할 때에는 클래스로 만든 객체 중심으로 동작할 방향을 구상한 후에 하나씩 해결해 나가는 것이 좋다. 

사칙연산을 가능하게하는 FourCal 클래스가 있다면 

a = FourCal() >>> a라는 객체를 만든다. 

a.setdata(4,2) >>> 숫자 4와 2를 a에 지정해준다. 

print(a.add()) >>> 두 수를 합한 결과 4 + 2를 돌려주고 = 6 

print(a.mul()) >>> 곱한 결과

print(a.sub()) >>> 뺄셈 

print(a.div()) >>> 나누기 

이렇게 동작하는 FourCal 클래스를 만드는 것이 목표이다. 

# 클래스 구조 만들기 

앞서 구상한 것처럼 클래스를 만들어 보면 

제일 먼저 할 일은 a = FourCal()처럼 객체를 만들 수 있게 해주어야 한다. 

class FourCal : 
pass 

현재 FourCal 클래스는 아무 변수나 함수도 포함하지 않지만 객체 a를 만들 수 있는 기능을 가지고 있다. 

a = FourCal() 
type(a) 
<class '__main__.FourCal'> 

type를 이용해서 객체 타입을 출력해 보면 FourCal 클래스의 객체임을 알 수 있다. 

# 객체에 숫자 지정할 수 있게 만들기 

이제 사칙연산을 넣어주면 된다. 사칙연산을 하려면 2개의 숫자가 있어야 한다. 연산을 수행할 대상을 객체에 지정할 수 있게 만들어보자. 

a.setdata(4,2) 

위 문장을 수행하려면.. 

class FourCal : 
    def setdata(self, first, second): # 메서드 
       self.first = first 
        self.second  = second 

앞서 만든 FourCal 클래스에서 pass를 삭제하고 대신 setdata 함수를 만들었다. 
클래스 안에서 구현된 함수는 메서드라고 부른다. 

setdata의 메서드를 다시 보면

def setdata(self, first, second): # 1 메서드의 매개변수 
    self.first = first # 2 메서드의 수행문 
    self.second = second # 3 메서드의 수행문 

1. setdata 메서드의 매개변수 

setdata 메서드는 매개변수로 self, first, second 3개의 입력값을 받는다. 
하지만 일반 함수와는 달리 메서드의 첫 번째 매개변수 self는 특별한 의미가 있다. 

예를 들어

a = FourCal() 
a.setdata(4,2) 

setdata 메서드에는 self, first, second 총 3개의 매개변수가 필요한데 실제로는 a.setdata(4, 2)처럼 2개 값만 전달했다. 
그 이유는 a.setdata(4, 2)처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달되기 때문이다. 

a는 self에 들어가며 4는 first, 2는 second에 들어가게 된다. 

파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.  
객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한 것이다.  
물론 self 말고 다른 이름을 사용해도 상관없다. 

# 여러가지 메서드의 호출 방법 

a = FourCal() 
FourCal.setdata(a, 4, 2) 

위와 같이 클래스 이름. 메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 한다.  
반면에 다음처럼 객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다. 

a = FourCal() 
a.setdata(4, 2) 

2. setdata 메서드의 수행문 

def setdata(self, first, second): # 1 메서드의 매개변수 
    self.first = first # 2 메서드의 수행문 
    self.second = second # 3 메서드의 수행문 

a.setdata(4, 2)처럼 호출하면 setdata 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달되어 setdata 메서드의 수행문은 다음과 같다. 

self.first = 4 
self.second = 2 

self는 전달된 객체 a이므로  

a.first = 4 
a.second = 2 

a.first = 4 문장이 수행되면 a 객체에 객체 변수 first가 생성되고 값 4가 저장된다.  
마찬가지로 a.second = 2 문장이 수행되면 a 객체에 객체 변수 second가 생성되고 값 2가 저장된다. 

객체에 생성되는 객체만의 변수를 객체변수라고 부른다. 

a = FourCal() 
a.setdata(4, 2) 

print(a.first) >>> 4 

print(a.second) >>> 2 

a 객체에 객체 변수 first와 second가 생성되었다. 

이어서 a, b 객체를 만들어 보고 

a = FourCal() 
b = FourCal() 

a 객체의 객체변수 first를 생성한다. 
a.setdata(4, 2) 
print(a.first) >>> 4 

이번에는 b 객체의 객체 변수 first를 생성한다. 
b.setdata(3, 7) 
print(b.first) >>> 3 

위와 같이 진행하면 b 객체의 객체 변수 first에는 값 3이 저장된다는 것을 확인할 수 있다. 

그렇다면 a 객체의 first는 3으로 변할까? 아니면 기존 값 4를 유지할까? 

print(a.first) >>> 4 

a 객체의 first 값은 b 객체의 first 값에 영향받지 않고 원래 값을 유지하고 있다. 

여기서 중요한 점이 클래스로 만든 객체의 객체 변수는 다른 객체의 객체 변수에 상관없이 독립적인 값을 유지한다는 것이다. 

id 함수를 사용하면 객체변수가 독립적인 값을 유지한다는 점을 좀 더 명확하게 증명해 보일 수 있다. 

id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수이다. 

a = FourCal() 
b = FourCal() 


a.setdata(4, 2) 
b.setdata(3, 7) 


id(a.first)   # a의 first 주소 값을 확인 
 >>> 1839194944 
id(b.first)   # b의 first 주소값을 확인 
 >>> 1839194928 

a 객체의 first 주소 값과 b 객체의 first 주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있다. 
객체변수는 그 객체의 고유 값을 저장할 수 있는 공간이다.  
객체 변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다는 점!! 

다음은 현재까지 완성된 FourCal 클래스이다. 

def setdata(self, first, second): # 1 메서드의 매개변수 
    self.first = first # 2 메서드의 수행문 
    self.second = second # 3 메서드의 수행문 

# 아직... 클래스만 완성.. 

# 더하기 기능 만들기 
a = FourCal() 
a.setdata(4, 2) 
print(a.add()) >>> 6 

다음과 같이 더하기 기능을 만들 것이다. 
class FourCal: 
def setdata(self, first, second): 
self.first = first 
self.second = second 
def add(self): 
result = self.first + self.second 
return result 

add 메서드가 새롭게 추가되었다. 추가된 메서드를 사용해 보면 

a = FourCal() 
a.setdata(4, 2) 

위와 같이 호출하면 앞에서 살펴보았듯이 a객체의 first, second 객체 변수에는 각각 값 4와 2가 저장될 것이다. 

메서드를 호출해 보자. 

print(a.add()) >>> 6 

a.add()라고 호출하면 add 메서드가 호출되어 값 6이 출력된다. 
어떤 과정을 거쳐 값 6이 출력되는지 add 메서드를 따로 떼어 내서 보자. 
def add(self): 
result = self.first + self.second 
return result 

add 메서드의 매개변수는 self이고 반환 값은 result이다. 반환 값인 result를 계산하는 부분은 다음과 같다. 

result = self.first + self.second 

a.add()와 같이 a 객체에 의해 add 메서드가 수행되면 add 메서드의 self에는 객체 a가 자동으로 입력되므로 위 내용은 다음과 같이 해석한다. 

result = a.first + a.second 

위 내용은 a.add() 메서드 호출 전에 a.setdata(4, 2) 가 먼저 호출되어 a.first = 4, a.second = 2라고 이미 설정되었기 때문에 다시 다음과 같이 해석한다. 

result = 4 + 2 

그래서 a.add() 를 호출하면 6을 돌려주는 것이다.


# 우엑

# 곱하기, 빼기, 나누기 기능 만들기 
class FourCal: 
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self): 
        result = self.first + self.second 
        return result 
    def mul(self): 
        result = self.first * self.second 
        return result 
    def sub(self): 
        result = self.first - self.second 
        return result 
    def div(self): 
        result = self.first / self.second 
        return result 

# 실행 

a = FourCal() 
b = FourCal() 

a.setdata(4, 2) 
b.setdata(3, 8) 

# 끝 

--- 

클래스가 진짜 중요하다 생각한다. 

조금 늦더라고 천천히 제대로 이해 가고 가야 한다.



