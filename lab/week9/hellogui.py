import tkinter as tk       #tkinter 모듈을 포함

window = tk.Tk()               #루트 윈도우를 생성
window.title("Hello 김윤빈") 
window.geometry("400x200")  

label = tk.Label(window,text="Hello,GUI")  #레이블 위젯을 생성
label.pack()                            #레이블 위젯을 윈도우에 배치

window.mainloop()                       #윈도우가 사용자 동작을 대기