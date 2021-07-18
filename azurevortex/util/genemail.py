import random

def getrandemailaddr():
    list = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com']
    return f'someuser{random.randint(100, 1000)}{random.choice(list)}'