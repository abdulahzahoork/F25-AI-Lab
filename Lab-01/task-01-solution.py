# Run the program below. Try different integer values, and note down what happens and any errors you need to fix:

x = int(input("Please enter an integer: "))
if x < 0:
 x = 0 
 print('Negative changed to zero')
elif x == 0:
 print('Zero')
elif x == 1:
 print('Single')
else:
 print('More')

# The program is syntactically correct and will execute without any errors. 
# The only error occurs if the user does not enter an integer. To resolve this, we can use try/except.

try:
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0 
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
except(ValueError):
    print("Please enter a valid integer.")