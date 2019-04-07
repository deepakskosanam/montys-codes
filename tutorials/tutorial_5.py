# PYTHON TUTORIALS 5
""" DATA STRUCTURES """

# More on Lists: Methods
"""
list.append(x) # Equals a[len(a):] = [x]
list.extend(x) # Equals a[len(a):] = iterable
list.insert(i.x)
    # a.insert(0,x) inserts at the front of List
    # a.insert(len(a),x) inserts at end of list. Equals a.append(x)
list.remove(x) # Removes first occurance of value "x"
list.pop(i) # Removes and returns i-th element. No "i" removes last element.
list.clear() # Removes all elements. Equals "del a[:]"
list.index(x[,start[,end]]) # First Item with value "x". Options narrow subsequence
list.count(x) # Count of value "x"
list.sort(key = none, reverse = False) #sort items in place (SEE SORTED())
list.reverse() # reverse elements in List
list.copy() # Return a shallow copy of the List. Equals a[:]
SHALLOW COPY: References original list values. Editing copy will modify original.
DEEP COPY: Complete and independent copy of original list.
"""
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting a position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()

# USE .append and .pop to add/remove elements to the end of Lists

# Add/remove from both ends of a List
# USE collections.deque
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
queue                           # Remaining queue in order of arrival
