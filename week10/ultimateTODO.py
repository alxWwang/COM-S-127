# <Nicholas Alexander Wang>             <Date it was started>
# <Assignment 5>

import sys
import pickle

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList,loc):
    itemFound = False
    keyName = ""
    index = -1
    # TODO: Iterate through all the keys in the dictionary and check each list of each key to  
    # see if an item is present. If it is, set itemFound to be 'True.' Then, set the keyName variable  
    # to the key where the item was found, and the index in the list where the item was found. 
    # If the item is not found in any of the lists in the dictionary, keep the default values above. 
    # Return the itemFound boolean, the keyName string, and the index integer (1 pt.)
    if item in todoList[loc] :
        itemFound = True
        keyName=item
        index = todoList[loc].index(item)
        index = int(index)
    
    
    return itemFound, keyName, index

def addItem(item, toList, todoList,loc):
    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is not in the dictionary of lists, add it to the list specified by the 'toList'
    # variable. If the item is already in the dictionary of lists, print an error message specifying:
    # - the name of the item
    # - the keyName of the list where the item is found
    # - the index of the item in the list
    # Return the todoList data structure after it has been modified (or not) (1 pt.)
    
    itemFound,keyName,index = checkItem(item,todoList,loc)
    
    if itemFound== True:
        print(keyName,"is found on the list")
        indexView = index + 1
        print("index number :", indexView)
        
    
    if itemFound == False:
        toList.append(item)
        
    return todoList

def deleteItem(item, todoList,loc):
    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is already in the dictionary of lists, delete that item. If the item is not
    # in the dictionary of lists, print an error message specifying:
    # - the name of the item
    # Return the itemFound boolean and the todoList data structure after it has been modified (or not) (1 pt.)
    itemFound,keyName,index = checkItem(item,todoList,loc)
    
    if itemFound== True:
        print(keyName,"is found on the list")
        indexView = index + 1
        print("index number :", indexView)
        
        todoList[loc].pop(index)
    
    if itemFound == False:
        print("There is no such item in the list")
   
    return itemFound, todoList

def moveItem(item, dariMana, keMana,todoList):
    # TODO: Use the deleteItem function to search for/ delete the specified item. Use the itemFound boolean
    # it returns to determine if the item was found. If it was, use the addItem function to add the item to  
    # the specified toList key.
    # Return the todoList data structure after it has been modified (or not) (1 pt.)
    deleteItem(item,todoList,dariMana)
    addItem(item,todoList[keMana],todoList,keMana)
    return todoList
    
def printTODOList(todoList):
    # TODO: Iterate through all the keys in the dictionary and print both the key and the list the dictionary
    # holds for that key on a single line on the screen.
    # ex: todo: ['laundry', 'dishes']
    # Return None (1 pt.)
    for x in todoList:
        print(x,": ", end='')
        
        for i in todoList[x]:
            print(i, " ",end = '')
        print()

    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            # TODO: Prompt the user to enter an item, and take in that input as a string. Call the addItem function
            # to add the item to the 'backlog' key's corresponding list. Finally, use the printTODOList function
            # to print the todoList data structure. (1 pt.) 
            initList()
            
            inputBacklog = input("Enter a string input :")
            
            addItem(inputBacklog,todoList["backlog"],todoList,"backlog")
            
            print()
            printTODOList(todoList)
            
            
            pass
        elif choice == "m":
            # TODO: Check to see if any of the lists in the data structure have items in them. If all of the lists in
            # the dictionary are empty, print an error message that states 'No items to move!' or something similar.
            # If at least one of the lists in the dictionary has an item in it, do the following:
            # - Prompt the user to enter an item, and take in that input as a string.
            # - Use the checkItem function to confirm if that item is in the data structure.
            # - While the item is not in the data structure, print an error message stating the item does not exist
            #   and then prompt the user to enter a different item. Use the checkItem function again to confirm if 
            #   the new item is inside the data structure.
            # - Prompt the user to enter a dictionary key for the list to move the item to, and take in that input 
            #   as a string.
            # - While the dictionary key the user specifies is not a key that is in the dictionary, print an error
            #   message stating that the key does not exist. Then, prompt the user to enter a new dictionary key.
            # - call the moveItem function, passing the item, dictionary key, and todoList as arguments.
            # Finally, whether or not the data structure is totally empty or not, call the printTODOList function
            # and print out the data structure. (1 pt.)
            
            initList()
            
            if todoList["backlog"] == [] and todoList["todo"] ==[] and todoList["in_progress"] ==[] and todoList["in_review"] == [] and todoList["done"] == []:
                print("No items to move!")
                
            else :
                while True:
                    itemMoveLoc1 = input("Where is the item that you want to move? ")
                    print()
                    if itemMoveLoc1 in todoList:
                        break  
                print("------------------------------------------")
                while True:
                    itemMove = input("What is the item that you want to move? ")
                    print()
                    if itemMove in todoList[itemMoveLoc1]:
                        break  
                print("------------------------------------------")
                while True:
                    itemMoveLoc2 = input("Where do you want to move the item? ")
                    print()
                    if itemMoveLoc2 in todoList:
                        break
                
                print()
                moveItem(itemMove,itemMoveLoc1,itemMoveLoc2,todoList)
                printTODOList(todoList)
            
            
            
            
            
            pass
        elif choice == "d":
            # TODO: Prompt the user to enter an item, and take in that input as a string. Call the deleteItem function
            # to remove the item from the data structure if it is present. Finally, use the printTODOList function
            # to print the todoList data structure. (1 pt.)
            # HINT: the deleteItem function returns two (2) values - do you need to do things with both of them?
            
            initList()
            
            inputDelete = input("Enter a String input :")
            
            deleteItem(inputDelete,todoList,"backlog")
            
            printTODOList(todoList)
            
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    taskOver = False

    print("The Ultimate TODO List")
    print()
    
    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Nicholas Alexander Wang")
    print("[COM S 127 1]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()