import random
#The while loop is similar to an if statement: it executes the code inside of it if some condition is true. The difference is that the while loop will continue to execute as long as the condition is true. In other words, instead of executing if something is true, it executes while that thing is true

# example while loops

loop_condition = True

while loop_condition:
    print("I am a loop")
    loop_condition = False

count = 0

while count < 10 :
    print(f"Count: {count}")
    count += 1

num = 1

while num < 11:
    num_squared = num ** 2
    print(num_squared)
    num+=1

# different way to break out of a while loop or loop. Using the word break
loop = 0

while True:
    print (f"Count: {loop}")
    loop += 1
    if loop >=10:
        break

# While/Else
#  while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition is evaluated to False. This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

coin = 0
while coin < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  coin += 1
else:
  print ("You win!")