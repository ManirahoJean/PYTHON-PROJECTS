# Using continue in a Loop

"""""
Rather than breaking out of a loop entirely without executing the rest of its 
code, you can use the continue statement to return to the beginning of the 
loop based on the result of a conditional test. For example, consider a loop 
that counts from 1 to 10 but prints only the odd numbers in that range

"""""

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print("\n")

# Avoiding Infinite Loops

# Every while loop needs a way to stop running so it won’t continue to run
# forever. For example, this counting loop should count from 1 to 5:

x = 1
while x <= 5:
    x += 1
    print(x)

# But if you accidentally omit the line x += 1,  the loop
# will run forever:

# Every programmer accidentally writes an infinite while loop from time
# to time, especially when a program’s loops have subtle exit conditions

# If your program gets stuck in an infinite loop,
# press ctrl-C or just close the
# terminal window displaying your program’s output.
