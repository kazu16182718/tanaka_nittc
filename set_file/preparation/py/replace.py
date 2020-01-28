import sys

args = sys.argv

#file_name = input("input file name:")
file_name=args[1]
text=""

with open(file_name, encoding="utf-8") as f:
    for line in f:
        #改行削除
        line=line.strip()
        #｢,｣で分割
        line=line.split("，")
        for l in line:
            l = l  + " " + l + "\n" 
            text += l

with open("/home/pi/julius/dict/word_chain.yomi", mode="w", encoding="utf-8") as f:
    f.write(text)


