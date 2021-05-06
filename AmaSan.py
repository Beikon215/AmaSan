"""
ゲームの概要
あなたはあまさんです。
広大な海の中からうにを見つけてください。

操作方法
スタート/リセット：スペースキー
うにを捕獲：うにをクリック
"""
import tkinter as tk
from random import randint #2つライブラリを入れたよ

class AmaSan():
    def __init__(self):
        """
        アプリケーションを初期化する
        """
        self.win = tk.Tk() #Tkinterのウィンドウ表示
        self.win.title("Ama san") #ウィンドウの名前
        self.win.geometry("800x600") #ウィンドウサイズ
        self.win.resizable(width=False, height=False) #ウィンドウの大きさ変更できるか
        self.win.configure(bg="white") #ウィンドウの背景色
        self.labels = [[tk.Label(background="white",font=("MSゴシック", "15")) for i in range(23)] for j in range(24)] #ラベル作ったよ
        self.win.bind('<space>', self.reset) #ウィンドウに機能つけたよ
        self.startflag = False #開始フラグをオフにしたよ（開始フラグを作った）
        self.time_label = tk.Label(text="Time", background="white",font=("MSゴシック", "36")) #時間表示させるラベル作ったよ
        self.time_label.place(x = 10, y = 520) #現在時間表示させるラベルおいたよ
        self.seacret_canvas = tk.Canvas(self.win,width = 800 ,height = 518, bg = "white") #キャンバス作ったよ
        self.seacret_canvas.pack()
        self.nowtime = 0 #最初の時間0にしたよ
        self.hightime = 999999 #最初のハイスコア0にしたよ
        self.highscore_label = tk.Label(text="High Score", background="white",font=("MSゴシック", "36")) #ハイスコアを表示するラベルを作ったよ
        self.highscore_label.place(x = 500, y = 520) #ハイスコアを表示させるラベルおいたよ
        self.update() #アップデートメソッドを動かすよ

    def create_question(self):
        """
        問題を作る
        __init__()で作ったラベルにうに、うみのテキスト、機能（押したら反応）を入れる。
        """
        self.seacret_canvas.pack_forget()
        self.nowtime = 0
        rx = randint(0,21)
        ry = randint(0,23)
        for i in range(24):
            for j in range(22):
                if i == ry and j == rx:
                    self.labels[i][j]["text"] = "うに"
                    self.labels[ry][rx].bind('<Button-1>', self.mouse_canvas)
                else:
                    self.labels[i][j]["text"] = "うみ"
                    self.labels[i][j].bind('<Button-1>', self.penalty)
                self.labels[i][j].place(x = 10+j*35,y = 8+i*21)

    def mouse_canvas(self,event):
        """
        うにがクリックされたときのイベント
        ハイスコアと現在のスコアを比較し、数字が少なかった方をハイスコアにする。
        その後現在時刻を0にし、新しい問題を生成する。
        """
        self.hightime = min(self.nowtime, self.hightime)
        self.highscore_label["text"] = f"HS: {str(self.hightime//6000).zfill(2)}:{str(self.hightime%6000//100).zfill(2)}:{str(self.hightime%100)}"
        self.highscore_label.place(x = 500, y = 520)
        self.seacret_canvas.pack()
        self.nowtime = 0
        self.startflag = True

    def penalty(self,event):
        """
        うみがクリックされたときのイベント
        現在時刻に+500(+5秒)する。
        """
        self.nowtime += 500

    def reset(self,event):
        """
        スペースキーが押されたときのイベント
        スタートフラグを立て、新しいゲームを開始する。
        """
        self.seacret_canvas.pack()
        self.nowtime = 0
        self.startflag = True

    def update(self):
        """
        0.01秒ごとに時間を経過させ、スタートフラグが立っていることを確認する
        """
        self.nowtime += 1
        self.time_label["text"] = (f"Time: {str(self.nowtime//6000).zfill(2)}:{str(self.nowtime%6000//100).zfill(2)}:{str(self.nowtime%100).zfill(2)}")
        if self.startflag:
            if self.nowtime >= 20:
                self.create_question()
                self.startflag = False
        self.win.after(10, self.update)

app = AmaSan() #AmaSanClassからappインスタンスを作る
app.win.mainloop() #tkinterのメインループを作る