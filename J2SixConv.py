import re
from janome.tokenizer import Tokenizer
from pykakasi import kakasi
import jaconv

#J2SixConv.py
#ゲーム グランブルーファンタジーに登場する言語
#六竜語と日本語を一対一で変換するプログラム
#日本語を入力することで対応した六竜語が返答される


#各インスタンスの生成
kks: kakasi = kakasi()
tk: Tokenizer = Tokenizer()

count: int = 0
while 1:
    string = input("日本語を入力してください:")
    #形態素ごとに分割
    for token in tk.tokenize(string):
        
        #ひらがなを抽出
        hira = token.surface
        #ひらがなをローマ字に変換
        token = kks.convert(hira)
        token = token[0]["kunrei"]
        token.split()
        #変換したローマ字を逆順に
        token = token[::-1]

        #子音が連続した部分に母音'u'を挿入
        if re.search("[aiueo-]+$", token) and len(token) != 0 and token[0] != "　":
            token = token
        else:
            token = token + "u"
        count = 0
        for i in range(len(token)):
            if (
                token[i] == "a"
                or token[i] == "i"
                or token[i] == "u"
                or token[i] == "e"
                or token[i] == "o"
                or token[i] == " "
                or token[i] == "-"
            ):
                count = 0
            else:
                count = count + 1
            if count == 2:
                count = 0
                token = token[:i] + "u" + token[i:]
        
        #ローマ字をカタカナに変換
        token = jaconv.alphabet2kata(token)
        char = ["ア", "イ", "ウ", "エ", "オ"]
        charl = ["ァ", "ィ", "ゥ", "ェ", "ォ"]

        #先頭の母音を小文字に変換する
        for i in range(0, 5):
            if token[0] == char[i]:
                token = charl[i] + token[1:]
        print(hira + " : " + token)
