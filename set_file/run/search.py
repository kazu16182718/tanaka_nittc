PATH = "dictionary2.txt"
with open(PATH) as f:
    l = [text.strip() for text in f.readlines()]
    print(l)
