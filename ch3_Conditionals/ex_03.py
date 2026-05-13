#Grade  Score 
inp = input("Enter your grade: \n")
try:
    grade = float(inp)

    #Conditionals F < 0.6     
    if 0.0 <= grade <= 1.0:
        if grade >= 0.9:
            print("Your grade is an A")
        elif grade >= 0.8:
            print("Your grade is an B")
        elif grade >= 0.7:
            print("Your grade is an C")
        elif grade >= 0.6:
            print("Your grade is an D")
        elif grade < 0.6:
            print("Your grade is an F")
    else:
        print("Your score is not valid. Must be between:[0.0 - 1.0]")
except:
    print("Enter a valid number")
