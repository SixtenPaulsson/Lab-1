import wordfreq
import sys
import urllib.request

#python3 topmost.py eng_stopwords.txt examples/article1.txt 20
#python3 topmost.py eng_stopwords.txt https://www.gutenberg.org/files/15/15-0.txt 20
if(sys.argv[2].startswith("http") or sys.argv[2].startswith("https")):
    response = urllib.request.urlopen(sys.argv[2])
    lines = response.read().decode("utf8").splitlines()
    words = wordfreq.tokenize(lines)
else:
    with open(sys.argv[2], encoding="utf-8") as inp_file:
        words = wordfreq.tokenize(inp_file)

stopwords=open(sys.argv[1],encoding="utf-8").read().split("\n")
counted_words = wordfreq.countWords(words,stopwords)
wordfreq.printTopMost(counted_words,int(sys.argv[3]))