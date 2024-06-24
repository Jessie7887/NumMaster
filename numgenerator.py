import random
# get a random string of numbers for each difficulty
# leave it its own fiie in case you make difficulty changes



# b gen ~~ beginner level; gives 4 digits 
def bgen():
    num = random.randrange(1000, 9999)
    return num


# i gen ~~ intermediate level; gives 5 digits 
def igen():
    num = random.randrange(10000, 99999)
    return num


# ex gen ~~ expert level; gives 6 digits 
def exgen():
    num = random.randrange(100000, 999999)
    return num


# custom gen ???; gives ??? digits
