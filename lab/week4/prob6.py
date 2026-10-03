# 작성자: 김윤빈
# 작성일: 2026-10-02
# 문제: Person 클래스를 작성. Person 클래스는 이름, 핸드폰 번호, 직장 전화번호, 이메일 주소를 인스턴스 변수로 가짐.
# 설계: Person 클래스를 정의하고 이름, 핸드폰 번호, 직장 전화번호, 이메일 주소를 인스턴스 변수로 설정. 접근자와 설정자를 통해 속성에 접근 및 수정.

class Person:
    def __init__(self, name, mobile="", office="", email=""):
        self.__name = name
        self.__mobile = mobile
        self.__office = office
        self.__email = email

    def __str__(self):
        return f"{self.__name},{self.__mobile},{self.__office},{self.__email}"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setMobile(self,mobile):
        self.__mobile = mobile

    def getMobile(self):
        return self.__mobile

    def setOffice(self,office):
        self.__office = office

    def getOffice(self):
        return self.__office

    def setEmail(self,email):
        self.__email = email

    def getEmail(self):
        return self.__email


def test_prob6():
    p1 = Person("Kim",office="1234567",email="kim@company.com")
    p2 = Person("Park",office="2345678")

    p2.setEmail("park@company.com")

    print(p1)
    print(p2)

if __name__ == "__main__":
    test_prob6()

    