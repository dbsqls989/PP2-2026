# 작성자: 김윤빈
# 작성일: 2026-10-03
# 문제: 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성. PhoneBook 클래스는 딕셔너리를 이용해서 연락처를 저장함.
# 설계: PhoneBook 클래스를 정의하고 contacts 딕셔너리에 이름을 key로, 휴대폰 번호, 직장 전화번호, 이메일 주소를 value로 저장. add 메소드를 이용하여 연락처를 추가.


class PhoneBook:
    def __init__(self):
        self.contacts={}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name]= (mobile, office, email)

    def __str__(self):
        result = ""

        for name, contact in self.contacts.items():
            mobile, office, email = contact

            result += name + "\n"
            result += "office phone: " + str(office) + "\n"
            result += "email address: " + str(email) + "\n"


        return result

def test_prob7():
    obj = PhoneBook()

    obj.add("Kim",office="1234567",email="kim@company.com")
    obj.add("Park",office="2345678",email="park@company.com")

    print(obj)

if __name__=="__main__":
    test_prob7()
