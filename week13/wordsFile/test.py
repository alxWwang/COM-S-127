def write():
    currentFile = open("test.txt","w")

    currentFile.write("kontol lu")
    currentFile.close()


def read():
    readFile = open("test.txt","r")
    text = readFile.read()
    readFile.close()

    print(text)
    
def append():
    appendFile = open("test.txt", "a")
    appendFile.write("\n")
    appendFile.write("This is the next line")
    appendFile.close
    
write()