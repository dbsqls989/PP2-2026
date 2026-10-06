# 작성자: 김윤빈
# 작성일: 2026-10-01
# 문제: 사각형을 나타내는 Rectangle 클래스를 작성. Rectangle 클래스는 좌측 상단 좌표, 너비와 높이를 인스턴스 변수로 가짐.
# 설계: Rectangle 클래스를 정의하고, x, y, width, height를 인스턴스 변수로 설정
#       overLap()으로 두 사각형이 서로 겹치는지 확인.

class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"({self.x},{self.y}, {self.width}, {self.height})"

    def setX(self,x):
        self.x=x

    def setY(self,y):
        self.y=y

    def setWidth(self,width):
        self.width=width

    def setHeight(self,height):
        self.height=height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

    def overLap(self, r):
        if (self.x + self.width < r.x or r.x + r.width < self.x or self.y + self.height < r.y or r.y + r.height < self.y):
            return False
        else:
            return True

def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle (10, 10, 100, 100)

    if r1.overLap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")

if __name__ == "__main__":
    test_prob4()
    