#Accessing a list

n = [1,3,5]

print(n[1]) #outputs 3

n[1] = n[1] * 5

print(n[1])

n.append(4)

print(n)

#.pop(index), .remove(actual value), .delete(list[index]) will all remove a value from the list
n.pop(3)
print(n)

#function refresher -> function with more than one argument

def add_values(x,y):
    return x+y

print(add_values(n[1],n[2]))

# Function with strings

sample_string = "This is "

def concactenate_string(string):
    return string + "some other thing"

print(concactenate_string(sample_string))

def first_item_in_list(item):
    return f"This is the first item: {item[0]}"

print(first_item_in_list(n))

# modifying a list in a function modifies the original list as well

# def multiply_index(list):
#     i = 0
#     while i < len(list):
#         list[i] = list[i] * 2
#         i +=1
#     return list

generic_list = [3,5,7]
# print (multiply_index(generic_list))

def multiply_index(list):
    for i in range(0, len(list)):
        list[i] = list[i] * 2
    print(list)

multiply_index(generic_list) # does the same as the while function above

def append_list(lst):
    lst.append(18)
    return lst

print(append_list(generic_list))

def print_each_list_index(x):
    for i in range(0, len(x)):
        print(x[i])

print_each_list_index(generic_list)

# The range function has three different versions:

# range(stop)
# range(start, stop)
# range(start, stop, step)
# In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.

# If omitted, start defaults to 0 and step defaults to 1.


#!does not work
# def create_number_list(x):
#     for i in range(0, len(x)):
#         x[i] = x[i]
#     return x

# print (create_number_list(range(3)))