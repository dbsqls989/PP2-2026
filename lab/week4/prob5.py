# 작성자: 김윤빈
# 작성일: 2026-10-01
# 문제: 삼각형을 나타내는 Triangle 클래스를 작성. Triangle 클래스는 삼각형의 각 각도, 변의 개수를 인스턴스 변수로 가짐.
# 설계: Triangle 클래스를 정의하고 angle1, angle2, angle3를 인스턴스 변수로 설정하고 세 각도를 인스턴스 변수로 설정. 접근자와 설정자를 통해 각 각도에 접근 및 수정하고, checkAngles를 통해 세 각도의 합이 180도인지 확인.
class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.__angle1 = angle1 
        self.__angle2 = angle2
        self.__angle3 = angle3

    def __str__(self):
        return f"({self.__angle1},{self.__angle2},{self.__angle3})"

    def setAngle1(self, angle1):
        self.__angle1 = angle1

    def setAngle2(self, angle2):
        self.__angle2 = angle2

    def setAngle3(self, angle3):
        self.__angle3 = angle3

    def getAngle1(self):
            return self.__angle1

    def getAngle2(self):
        return self.__angle2

    def getAngle3(self):
            return self.__angle3
    
    def checkAngles(self):
        if self.__angle1 + self.__angle2 + self.__angle3 ==180:
            return True
        else:
            return False


def test_prob5():
    triangle=Triangle(90, 30, 60)

    print(triangle.checkAngles())


if __name__ == "__main__":
    test_prob5()