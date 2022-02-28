# This is the solution to problem 1
# 2-8 Solution
# We will do addition, subtraction, multiplication, and
# Division with the print function
print(1+7)
print(9-1)
print(2*4)
print(16/2)

# 2-9 Solution
# Assigning 3 to variable favorite_number
favorite_number = 3
message = "My favorite number is {0}."
print(message.format(favorite_number))

# This is the solution to problem 2
# I define each number with a variable and put _ like how you would for commas
variable_A = 45_624
variable_B = 68_423_791
variable_C = 13_794_628
variable_D = 96_374

# Then we define a number_sets function and print the variables in order
def number_sets():
    print(variable_A)
    print(variable_B)
    print(variable_C)
    print(variable_D)

number_sets()

# This is the solution to problem 3
# First I define a function with 2 arguments and establish
# what the argument will be converted to.  Then I print the
# argument and display what type it is.  Last, I recall the function
# and give the arguments their actual value
def my_function(arg1, arg2):
    arg1 = float(arg1)
    arg2 = int(arg2)
    print(arg1, type(arg1))
    print(arg2, type(arg2))

my_function(72, 30.5)

# This is the solution to problem 4
# Defined the variable favorite_movie, then defined movie and times_seen
# print in the message format
# Then defined the message with placeholders and finally reused the function
def favorite_movie():
    movie = input("What is your favorite movie?")
    times_seen = int(input("How many times have you seen it?"))
    print(message.format(movie, times_seen))

message = "I have seen {0} {1} times."

favorite_movie()






