
#*lists are to python what arrays are to JS and dictionaries are to PY what objects are to JS

#? Intro to List

# lists seem to work the same as arrays in JS
list_name = ["item_1", "item_2"]

#can splice in list item directly
list_name[1] = "item_3"
print(list_name)

#*append and length of list method
empty_list = []
empty_list.append('fill_1')
empty_list.append('fill_2')
empty_list.append('fill_3')
list_length = len(empty_list)
print ("Empty list has %d items" % (list_length))
print(empty_list)

#* lists can also store variables
variable_list = []
variable_item_one = True
variable_item_two = False
#! append only takes one argument
variable_list.append(variable_item_one)
variable_list.append(variable_item_two)
variable_length = len(variable_list)
print(variable_length, variable_list)

#* slice method
slice_me = ['slice_one','slice_two','slice_three','slice_four','slice_five']

first = slice_me[0:2]
middle = slice_me[2:4]
last = slice_me[3:6]
print(first,middle,last)

# slice also works on strings as strings can be accessed the same as lists

together = 'splitthisstring'
split = together[:5]
this = together[5:9]
string = together[9:]
print(split,this,string)

#* index and insert method
##index is to search for the index for a specific item in a list
print(slice_me.index('slice_three'))#prints 2

#insert pushes item to a designated index on the list
slice_me.insert(0,"slice_zero")
print(slice_me)

#should have named push or insert list
replace_list = ['replace_one', 'replace_two', 'replace_three']

replace_two_index = replace_list.index('replace_two')
replace_list.insert(replace_two_index,"replace_one_point_five")

print(replace_list)

#for loop

number_list = [1,3,5,7,11]

for number in number_list:
    print(number / 2)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
odd_numbers = []

for number in numbers:
    if(number % 2 != 0):
        odd_numbers.append(number)
odd_numbers.sort()

print(odd_numbers)

#? Intro to Dictionaries

full_name = {'first name' : "John", 'middle name' : " ", 'last name' : 'Doe'}
print(full_name)
print(full_name['first name'], full_name['middle name'],full_name['last name'])

empty_dictionary = {}
empty_dictionary['pair one'] = "value one"
empty_dictionary['pair two'] = "value two"
empty_dictionary['pair three'] = "value three"
empty_dictionary['list one'] = [1,2,3,4,5]
empty_dictionary['list two'] = ['one','two','three', 'four']

test_var_one = 'one' 
test_var_two = 'two' 
test_var_three = 'three'

empty_dictionary['list three'] = [test_var_one, test_var_two, test_var_three]

print(empty_dictionary)
print(empty_dictionary['list one'])

# delete method
del empty_dictionary['pair three']
print (empty_dictionary)

#remove method
slice_me.remove('slice_one')
print(slice_me)

print (empty_dictionary['list two'][1]) #prints 'two' -- selecting specific data from list within dictionary

print(empty_dictionary['list three'][0]) #prints one -- prints the value of the variable within the list inside the dictionary