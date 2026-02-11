#what is a while loop?

""" num = 10
while num > 0:
    print(num)
    num = num - 1 
print("Count finished!") """

""" will be creating a program that creates a random number and then
have the user guess the number. The code must contain all of the following
-Generate a random number between 1 and 10 (you can do more if you
want)
-Use a while loop that breaks only when the user correctly guesses the
number
-create a guess variable based on user input. There will be a global guess
variable equal to 0 and then another guess variable inside the while loop
based on user input
-using conditional statements, inform the user if their guess is less than or
greater than the random number
-push the users incorrect guess into a guess_history list. Print the used
letters at every wrong guess
-When the user guesses correctly inform them and show them their guess
history using a for loop """

import random # allows me to use the random thing to get a random number from my list. 
guess_history = []
x = 0
pos = [1,2,3,4,5,6,7,8,9,10]
rand = int(random.choice(pos)) 
guess = int(input("Guess an integer from 1-10:"))
while guess != rand:
    guess_history.append(guess)
    print("Incorrect! You have guessed these numbers so far..")
    print(guess_history)
    if guess > 10 or guess < 1:
        print("This number is out of bounds!")
    elif guess > rand:
        print("Guess lower!")
    elif guess < rand:
        print("Guess higher!") 
    guess = int(input("Guess an integer from 1-10:"))
print("Correct!")
print("You guessed previously..")

for guesses in guess_history:
    print(guess_history[0+x])
    x = x + 1