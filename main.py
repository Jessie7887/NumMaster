import numgenerator as ng
import gametime as gt

###
# Number Mastermind
# beginner -> 4 digits
# intermediate -> 5 digits
# expert -> 6 digits
###

# Notes:
# - may include validity checks: .isdigit, checklength
# have pegs ?? to tell user how close they are
# number of guesses should +1 the number of digits

def menu():
    ## b, i, e === 1, 2, 3
    while True:
        print(f'Please select the difficulty level you wish to try.')
        diff = str(input(">> "))
        if diff == str(1):
            gt.Bguessing()  # beginner
            break
        if diff == str(2):  
            gt.Iguessing()  # intermediate
            break
        if diff == str(3):
            gt.EXguessing() # expert
            break
        if diff == "X":
            print(f'Play again soon! >:/')
            exit(0)
        else:
            print("You must select a difficulty to begin playing.")
            quit = input("If you wish to exit, press X. or enter ok to select again.")
            if quit == "ok":
                continue
            if quit == "X":
                print(f'Play again soon! >:/')
                exit(0)
            else:
                print("terminating")
                exit(0)
    


# Main ~~~~~~~~~~~
if __name__ == '__main__':
    print(f'\nWelcome Message\nRules:(you will enter 4 digits @ a time).....\n\n')
    menu()
