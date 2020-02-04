## 점프 투 파이썬 - 클래스

# 생성자 
저번에 만든 FourCal 클래스를 사용해보자. 

a = FourCal() 
a.add() >>> 
Traceback (most recent call last): 
  File "", line 1, in  
  File "", line 6, in add 
AttributeError: 'FourCal' object has no attribute 'first' 

그러면 에러가 날것이다. 

FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 수행하면 생기는 오류이다. 
이 오류는 setdata 메서드를 수행해야 객체 a의 객체 변수 first와 second가 생성되기 때문이다. 

이렇게 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다. 

생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다. 

파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다.  
__init__ 메서드의 init 앞뒤로 붙은 __는 언더스코어(_) 두 개를 붙여 쓴 것이다. 

__init__를 FourCal 클래스에 생성자를 추가해 보면 
class FourCal: 
    def __init__(self, first, second): 
        self.first = first 
        self.second = second 
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

>>> 

__init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 
단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

이제 다음과 같이 명령어를 입력하면 
a = FourCal() 
Traceback (most recent call last): 
  File "", line 1, in  
TypeError: __init__() missing 2 required positional arguments: 'first' and 'second' 

에러가 난다.

a = FourCal()을 수행할 때 생성자 __init__이 호출되어 위와 같은 오류가 발생했다. 오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다. 

이 오류를 해결하려면.. 

a = FourCal(4, 2) 

first와 second에 해당되는 값을 전달하여 객체를 생성해야 한다. 
이렇게 입력되면 __init__메서드의 매개변수에는 

self = 생성되는 객체 , first = 4 , second = 2 

이렇게 대입된다. 

__init__ 메서드도 다른 메서드와 마찬가지로 첫 번째 매개변수 self에 생성되는 객체가 자동으로 전달된다. 

따라서 __init__ 메서드가 호출되면 setdata 메서드를 호출했을 때와 마찬가지로 first와 second라는 객체 변수가 생성될 것이다. 

a = FourCal(4, 2) 
print(a.first) >>> 4 

print(a.second) >>> 2 

# 클래스의 상속 
상속 개념을 사용하여 FourCal 클래스에 a^b 기능을 추가한다. 
MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있어야 한다. 
class MoreFourCal(FourCal): 
    pass 

FourCal 클래스를 상속하는 MoreFourCal 클래스를 만든다. 

클래스를 상속하기 위해서는 
class 클래스 이름(상속할 클래스 이름) 

# 확인해보기 
a = MoreFourCal(4, 2) 
a.add() >>> 6 

등등 상속받은 FourCal 클래스의 모든 기능을 사용할 수 있다. 

# 상속을 하는 이유 
보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다. 
기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다. 

a^b를 계산하는 MoreFourCal 클래스 만들기 
class MoreFourCal(FourCal): 
    def pow(self): 
        result = self.first ** self.second 
        return result 

pass 문장은 삭제하고 위와 같이 두 수의 거듭제곱을 구할 수 있는 pow 메서드를 추가 

a = MoreFourCal(4, 2) 
a.pow() >>> 16 

MoreFourCal 클래스로 만든 a 객체에 값 4와 2를 설정한 후 pow 메서드를 호출하면 4의 2 제곱 (42)인 16을 돌려주는 것을 확인할 수 있다. 

상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용한다. 

# 메서드 오버라이딩 
FourCal 클래스를 다음과 같이 실행해 보면... 

a = FourCal(4, 0) 
a.div() >>>  
Traceback (most recent call last): 
  File "", line 1, in  
    result = self.first / self.second 
ZeroDivisionError: division by zero 

또 오류다.. FourCal 클래스의 객체 a에 4와 0 값을 설정하고 div 메서드를 호출하면 4를 0으로 나누려고 하기 때문에 위와 같은 오류가 발생한 거란다.

그래서 0으로 나눠도 오류가 아니라 0을 돌려주게 만들어야 해서 하는 방법 

FourCal 클래스를 상속하는 SafeFourCal 클래스를 만든다. 

class SafeFourCal(FourCal): 
    def div(self): 
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정 
            return 0 
        else: 
            return self.first / self.second 

SafeFourCal 클래스는 FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성하였다. 이렇게 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버 라이딩(Overriding, 덮어쓰기)이라고 한다. 이렇게 메서드를 오버 라이딩하면 부모 클래스의 메서드 대신 오버 라이딩한 메서드가 호출된다. 

SafeFourCal 클래스에 오버라이딩한 div 메서드는 나누는 값이 0인 경우에는 0을 돌려주도록 수정했다. 확인해보면 

a = SafeFourCal(4, 0) 
a.div() >>> 0 

아까와는 달리 오류가 아니라 0이 나온다. 


# 클래스 변수 
객체 변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지한다는 점을 이미 알아보았다. 이번에는 객체 변수와는 성격이 다른 클래스 변수에 대해 알아보자. 
class Family: 
    lastname = "김" 

Family 클래스에 선언한 lastname이 바로 클래스 변수이다. 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다. 사용해보면 

print(Family.lastname) >>> 김 

클래스 변수는 위 예와 같이 클래스이름.클래스 변수로 사용할 수 있다. 

또는 다음과 같이 Family 클래스로 만든 객체를 통해서도 클래스 변수를 사용할 수 있다. 

a = Family() 
b = Family() 
print(a.lastname) >>> 김 
print(b.lastname) >>> 김 

이 상태에서 Family 클래스의 lastname을 다음과 같이 "박"이라는 문자열로 바꾸면 

Family.lastname = "박" 
print(a.lastname) >>> 박 
print(b.lastname) >>> 박 

클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값도 모두 변경된다.  
즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다. 

id함수를 사용해 증명해 보자. 
id(Family.lastname) >>> 4480159136 
id(a.lastname) >>> 4480159136 
id(b.lastname) >>>4480159136 

id 값이 모두 같으므로 Family.lastname, a.lastname, b.lastname은 모두 같은 메모리를 가리키고 있다. 

클래스에서 클래스 변수보다는 객체 변수가 훨씬 중요하다.  

--- 

클래스 중요하다. 


