def tokenize(lines=[]):
    #Lista på alla ord
    word_list = []
    for line in lines:
        start = 0
        while start < len(line):

            #Kollar ifall bokstaven är bokstav eller nummer
            if(line[start].isalnum()):

                end = start + 1
                #Gör så att end blir indexet på när ordet slutar
                #Efteråt kommer line[start:end] bli ett ord
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
    word_list = list(filter(lambda x: x not in stop_words, word_list))
    counted_words={}
    for word in word_list:
        if counted_words.get(word) == None:
            counted_words[word]=0
        counted_words[word] +=1
    return counted_words

def printTopMost(counted_words={},printed_amount=10):
    #Sorterar dicten
    sorted_list = sorted(counted_words.items(), key=lambda x: -x[1])
    for i in range(printed_amount):
        if(i==len(sorted_list)):
           break
        print(sorted_list[i][0].ljust(20)+str(sorted_list[i][1]).rjust(5))