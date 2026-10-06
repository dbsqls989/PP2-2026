# 작성자: 김윤빈
# 작성일: 2026-10-01
# 문제: 상자를 나타내는 Box 클래스 작성. Box 클래스는 가로길이, 세로길이, 높이를 나타내는 인스턴스 변수를 가진다.
# 설계: Box 클래스를 정의하고 가로, 세로, 높이를 인스턴스 변수로 설정. 접근자와 설정자를 통해 속성에 접근 및 수정. 가로, 세로, 높이를 곱하여 상자의 부피를 계산

class Box:
    def __init__(self, length, height, depth):
        self.__length = length  # 가로길이
        self.__height = height  # 세로길이
        self.__depth = depth  # 높이

    def __str__(self):
        return f"({self.__length},{self.__height},{self.__depth})"

    def setlength(self, length):
        self.__length = length

    def getlength(self):
        return self.__length

    def setheight(self, height):
        self.__height = height

    def getheight(self):
        return self.__height

    def setdepth(self, depth):
        self.__depth = depth

    def getdepth(self):
        return self.__depth

def test_prob3():
    b1 = Box(100,100,100)

    print(b1)

    volume = b1.getlength() * b1.getheight() * b1.getdepth()

    print("상자의 부피는",volume)

if __name__ == "__main__":
        test_prob3()