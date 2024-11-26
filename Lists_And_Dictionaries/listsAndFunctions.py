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