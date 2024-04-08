
###? Syntax ###

print ("This will print in the console")
print ("Python 3 syntax uses parens for print")

print ("Adding" + " " + "lines together")

# mismatched quotes will cause SyntaxError 
# so will missing parens

###? Variables ###

todays_date = "3/11/24"
print (todays_date)

this_variable = "variable"
print (this_variable)

wordcount = 'wordcount'
print(wordcount)

number_variable = 13
print(number_variable)

#*math operators

addition_variable = 1000 + 9000
subtraction_var = 80 - 40
multiplication_var = 5 * 5
division_var = 30 / 5
combo_var = 120 * 2 + 25 / 10 - 5

print(addition_variable, subtraction_var, multiplication_var, division_var, combo_var)

#*updating variables

score = 10
print(score)
print ('Three pointer!!')
three_point_shot = 3
score = score + three_point_shot
print(score)

wallet = 40
whooper_meal = 14.99
sales_tax = .07 * whooper_meal

print(wallet, whooper_meal, sales_tax)

whooper_meal += sales_tax
wallet -= whooper_meal

print(wallet, whooper_meal, sales_tax)

#float gives back decimals
#it doesnt seem to be needed

no_float = 100 / 6
yes_float = float(100)/6

print(no_float, yes_float)

""" 
this
is
a
multi
line
comment
 """

multi_line_var = """ this
is also
multi line
 """
print (multi_line_var)

#Booleans

is_true = True
is_false = False

print (is_false, is_true)

# int str
""" 
int turns string variable value into an integer
str turns integer variable value into a string
int does not work on decimals that are strings
 """

age = 28
intro = "I am " + str(age) + " years old"
print(intro)

num1 = "2"
num2 = 3
turn_to_int = num2 + int(num1)
print (turn_to_int) 
num3 = 2.5
print (int(num3))