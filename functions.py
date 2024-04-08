#generic import of a python module
import math

""" 
function import
from module import function
from math import sqrt
 """

""" 
Universal import
from module import *
from math import *
 """

""" 
Universal imports may look great on the surface, but theyre not a good idea for one very important reason: they fill your program with a ton of variable and function names without the safety of those names still being associated with the module(s) they came from.

If you have a function of your very own named sqrt and you import math, your function is safe: there is your sqrt and there is math.sqrt. If you do from math import *, however, you have a problem: namely, two different functions with the exact same name.

Even if your own definitions dont directly conflict with names from imported modules, if you import * from several modules at once, you wont be able to figure out which variable or function came from where.

For these reasons, its best to stick with either import module and type module.name or just import specific variables and functions from various modules as needed.
 """

""" 
to find out which functions exists in a module you can
import module
everything_in_module = dir(module)
print (everything_in_module)
 """

#?Functions
""" 
functions are defined by def keyword
and the block of code to run 
EX:
def hello_world():
print ("Hello World!")
 """

def printing_press():
    print("Start Production")

printing_press()

print(math.sqrt(25))

highest_num = max(10,100,50,20,25)
lowest_num = min(10,100,50,20,25)
absolute_num = abs(-25)

print ("returns highest value",highest_num,"returns lowest value", lowest_num,"returns absolute value from zero", absolute_num)

#type functions similar to JS typeof
print (type(42))
print (type(4.2))
print (type('spam'))