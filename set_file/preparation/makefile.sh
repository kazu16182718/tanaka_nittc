### ファイルのパスは絶対パスで指定！ ### 
DICT_NAME = "/home/pi/julius/dict/dic.txt"

cd /home/pi/julius
ls
mkdir dict
cd dict
python3 /home/pi/tanaka/set_file/preparation/py/replace.py /home/pi/julius/dict/dic.txt 
iconv -f utf8 -t eucjp ~/julius/dict/word_chain.yomi | ~/julius/julius-4.4.2.1/gramtools/yomi2voca/yomi2voca.pl | iconv -f eucjp -t utf8 > ~/julius/dict/word_chain.phone

# 空白を半角スペースに変換する処理
cat /home/pi/julius/dict/word_chain.phone | tr '\t' ' ' > /home/pi/julius/dict/new_word_chain.phone
# 読み込み用単語のみに整形
cat /home/pi/julius/dict/new_word_chain.phone | tr -dc '[a-zA-Z"\n"]' > /home/pi/julius/dict/format.txt
# .grammerファイルを作成
python3 /home/pi/tanaka/set_file/preparation/py/gram.py
python3 /home/pi/tanaka/set_file/preparation/py/voca.py
# 独自辞書データに変換
cd /home/pi/julius/julius-4.4.2.1/gramtools/mkdfa
mkdfa.pl /home/pi/julius/dict/word_chain


