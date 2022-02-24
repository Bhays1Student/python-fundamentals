# Can I make a typo that generates an error?
# I am able to if I do something wrong such as spell print incorrectly
# When putting rint instead of print, it gave me the error code that
# rint is not defined.
# Can you make sense of the error?
# Yes since incorrectly typing the actual command would throw things
# off completely.
print("Exercise for Hello World.\n")
print("Hello Python World!\n")

# Can you make a typo that doesn't generate an error?
# Yes if I were to put something such as print("Hello Pythoo World"),
# it does not give an error back and just repeats the phrase as intended.
# Why do you think it didn't make an error?
# Because the command itself was correctly typed, it was still able
# to understand what I was trying to say, and it said it even though
# Python was incorrectly spelled.
print("Hello Pythoo World Yet Again!\n")
print("-----")
# In order to display the Zen of Python, you must type the following: import this
# That will be of course without the number symbol or anything else.

import this

# I am assigning this variable the message, "How are you?"
message = "How are you?"

# As before, I am assigning a variable the note "How are you?"
note = "How are you?\n"
print(note)

# I then changed the note to "How are you doing today?"
note = "How are you doing today?\n"
print(note)


# This is code for exercise 8-1
def display_message():
    """Display messages."""
    print("I learned about how arguments and parameters work.")


display_message()

# This is code for exercise 8-2

def favorite_book(title):
    """Display favorite book."""
    print(f"One of my favorite books is {title.title()}!")

favorite_book("alice in wonderland")