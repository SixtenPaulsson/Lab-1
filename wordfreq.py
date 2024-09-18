#Funktion för att tokenizea 
def tokenize(sentences=[]):
    term_list = []
    #Checkar ifall 
    for sentence in sentences:
        #Går igenom varenda mening
        words=sentence.split()
        print(sentence)
        for word in words:
            #print(word)
            term_list.append(word)
    print(term_list)
    return term_list