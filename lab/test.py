import turtle

# =========================
# 1. BMI 계산 함수
# =========================
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi


# =========================
# 2. BMI 판정 함수
# =========================
def get_status(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    else:
        return "비만"


# =========================
# 3. health.txt 파일 읽기
# =========================
def read_health_file(filename):
    people = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # 빈 줄이면 건너뛰기
            if not line:
                continue

            data = line.split()

            # 데이터는 전화번호, 이름, 키, 몸무게
            if len(data) != 4:
                continue

            phone = data[0]
            name = data[1]

            # 첫 줄이 제목인 경우 등을 건너뛰기
            try:
                height = float(data[2])
                weight = float(data[3])
            except ValueError:
                continue

            bmi = calculate_bmi(height, weight)
            status = get_status(bmi)

            people.append([
                phone,
                name,
                height,
                weight,
                bmi,
                status
            ])

    return people


# =========================
# 4. Turtle로 사각형 그리기
# =========================
def draw_rectangle(t, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)


# =========================
# 5. Turtle로 글자 출력하기
# =========================
def write_text(t, text, x, y, font_size=10):
    t.penup()
    t.goto(x, y)
    t.write(
        str(text),
        align="center",
        font=("Arial", font_size, "normal")
    )


# =========================
# 6. 표 그리기
# =========================
def draw_table(people):
    screen = turtle.Screen()
    screen.title("BMI 건강 관리 프로그램")
    screen.setup(width=1000, height=700)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # 표 제목
    write_text(t, "BMI 건강 관리 프로그램", 0, 280, 20)

    headers = [
        "전화번호",
        "이름",
        "키(cm)",
        "몸무게(kg)",
        "BMI",
        "소견"
    ]

    # 각 열의 너비
    widths = [180, 100, 100, 120, 100, 100]

    row_height = 40

    # 표 전체 너비
    total_width = sum(widths)

    # 표 시작 위치
    start_x = -total_width / 2
    start_y = 220

    # -------------------------
    # 제목 행 그리기
    # -------------------------
    x = start_x

    for i in range(len(headers)):
        draw_rectangle(
            t,
            x,
            start_y,
            widths[i],
            row_height
        )

        write_text(
            t,
            headers[i],
            x + widths[i] / 2,
            start_y - 27,
            10
        )

        x += widths[i]

    # -------------------------
    # 사람 데이터 출력
    # -------------------------
    y = start_y - row_height

    for person in people:

        phone = person[0]
        name = person[1]
        height = person[2]
        weight = person[3]
        bmi = person[4]
        status = person[5]

        row_data = [
            phone,
            name,
            f"{height:g}",
            f"{weight:g}",
            f"{bmi:.1f}",
            status
        ]

        x = start_x

        for i in range(len(row_data)):
            draw_rectangle(
                t,
                x,
                y,
                widths[i],
                row_height
            )

            write_text(
                t,
                row_data[i],
                x + widths[i] / 2,
                y - 27,
                10
            )

            x += widths[i]

        y -= row_height

    turtle.done()


# =========================
# 7. 프로그램 시작
# =========================
def main():
    people = read_health_file("health.txt")

    if len(people) == 0:
        print("health.txt에서 데이터를 읽지 못했습니다.")
        return

    # 터미널에서도 확인
    print("전화번호\t이름\t키\t몸무게\tBMI\t소견")

    for person in people:
        print(
            person[0],
            person[1],
            person[2],
            person[3],
            f"{person[4]:.1f}",
            person[5]
        )

    # Turtle 표 출력
    draw_table(people)


if __name__ == "__main__":
    main()