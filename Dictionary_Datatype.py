

dict1 = {'a':2,'c':1,'b':10}
dict2 = {'X':20}
print("Combine the two dictionaries")
result = dict1.copy()
# copied dict1 objects to new dict result by using shallow copy
result.update(dict2)
print("combining to dictinaries: ",result)

print("Sort the dictionaries")
res = dict(sorted(dict1.items()))
res1 = dict(sorted(dict1.items(),key = lambda X:X[0]))
print(res)
print(res1)