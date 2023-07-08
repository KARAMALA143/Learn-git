
print("Tuple: which is an immutable object")
print("Its is an ordered colelction type")
my_tuple = (1,2,'a')
my_tupl1 = (3,'ab',10)
res = my_tuple + my_tupl1
print(res)

print("Can you pass a list as a key to a dictionary?")
print("Directly No, but through tuples i can do")

my_list = [1,2,3]
my_tuple = tuple(my_list)
my_dict = {}
my_dict[my_tuple] = "Numbers"
print(my_dict)