# 読み込み用ファイル
R1_FILE = "/home/pi/julius/dict/new_word_chain.phone"
R2_FILE = "/home/pi/julius/dict/format.txt"
# 書き込み用ファイル
W_FILE = "/home/pi/julius/dict/word_chain.voca"

# 文末に追加
FORM = ["% NS_B","[s] silB","% NS_E","[/s] silE"]


with open(R1_FILE, mode = "r") as f:
    data1 = [v.rstrip() for v in f.readlines()]

with open(R2_FILE, mode = "r") as f:
    data2 = [v.rstrip() for v in f.readlines()]

with open(W_FILE, mode = "w") as f:
    for text1,text2 in zip(data1,data2):
        f.write("% "+text2.upper()+"\n")
        f.write(text1+"\n")
    for w in FORM:
        f.write(w+"\n")
