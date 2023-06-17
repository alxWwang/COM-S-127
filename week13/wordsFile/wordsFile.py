def write(word, where):
    currentFile = open(where,"a")
    
    currentFile.write("\n")    
    currentFile.write(word)
    currentFile.close()

def overwrite(word, where):
    currentFile = open(where,"w")
    
    currentFile.write("\n")    
    currentFile.write(word)
    currentFile.close()
    
def sort1(list1):
    list1sorted = sorted(list1)
    return list1sorted
    
def main():
    wordList = []
    wordListSorted = ''
    while True:
        word = input("Enter a String ")
        if word == "*":
            break
        wordList.append(word)
        
    for i in wordList:
        write(i,"wordsFile.txt")
        
    wordListSorted = sort1(wordList)
    overwrite("", "wordsFile.txt")
    
    for i in wordListSorted:    
        write(i,"wordsFile.txt")
    
main()
