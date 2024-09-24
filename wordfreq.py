#Funktion för att tokenizea 
def tokenize(lines=[]):
    word_list = []
    for line in lines:
        word = ""
        for letter in line:
            if(letter.isspace()):
                word+=letter
                print(letter)
            else:
                word_list.append(word)
                word = ""
            
        word_list.append(word)
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
        if not word in counted_words:
            counted_words[word]=0
        counted_words[word] +=1
    return counted_words



def remove_items(test_list, item): 
    res = [i for i in test_list if i != item] 
    return res 

def printTopMost(counted_words={},printed_amount=0):
    sorted_list = sorted(counted_words.items(), key=lambda x: -x[1])
    for i in range(printed_amount):
        if(i==len(sorted_list)):
           break
        print(sorted_list[i][0].ljust(20)+str(sorted_list[i][1]).rjust(5))



    
    
