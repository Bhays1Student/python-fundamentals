# Here is the solution to 2-3 Personal Message
# Labeling the literal "Sam" with the variable name
# Then I establish a msg for a print function to display
# with (msg.format(name))
name = "Sam"

msg = "Hello, {0}, how is your weekend going?\n"
print(msg.format(name))

# Here is the solution to 2-4 Name Cases
name_again = "Sam\n"

# First, we will do the lowercase with the lower() method
print(name_again.lower())

# Now we will do uppercase with the upper() method
print(name_again.upper())

# Finally, we will do the title() method
print(name_again.title())

# Here is the solution to 2-5 Famous Quote
print('\tGeorge Washington once said, "Knowledge is in '
      'every country\n\tthe surest basis of public happiness."\n')

# Here is the solution to 2-6 Famous Quote 2
# Assigning literal "George Washington" to variable famous_person
# Assigning quote to variable message
# combining the two variables using concatenation function
famous_person = "\tGeorge Washington"
message = "Knowledge is in every country\n\tthe surest basis of public happiness."
combine = famous_person + ' once said, "' + message + '"'
print(combine)

# This is the solution to 2-7 Stripping Names
# First we give a name a variable
# We will use Sam again
person_name = " \n\t Sam Hays\n "
print(person_name)

# Now we will do the strip() methods
# The lstrip() method removes the space as well as\n\t so there is
# only a space below
print(person_name.lstrip())
# The rstrip() removes the \n and space so there is a space above
# the name and does a tab space
print(person_name.rstrip())
# The strip() method strips the literal of everything so it
# prints like normal
print(person_name.strip())