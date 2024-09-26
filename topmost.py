import wordfreq
import sys
import urllib.request

def main():
    #Ifall det är en hemsida som ska checkas
    if(sys.argv[2].startswith("http")):
        response = urllib.request.urlopen(sys.argv[2])
        words = wordfreq.tokenize(response.read().decode("utf8").splitlines())
    #Ifall det är en text som ska checkas
    else:
        with open(sys.argv[2], encoding="utf-8") as inp_file:
            words = wordfreq.tokenize(inp_file)
    #Hämtar ut alla stopwords
    stopwords=open(sys.argv[1],encoding="utf-8").read().split("\n")
    #Printar de ord som är med mest i texten
    wordfreq.printTopMost(wordfreq.countWords(words,stopwords),int(sys.argv[3]))

if __name__ == "__main__":
    main()