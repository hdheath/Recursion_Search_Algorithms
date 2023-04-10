#Question 4 modify the binary search function so that it performs ternary
#search on a Python list.


def ternarySearch(alist, item):
  ## initialize values of given list
  first = 0
  last = len(alist) - 1

  ## while the entire list has not been searched:
  while first <= last:
    found = False

  ## set both midpoints, one 2/3 into the list and the other a 1/3
  ## through the list
    seg2 = last - (last - first)//3
    seg1 = first + (last - first)//3

  ## return true if either midpoints is equal to given value 
    if alist[seg1] == item or alist[seg2] == item:
        return True

  ## if item is larger than item at 2nd MP, move MPs closer to end of list 
    if item > alist[seg2]:
        first = seg2 + 1

  ## if item is less than item at 1st MP, move MPs closer to beginning of list
    if item < alist[seg1]:
        last = seg1 - 1

  ## otherwise move both MPs towards the middle of the list 
    else:
        last = seg2 - 1
        first = seg1 + 1

  ## if not found, return false  
  return found


