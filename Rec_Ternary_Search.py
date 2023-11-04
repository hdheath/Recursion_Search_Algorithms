#Question 5 modify the binary search function so that it performs ternary
#search on a Python list, recursively!
    

def ternarySearchRec(alist, item):
    found = False

    ## set Midpoint values depending on returned list/size 
    segR = int(len(alist)//1.5)
    segL = len(alist)//3

    if alist == []:
        return False

    ## If value given is equal to either MP return True
    if alist[segL] == item or alist[segR] == item:
        return True

    ## if the value is greater than the right MP, return a list with
    ## the rest of the values to the right of the MP
    if item > alist[segR]:
        return ternarySearchRec(alist[segR + 1:], item)

    ## if the value is less than the left MP, return a list with the rest
    ## of the values to the left of the MP
    if item < alist[segL]:
        return ternarySearchRec(alist[:segL], item)

    ## if value is greater than the left MP, return a list with the rest
    ## of the values to the right of the MP
    elif item > alist[segL]:
        return ternarySearchRec(alist[segL + 1:], item)

    ##if not found, return found (false)
    else:
        return found

        
            








    
        
