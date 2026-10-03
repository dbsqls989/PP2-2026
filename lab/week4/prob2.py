# 작성자: 김윤빈
# 작성일: 2026-10-01
# 문제: 로켓을 나타내는 Rocket 클래스를 작성. Rocket 클래스는 인스턴스 변수와 메소드를 가짐
# 설계: Rocket 클래스를 정의하고, 로켓의 현재 위치, 생성자 함수, 이동 메소드, 현재 위치를 반환하는 메소드를 구현.

class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x  # 로켓의 현재 위치 x 좌표
        self.y = y  # 로켓의 현재 위치 y 좌표


    def __str__(self):
        return f"({self.x}, {self.y})"

    def moveUp(self):
        self.y += 1  # 로켓을 위로 이동

def test_prob2():
    myRocket = Rocket()  # Rocket 클래스의 인스턴스 생성

    print("로켓의 높이: ", myRocket.y)
    
    myRocket.moveUp()
    print("로켓의 높이: ", myRocket.y)  # 출력: (0, 1)

if __name__ == "__main__":
    test_prob2()