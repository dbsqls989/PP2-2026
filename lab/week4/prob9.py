# 작성자: 김윤빈
# 작성일: 2026-10-03
# 문제: 터틀 그래픽에서 각각의 거북이는 객체. 2개의 거북이를 생성해서 서로 다른 방향으로 움직이게 하기
# 설계: turtle 모듈을 이용하여 2개의 Turtle 객체를 생성하고, 각 객체의 이동 방향을 다르게 설정하여 움직이도록 한다.

import turtle

def test_prob9():
    lee=turtle.Turtle()
    kim=turtle.Turtle()

    lee.shape("turtle")
    kim.shape("turtle")

    lee.forward(100)
    lee.right(90)
    lee.forward(100)
    lee.left(90)
    lee.forward(100)

    kim.left(90)
    kim.forward(100)
    kim.right(90)
    kim.forward(100)

    turtle.done()

if __name__=="__main__":
    test_prob9()