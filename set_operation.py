a = {1,2,3,4,5}
b = {3,4,5,6,7,8}
c = a.union(b)
d = b.union(a)
print(c , d) # -> No duplicates are allowed in sets
e = a.intersection(b)
print(e)