# 생성자 함수의 이름은 __init__ 으로 고정되어 있음
# 생성자는 생성시에 호출되는 함수

# self : 내부 인자에 자기 자신을 넘겨줌

# 데이터를 저장하고 싶은데, 생성자에 데이터를 받고 싶음 -> 생성자에 param_name 추가
# 클래스 내에 name 이라는 변수를 만들어서 받은 데이터인 param_name을 저장해줌

# 클래스 내부의 함수는 메소드(method) 라고 부름, talk 라는 메소드를 만들어 보면,
# 각 객체의 변수를 사용해서 메소드를 구현할 수 있음

class Person:
    def __init__(self, param_name):
        self.name = param_name
        print("I am created !", self)

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다")


person_1 = Person("LSJ")
print(person_1.name)
person_2 = Person("KYM")
print(person_2.name)