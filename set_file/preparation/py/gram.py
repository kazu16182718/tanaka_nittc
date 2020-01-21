'''
元となるテキストデータファイルをJulius用のファイルに変換
'''

# 読み込み用ファイル
R_FILE = "/home/pi/tanaka/julius/dict/format.txt"
# 書き込み用ファイル
W_FILE = "/home/pi/tanaka/julius/dict/word_chain.grammar"

with open(R_FILE, mode = "r") as f:
    data = [v.rstrip() for v in f.readlines()]

with open(W_FILE, mode = "w") as f:
    f.write("S : NS_B WORD_CHAIN NS_E\n")
    for text in data:
        f.write("WORD_CHAIN:"+text.upper()+"\n")
