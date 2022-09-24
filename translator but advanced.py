def setup(): #creates the arrays for usage.
    for x in range(100000): languages[0].append("") # used for English
    for x in range(100000): languages[1].append("") # used for French
    for x in range(100000): languages[2].append("") # used for Spanish
    for x in range(100000): languages[3].append("") # used for Japanese
    
def WordToOrd(word): # turns a word into its ord counterpart.
    val = 0
    for x in range(0,len(word)): val += ord(word[x])
    return val
 
def PosMoving(pos): # basically keep moving 1 space to the right until either you find an empty pos, or you hit the end of the array, at which point you go back to pos 0.
    fin = False
    spos = pos - 1
    while fin == False and spos != pos:
        if languages[0][pos] != "":
            pos += 1
            if pos >= len(languages[0]): pos = 0 # if it reaches the end of the array
        else: fin = True
    if spos == pos:
        pos = 696969
        print("there is no space in the dictionary.")
    return pos

def addword(choice): # adds a word for whichever language the user specifies
    if choice == 0:
        word = input("input english word \n")
        pos = (WordToOrd(word)) % 100000 
        pos = PosMoving(pos)
        if pos != 696969:
            languages[choice][pos] = word # choice is which array, pos is the position in said array.
            languages[1][pos] = input("input the French translation \n") # adds the translations in the same position, but in the respective row of the language.
            languages[2][pos] = input("input the Spanish translation \n")
            languages[3][pos] = input("input the Japanese translation \n")
            print(word, "and its respective translations have been added.")
    if choice == 1:
        word = input("input French word \n")
        pos = (WordToOrd(word)) % 100000
        pos = PosMoving(pos)
        if pos != 696969:
            languages[choice][pos] = word
            languages[0][pos] = input("input the English translation \n") # adds the translations in the same position, but in the respective row of the language.
            languages[2][pos] = input("input the Spanish translation \n")
            languages[3][pos] = input("input the Japanese translation \n")
            print(word, "and its respective translations have been added.")
    if choice == 2:
        word = input("input Spanish word \n")
        pos = (WordToOrd(word)) % 100000
        pos = PosMoving(pos)
        if pos != 696969:
            languages[choice][pos] = word
            languages[0][pos] = input("input the English translation \n")
            languages[1][pos] = input("input the French translation \n") # adds the translations in the same position, but in the respective row of the language.
            languages[3][pos] = input("input the Japanese translation \n")
            print(word, "and its respective translations have been added.")
    if choice == 3:
        word = input("input Japanese word \n")
        pos = (WordToOrd(word)) % 100000
        pos = PosMoving(pos)
        if pos != 696969:
            languages[choice][pos] = word
            languages[0][pos] = input("input the English translation \n") # adds the translations in the same position, but in the respective row of the language.
            languages[1][pos] = input("input the French translation \n")
            languages[2][pos] = input("input the Spanish translation \n")
            print(word, "and its respective translations have been added.")

def FindWord(word): # finds where a certain word is stored in a certain position
    if word == languages[0][(WordToOrd(word)) % 100000]:
        found = True
        print("First found in the English Dictionary")
    elif word == languages[1][(WordToOrd(word)) % 100000]:
        found = True
        print("First found in the French Dictionary")
    elif word == languages[2][WordToOrd(word) % 100000]:
        found = True
        print("First found in the Spanish Dictionary")
    elif word == languages[3][(WordToOrd(word))%100000]:
        found = True
        print("First found in the Japanese Dictionary")
    else:
        found = False
        pos = (WordToOrd(word)) % 100000
        spos = pos - 1
        while found != True and pos != spos:
            pos += 1
            if pos >= len(languages[0]): pos = 0
            if languages[0][pos] == word: found = True
            if languages[1][pos] == word: found = True
            if languages[2][pos] == word: found = True
            if languages[3][pos] == word: found = True
    if found == True:
        return pos
    else: 
        print("this word is not in the dictionary.")
        pos = 696969
        return pos


"""   
def storeword(pos): # stores the word the user inputted into the text file. No movement in terms of the text file is needed due to it all being fixed via the callibratetxt() function.
    tf = []
    for x in range(4): tf.append("")
    tf[0] = open("eng.txt", "w")
    tf[1] = open("french.txt", "w")
    tf[2] = open("spanish.txt", "w")
    tf[3] = open("jp.txt", "w")
    for x in range(4):
        tf[x].write(languages[x][pos])
        print(languages[x][pos], "has been saved into their respective file. ")
    print("all words have been successfully saved.")
"""
 
def callibratetxt(): # adds the words from the text file to the temporary array, which are then put into the pos position via the MovingPos function.
    tf = []
    for x in range(4): tf.append("")
    tf[0] = open("eng.txt", "r")
    tf[1] = open("french.txt", "r")
    tf[2] = open("spanish.txt", "r")
    tf[3] = open("jp.txt", "r")
    temporarray = [[],[],[],[]]
    count = 0
    data = "temp"
    while data != "": # takes the words out of each respective text file, then puts them in the temporarray (funny pun!)
        for x in range(4):
            data = tf[x].readline()
            data = data.rstrip()
            temporarray[x].append(data)
        for x in range(4): print(temporarray[x][count], "has been imported successfully.")
        count += 1
    for x in range(4): tf[x].close()
    for x in range(len(temporarray[0])):
        word = temporarray[0][x]
        pos = WordToOrd(word) % 100000
        for y in range(4): languages[y][pos] = word
            
def outword(word): # simply just finds the word in the dictionary, and outputs in whatever language you want it to.
    TranslateTo = int(input("What language to translate to (0 for English, 1 for French, 2 for Spanish, 3 for Japanese)?\n"))
    while TranslateTo < 0 or TranslateTo > 3:
        TranslateTo = int(input("Invalid language to translate to. Please select a language (0 for English, 1 for French, 2 for Spanish, 3 for Japanese \n"))
    pos = FindWord(word)
    if pos != 696969:
        if TranslateTo == 0: print(languages[0][pos])
        if TranslateTo == 1: print(languages[1][pos])
        if TranslateTo == 2: print(languages[2][pos])
        if TranslateTo == 3: print(languages[3][pos])
def rewrite():
    tf = []
    for x in range(4): tf.append("")
    tf[0] = open("eng.txt", "w")
    tf[1] = open("french.txt", "w")
    tf[2] = open("spanish.txt", "w")
    tf[3] = open("jp.txt", "w")
    for x in range(4): tf[x].truncate() # wipes the files
    for x in range(len(languages[x])): # for the 100000 times since that's how long each row is
        for y in range(4): # for each language (there are 4 of them)
            if languages[y][x] != "": tf[y].write(languages[x][y]) # if it isn't blank, it writes it in its respective language's text file.
            
temporarray = [[],[],[],[]]    
tf = []
languages = [[],[],[],[]]
finished = False
operation = ""
setup()
cont = 1
if int(input("import dictionary from computer files? y[1], n[2] \n")) == 1: callibratetxt()

while finished == False:
    operation = input("Input a word [i], output a word[o], replace a word in the dictionary[r], remove a word from the dictionary [x], or quit [q]? \n")
    if operation == "i" or operation == "I": # if the user wants to input a word
        while cont == 1:
            choice = int(input("put in English [0], French [1], Spanish [2] or Japanese [3]? \n"))
            while choice > 3 or choice < 0:
                choice = int(input("please input a valid number. English [0], French [1], Spanish [2] or Japanese [3]. \n"))
            addword(choice)
            cont = int(input("add another word? 1 for yes, 2 for no. \n"))
            while cont != 1 and cont != 2: cont = int(input("Invalid option. Add another word? 1 for yes, 2 for no."))
    if operation == "o" or operation == "O":# if the user wants to find the translation of a word and output it.
        while cont == 1:
            word = input("input word to find in the dictionary \n")
            outword(word)  
            cont = int(input("add another word? 1 for yes, 2 for no. \n"))
            while cont != 1 and cont != 2: cont = int(input("Invalid option. Add another word? 1 for yes, 2 for no."))
    if operation == "r" or operation == "R":
        print("invalid at the moment, try again in the next update!")
    if operation == "q" or operation == "Q":
        finished = True
    if operation == "x" or operation == "X":
        print("invalid at the moment, try again in the next update!")

if int(input("overwrite the file with the new words? Y[1], or N[2]")) == 2: rewrite()
            
        
