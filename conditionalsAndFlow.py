""" 
Comparators :
== equal to
!= not equal to
< less than
> greater than
<= less than or equal to
>= greater than or equal to

?The boolean operator not returns True for false statements and False for true statements.
not True = False
not False = True

not not False = False
not not True = True
 """

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

to_slice = "word"
to_slice = to_slice[1:len(to_slice)]
print(to_slice)

#check if to_print is empty or a word
to_print = input("Print to console: ")
if(len(to_print) > 0 and to_print.isalpha()) :
    print(to_print.lower())
elif(len(to_print) > 0) :
    print('not a valid string')
else :
    print("empty")
