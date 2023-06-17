

def main():
    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": # (**"p" Section Tasks**)
            print("Welcome to Dungeon Crawl")
                       
            
        elif choice == "i": 
            pass
        
        
        elif choice == "q": 
            print("Goodbye then")
            gameOver = True
            
            
            pass
        
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()