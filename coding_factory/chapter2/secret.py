import random
import math

def main():
    secret: random.randint(1, 10)
    tries = 0
    MAX_TRIES = 5

    while True:
        tries += 1
        if tries > MAX_TRIES: break

        num = int(input("give an int"))
        if num == secret:
            print("bingo")
            break
        elif math.fabs(num - secret) <= 5:    
            print("hot")
        else:
            print("cold")

        if tries == MAX_TRIES:
            print(MAX_TRIES)    



main()            
