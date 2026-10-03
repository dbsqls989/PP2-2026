# 작성자: 김윤빈
# 작성일: 2026-10-03
# 문제: printSong이라는 클래스 작성. printSong의 생성자는 노래의 가사를 리스트 형태로 받아서 객체의 내부에 저장. sing() 메소드는 한 줄에 한 항목씩 저장
# 설계: Song 클래스를 정의하고 생산자에서 가사 리스트를 저장. sing() 메소드에서 반복문을 이용하여 가사를 한줄씩 작성

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics


    def sing(self):
        for line in self.lyrics:
            print(line)

def test_prob8():
    aSong = Song(["TWINKLE, twinkle, little star,",
                  "How I wonder what are you!" 
                  "Up above the world so high," 
                  "Like a diamond in the sky."])

    aSong.sing()

if __name__=="__main__":
    test_prob8()


