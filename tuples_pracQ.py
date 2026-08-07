# Create a tuple coordinates = (10, 20) and print both elements

s = (10, 20)
print(s)

# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.

# s[0]= 50
# print(s) # error because tuples are immutable

# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

s_list = list(s) # Convert tuples to list
s_list[0] = 50
print(s_list)

s = tuple(s_list) # convert list to tuples 
print(s)