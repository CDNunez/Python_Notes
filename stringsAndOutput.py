from _datetime import datetime

print('This is a way to use single quotes within quotes: isn\'t')

#targeting specific letters within strings

fifth_letter = "MONTY"[4]
print (fifth_letter)

print (len(fifth_letter))

long_var = 'this is a long string'
print(len(long_var))

to_lower = "SET THIS TO LOWERCASE"
print (to_lower.lower())

to_upper = 'set this to uppercase'
print (to_upper.upper())

to_string = 2024
print(str(to_string))

#? dot notation methods only work with strings

conc_to_string = "The year is " + str(2024)
print(conc_to_string)

#another way to conc is with %

string_1 = "Hello"
string_2 ="friend"

print("%s darkness my old %s" % (string_1, string_2))

# fill = "fill"
# the = 'the'
# blanks = 'blanks'

# print("%s in %s %s" % (fill, the, blanks))
#*both methods of filling in the blanks work
print("%s in %s %s" % ("fill", "the", "blanks"))

#* requires datetime import
print(datetime.now())

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

#formatting date
print('%02d/%02d/%04d' % (now.month, now.day, now.year))

#formatting time
print ('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

#date and time timestamp
print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))