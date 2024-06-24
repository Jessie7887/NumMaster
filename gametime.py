import numgenerator as num_gen
import main

## give less tries as difficulty gets harder ##

def Bguessing():    # nummy vs noob | comp vs human
    nummy = num_gen.bgen()
    print(nummy) ## for tracing!!
    noob = input(f'Guess the 4 digit number\n>> ')
    # if you get it right on the 1st try... :P
    if int(nummy) == int(noob):
        print("No way! :O Incredible!")
        play_again()
    else:
        while noob != nummy:
            ctr = 8     # easy mode -> 8 guesses
            ctr -= 1

            counter = 0    # correct numbers in seq  

            # read as a 4 character string to easily isolate each index
            noob = str(noob)    # string
            nummy = str(nummy)    # string

            # stores correct digits in a list
            good_digits = ["X"] * 4
            print(good_digits)  ## for tracing !!
            # guessing time ~~ make your attempts (you have 8)
            for i in range(0, 4):
                # if one of the guessed digits == to generated string
                if noob[i] == nummy[i]:
                    counter += 1    # number of correctly guessed digits
                    good_digits[i] == noob[i]
                # else:
                #     continue

            # if not all the numbers are right & you still have guesses
            if (counter < 8) and (counter != 0):
                print(f'the value you entered was incorrect. However, you did manage to get {counter} digits(s) correct.\n')
                # show them which numbers in their sequnce were correct/incorrect
                for j in good_digits:
                    print(j, end='')
                print("\n\n")
                noob = input(f'Guess another 4 digit number\n>> ')

            # if you couldn't guess any of digits correctly
            elif counter == 0:
                print(f'You were not able to find ANY of the numbers in the sequence :(.')
                noob = input(f'Try & guess a new 4 digit number\n>> ')

            elif (counter == 0) and (ctr == 0):
                print(f'You\'re out of guesses :( Sorry.')
                print(f'The sequence was: {nummy} .')
                play_again()

        if noob == nummy:
            print("Congrats Number Mastermind :)")
            print(f'You found the correct number with {ctr} tries left.')
            play_again()


def Iguessing():
    # noob = int(input(f'Guess the 5 digit number\n>> '))
    pass

def EXguessing():
    # noob = int(input(f'Guess the 6 digit number\n>> '))
    pass



# Play Again Option :)
def play_again():
    print(f'Want to take on a new challenge >:)?')
    print("(enter yes or no)")
    go = input(">> ")
    if go == "yes":
        main.menu()
    if go == "no":
        print(f'Alright. Thanks for playing!! :D')
        exit(0)