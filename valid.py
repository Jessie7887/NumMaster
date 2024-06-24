## checks if enteries are valid
# Check that all values are numbers
# Check that length of entry == len(nummy)

# are all numbers
def isNumber(x):
    if x.isdigit() == True:
        return True
    else:
        print(f'\nError, entry must contain numbers ONLY.')
        return False

# 4 digits| compare {x-user entry} to {y-comp entry}
def isLength(x, y):
    if len(x) == len(y):
        return True
    else:
        print(f'\nError, length of entry must match computer generated entry\'s length.')
        return False
