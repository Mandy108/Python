s = {1,3,4,5,66,77}
print(s)

s.add(32)
s.add(42)
s.remove(77)
# s.remove(9999) #key error -> that means this element is not available in this set
s.discard(88585) # remove this element in this set only if element exists in the sets
s.pop() # remove random element from the sets
print(s)