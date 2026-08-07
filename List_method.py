marks = [99,39,90,73,92,99,99,99]

marks.append(63) # this will change the original list [99,39,90,73,92,63]
print(marks)
marks.reverse()
print(marks)
marks.remove(73)
print(marks)
marks.copy()
print(marks)
marks.extend("Ransom")
print(marks)
marks.insert(11,3)
print(marks)
ans = marks.count(99)
print(ans)