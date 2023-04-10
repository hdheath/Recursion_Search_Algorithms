#Question 3 Assume you are climbing a ladder. The ladder has n rungs.
#You can only climb one or two rungs at a time.
#How many different ways can you climb to the top?

def ladder(n):
    if n is 2:
        return 2
    elif n is 1 or n is 0:
        return 1

    #recursively call down to n = 2, then add up values to n , 2 rung and 1 rung
    #for each n value 
    else:
        return ladder(n-2) + ladder(n-1) 
