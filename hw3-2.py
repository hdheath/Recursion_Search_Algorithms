#Question 2 Use Python and recursion to write a function called findLastValue(head)
#that returns the last value in an unordered list.

class Node:
  def __init__(self, data):
   self.data = data
   self.next = None
    
  def getData(self):
    return self.data
  
  def getNext(self):
    return self.next
    
  def setData(self, newdata):
    self.data = newdata
    
  def setNext(self, newnext):
    self.next = newnext

class UnorderedList:
  def __init__(self):
    self.head = None
    
  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
    
  def isEmpty(self):
    return self.head == None

  def length(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()
    return count
    
  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    return found 

def searchRec(item, head): 
    
    if item == head.getData():
        return True
    elif head == None:
        return False
    elif head.getNext() is None:
        return False
    else:
        return searchRec(item, head.getNext())
        
def findLastValue(head) :
    if head.getData() == None:
        return print("Invalid Parameters, Try Again")
    if head.getNext() == None:
        return head.getData()
    else:
        return findLastValue(head.getNext())



















    
