import re
from janome.tokenizer import Tokenizer
from pykakasi import kakasi
import jaconv

#J2SixConv.py
#ゲーム グランブルーファンタジーに登場する言語
#六竜語と日本語を一対一で変換するプログラム
#日本語を入力することで対応した六竜語が返答される

def check_vowel(c):
    check_arr = {"a","i","u","e","o"," ","-"}
    for check_char in check_arr:
        if c == check_char:
            return True
    return False


#各インスタンスの生成
kks: kakasi = kakasi()
tk: Tokenizer = Tokenizer()

count: int = 0
while 1:
    raw_input: str = input("日本語を入力してください:")
    raw_input.replace("ー","")
    #形態素ごとに分割
    for token in tk.tokenize(raw_input):
        
        #ひらがなを抽出
        hira = token.surface
        #ひらがなをローマ字に変換
        rome = kks.convert(hira)
        rome_kunrei = rome[0]["kunrei"]
        rome_kunrei.split()
        #変換したローマ字を逆順に
        conv_rome_kunrei = rome_kunrei[::-1]

        #子音が連続した部分に母音'u'を挿入
        if re.search("[aiueo-]+$", conv_rome_kunrei) and len(conv_rome_kunrei) != 0 and conv_rome_kunrei[0] != "　":
            pass
        else:
            conv_rome_kunrei += "u"
        count: [int] = 0
        for i in range(len(conv_rome_kunrei)):
            if check_vowel(conv_rome_kunrei[i]):
                count = 0
            else:
                count = count + 1
            if count == 2:
                count = 0
                conv_rome_kunrei: [str] = conv_rome_kunrei[:i] + "u" + conv_rome_kunrei[i:]
        
        #ローマ字をカタカナに変換
        rome_kata: list[str] = jaconv.alphabet2kata(conv_rome_kunrei)
        vowelUpper: list[str] = ["ア", "イ", "ウ", "エ", "オ"]
        vowelLower: list[str] = ["ァ", "ィ", "ゥ", "ェ", "ォ"]

        #先頭の母音を小文字に変換する
        for i in range(0, 5):
            if rome_kata[0] == vowelUpper[i]:
                rome_kata = vowelLower[i] + rome_kata[1:]
        print(hira + " : " + rome_kata)
