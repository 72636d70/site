from random import randint

number = randint(1,100)
guess = 0
attempts = 0
print "Welcome, user!\nThe computer has chosen a number between 1 and 100"
print "Please try to guess the number!"

while (guess != number):
	guess = input("Guess: ")
	attempts += 1
	if (guess > number):
		print "Your guess is higher!"
	elif (guess < number):
		print "Your guess is lower!"
	elif (guess == number):
		print "Congratulations, the number was %r. It took you %r attempts." \
		% (number, attempts)
	else:
		print "Invalid Choice"