import json
import random
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")


@app.route("/api/recommend_player")
def api_recommend_player():
    """ファイターズのHPから選手の名前を入手して、ランダムに1件返却します."""
    with urlopen("https://www.fighters.co.jp/team/player/list/") as res:
        html = res.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")

    numbers = soup.find_all("p", class_="pl_number")
    # print(numbers)
    numbers = [t.string for t in numbers]
    # print(numbers)


    playername=[]
    players = soup.find_all("p", class_="pl_name")

    count=0
    for n in players:
        #print(n)
        #p = n.get_text()
        p = n.text
        
        playername.append(p)
        count=count+1

    #print(playername)


    kanji=[]
    myouji=[]
    namae=[]
    count = 0
    for a in playername:
        index1 = a.find("\n")
        #print(index1)
        kanji.append(a[0:index1])
        #print(kanji[count])

        index2 = a.find("\u3000")
        if index2 == -1:
            index2 = a.find("・")

        if index1 > index2:
            #print("2回目!")
            index2 = a.find("・", index1+1)
        #print(index2)
            
        index3 = len(a)
        #print(index3)
        myouji.append(a[index1+1:index2])
        #print(myouji[count])
        namae.append(a[index2+1:index3])
        #print(namae[count])
        count = count +1

    count = 0
    for count in range(97):
        print(numbers[count], kanji[count], myouji[count], namae[count])


    index_c = random.randint(0,96)

    """
        **** ここを実装します（基礎課題） ****

        1. はてブのホットエントリーページのHTMLを取得する
        2. BeautifulSoupでHTMLを読み込む
        3. 記事一覧を取得する
        4. ランダムに1件取得する
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """





    # ダミー
    return json.dumps({
        "number" : numbers[index_c],
        "name" : kanji[index_c]
    })

@app.route("/api/xxxx")
def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)
