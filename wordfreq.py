#Funktion för att tokenizea 

#Tokenize WIP
def tokenize(lines=[]):
    word_list = []
    for line in lines:
        start = 0
        while start < len(line):
            #print(line[start])
            if(line[start].isalpha() or line[start].isdigit()):
                #print(line[start])
                end = start
                while end < len(line) and line[end].isalpha()==line[start].isalpha() and line[end].isdigit()==line[start].isdigit():
                    end+=1
                #print(line[start:end])
                word_list.append(line[start:end].lower())
                start=end-1
            elif(not line[start].isspace()):
                word_list.append(line[start])
            start = start+1
            

    return word_list
    

def process_word(word=""):
    segments = []
    segment = ""
asd = open("eng_stopwords.txt",encoding="utf-8")
stopwords=asd.read().split("\n")
#print(stopwords)

def countWords(word_list=[],stop_words=[]):
    for stop_word in stop_words:
        word_list=remove_items(word_list,stop_word)
    counted_words={}
    for word in word_list:
        if counted_words.get(word) == None:
            counted_words[word]=0
        counted_words[word] +=1
    return counted_words



def remove_items(test_list, stopword): 
    res = [i for i in test_list if i != stopword] 
    #if(test_list.conti)
    return res 




def printTopMost(counted_words={},printed_amount=0):
    sorted_list = sorted(counted_words.items(), key=lambda x: -x[1])
    for i in range(printed_amount):
        if(i==len(sorted_list)):
           break
        print(sorted_list[i][0].ljust(20)+str(sorted_list[i][1]).rjust(5))
#print(tokenize(["the 10 little chicks"]))