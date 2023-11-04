# Recursive Search Algorithms Collection

## Overview 
This repository contains a collection of recursive search algorithms implemented in Python. The algorithms include searching within an unordered list, finding the last value in such a list, calculating the number of ways to climb a ladder with a given number of rungs, and performing ternary searches both iteratively and recursively.

## Algorithms 
1. Recursive Search in Unordered List: Determines if a value is present in the list.
2. Find Last Value: Retrieves the last value in the list.
3. Ladder Climbing: Counts the different ways to climb to the top of a ladder with n rungs.
4. Iterative Ternary Search: A ternary search algorithm implemented iteratively.
5. Recursive Ternary Search: A ternary search algorithm implemented recursively.

## Usage 
Recursive Search in Unordered List
```
from recursive_algorithms import searchRec, Node, UnorderedList

# Create unordered list and add elements
my_list = UnorderedList()
my_list.add(70)
my_list.add(50)
my_list.add(20)
my_list.add(30)

# Search for an element recursively
item_to_search = 20
is_found = searchRec(item_to_search, my_list.head)
print(is_found)  # Outputs True if found, False otherwise
```
Find Last Value

```
from recursive_algorithms import findLastValue

# Assuming 'my_list' has been previously created and populated
last_value = findLastValue(my_list.head)
print(last_value)  # Outputs the last value in the list
```
Ladder Climbing 
```
from recursive_algorithms import ladder

number_of_rungs = 5
ways_to_climb = ladder(number_of_rungs)
print(ways_to_climb)  # Outputs the number of ways to climb the ladder

```

Iterative Ternary Search
```
from recursive_algorithms import ternarySearch

# Ensure the list is sorted before searching
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item_to_find = 7

is_present = ternarySearch(sorted_list, item_to_find)
print(is_present)  # Outputs True if found, False otherwise

```

Recursive Ternary Search
```
from recursive_algorithms import ternarySearchRec

# Ensure the list is sorted before searching
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item_to_find = 7

is_present = ternarySearchRec(sorted_list, item_to_find)
print(is_present)  # Outputs True if found, False otherwise

```
## Requirements 
Python 3.x

## Author 
Harrison Heath 
