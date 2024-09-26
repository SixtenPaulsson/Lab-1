import wordfreq
import sys
with open(sys.argv[1], encoding="utf-8") as inp_file:
    for line in inp_file:
        # do something with the current line
        print(wordfreq.tokenize(line))



#asd = open("eng_stopwords.txt",encoding="utf-8")
#stopwords=asd.read().split("\n")