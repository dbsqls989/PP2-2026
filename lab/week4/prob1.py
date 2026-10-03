# 작성자: 김윤빈
# 작성일: 2026-10-01
# 문제: 고양이를 클래스로 정의하고 인스턴스 설정하기. 접근자와 설정자 사용.
# 설계: Cat 클래스를 정의하고, 이름과 나이를 속성으로 설정. 접근자와 설정자를 통해 속성에 접근 및 수정.

class Cat:
    def __init__(self, name, age):
        self.__name = name  # 속성
        self.__age = age

    def get_name(self):   #접근자 
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):  #설정자
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return f"{self.__name} {self.__age}"

def test_prob1():
    missy = Cat("Missy", 3) # Cat 클래스의 인스턴스 생성
    lucky = Cat("Lucky", 5)

    print(missy)  # 출력: Missy 3
    print(lucky)  # 출력: Lucky 5

if __name__ == "__main__":
    test_prob1()