#score  Score 
def computescore(score):
    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            print("Your grade is an A")
        elif score >= 0.8:
            print("Your grade is an B")
        elif score >= 0.7:
            print("Your grade is an C")
        elif score >= 0.6:
            print("Your grade is an D")
        elif score < 0.6:
            print("Your grade is an F")
    else:
        print("Your score is not valid. Must be between:[0.0 - 1.0]")

inp = input("Enter your grade: \n")

try:
    score = float(inp)
    computescore(score)
except:
    print("Enter a valid number")
    quit()