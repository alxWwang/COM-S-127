# Nicholas Alexander             13 September 2022
# Assignment 2

print("Welcome to the Magic 9 Ball...")
print()

# TODO: Have student print their name/ section when the script runs
print("By: Nicholas Alexander Wang")
print("[COM S 127 A]")
print()

print("What would you like to do?")
print()
choice = input("[c]alculator, [p]rediction, [q]uit: ")
print()

if choice == "c" or choice == "p" or choice == "q" :
    if choice == "c":
        def numberTest(x) :
            try :
                float(x)
                return True
            except ValueError:
                return False

        calc = input('[+], [-], [*], [/], [%], [**]\n')
        res = 0
        
        if calc == "+" or calc == "-" or calc == "*" == calc == "/" or calc == "**" or calc =="%" :
            
            
            for i in range(5) :
                numbers = input("Please enter a number ")
                (numberTest(numbers))
                if numberTest(numbers) == False :
                    print("This is not a number", end = "\n")
                else :
                    break
            numbers = float(numbers)

            for i in range(5) :
                numbers2 = input("Please enter another number ")
                numberTest(numbers2)
                if numberTest(numbers) == False :
                    print("This is not a number", end ="\n")
                else :
                    break
            numbers2 = float(numbers2)
            
            
            if calc == "+" :
                res = (numbers + numbers2)
            elif calc == "-" :
                res = (numbers - numbers2)
            elif calc == "*" :
                res= (numbers * numbers2)
            elif calc == "/" :
                res = (numbers//numbers2)
            elif calc == "**" :
                if numbers2 == 0 :
                    print("please dont enter 0")
                    quit()
                res = (numbers**numbers2)
            elif calc == "%" :
                if numbers2 == 0 :
                    print("please dont enter 0")
                    quit()
                res = (numbers % numbers2)       
        else :
            print("that is not a valid answer")   
            quit()     
                
        print(numbers, calc, numbers2, "=",res)
                         
    elif choice == "p" :
        pred = input("What are you thinking? ")

        predVa = int(len(pred))
        predVa %= 10

        predS = [
            "this will be great!",
            "this will not be bad.",
            "this is maybe not the best idea.",
            "this is probably good for you.",
            "this is probably bad for you.",
            "this is for the better.",
            "this is the worst thing that could happen.",
            "this is the best thing that could happen.",
            "this is your luck!",
            "this is just bad luck.",
        ]

        predX = predS[predVa]

        print("As far as '", pred, "' is concerned, I think ", predX)
        
    else : #quit : 
        print("So you want to quit... ok") 
        quit()       
else :
    print("ERROR: This is not an option")
    quit()


    
    
# initial choice tasks ------------------------------------------------------------------------------------------------------------------------
# TODO: use conditional logic to determine which function of the Magic 9 Ball to use: [c]alculator, [p]rediction, [q]uit
# - create a section of code that executes if the user enters 'c' as their initial choice
# - create a section of code that executes if the user enters 'p' as their initial choice
# - create a section of code that executes if the user enters 'q' as their initial choice
# TODO: add another section of code where if the user does not enter "c", "p", or "q" in their initial choice, the script will print out an error message stating: 
# "ERROR: I did not understand your input... Please try again..." or something similar (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'c' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'c' section, take in input from the user for one of six calculations: [+], [-], [*], [/], [%], [**]
# TODO: if the user does not enter "+", "-", "*", "/", "%", or "**" in their calculation choice, print out an error message stating: 
# "ERROR: You must enter either \"+\", \"-\", \"*\", \"/\", \"%\", or \"**\"" or something similar (use your imagination)
# TODO: depending on the input from the step above, use conditional logic to determine which calculation to perform
# TODO: program code sections for each calculation type which takes in input for the left hand side and right hand side
# of the operator, perform the calculation, then print the result
# TODO: for / and % use conditional logic to check if the right hand side of the expression is zero (0) and print an error if it is
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'p' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'p' section, take in input from the user asking them "What is your question?: " or something similar (use your imagination)
# TODO: print a string stating print("As far as '", question, "' is concerned, I predict: ") or something similar (use your imagination)
# TODO: use then length of the question string the user input to generate a 'prediction selection value' within the following range: 
# from 0 through (<the number of predictions>-1)
# HINT: there is a built in function to find the range of a string
# HINT: one of the operators used in the 'c' section of the script will return a value within the range 'from 0 through (<the number of predictions>-1)'
# when applied to <the length of the question string> on the left side of the operator, and <the number of predictions> on the right side
# TODO: write at least ten (10) 'predictions' and use conditional logic to select which one to print after the 'prediction selection value'
# from above is calculated (use your imagination)
# TODO: if the computation to produce a 'prediction selection value' creates a value outside the range 'from 0 through (<the number of predictions>-1)'
# then have the script print an error message to that effect. NOTE: If the calculation of a 'prediction selection value' is done properly, this 
# error message should **never** be seen.
# HINT: if you write ten (10) 'predictions,' then <the number of predictions> will be 10. This means that the range of the 'prediction 
# selection value' will be between 0 and 9. After selecting a value between 0 and 9 by way of the length of the 'question' string, one of
# the operators from the 'c' option, and <the number of predictions>, you will print out a 'prediction' corresponding to this value.
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'q' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'q' option, print out a message stating "Maybe next time...", or "Goodbye!", or something else to that effect 
# (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------
