#Funktion för att tokenizea 

#Tokenize WIP
def tokenize(lines=[]):
    #Word list är listan på orden
    word_list = []
    for line in lines:
        start = 0
        while start < len(line):
            #Kollar ifall bokstaven är bokstav eller nummer
            if(line[start].isalnum()):
                end = start
                while end < len(line) and line[end].isalpha()==line[start].isalpha() and line[end].isdigit()==line[start].isdigit():
                    end+=1
                #Lägger till ordet i listan
                word_list.append(line[start:end].lower())
                start=end-1
            #Kollar ifall det är ett speciellt tecken
            elif(not line[start].isspace()):
                word_list.append(line[start])
            start += 1
    return word_list


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
    return res 


def printTopMost(counted_words={},printed_amount=0):
    sorted_list = sorted(counted_words.items(), key=lambda x: -x[1])
    for i in range(printed_amount):
        if(i==len(sorted_list)):
           break
        print(sorted_list[i][0].ljust(20)+str(sorted_list[i][1]).rjust(5))

asd = open("eng_stopwords.txt",encoding="utf-8")
stopwords=asd.read().split("\n")