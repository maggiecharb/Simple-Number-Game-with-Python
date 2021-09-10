import random
import math 
 
name = (input("Enter your name:"))
print("\nHello" + " " + name + "," + " " + "how are you doing today?")
answer = input("\nGood or bad?")

myList1 = ["\nGlad to hear it!", "\nNice!", "\nThat's awesome.", "\nSounds great!"]
if (answer == ("Good")) or (answer == ("good")): 
	print(random.choice(myList1) + " " + "Want to play a game?")
myList2 = ["\nAww man.", "\nI'm sorry :(", "\nTomorrow will be better!"]
if (answer == ("Bad")) or (answer == ("bad")):
	print(random.choice(myList2) + " " + "Want to play a game?")
		
answer2 = input("\nYes or no?")

myList3 = ["\nToo low!", "\nA little higher!", "\nClose! Try a larger number."]
myList4 = ["\nToo high!", "\nA little lower!", "\nClose! Try a smaller number."]
myList5 = ["\nYou got it!", "\nThat is correct!", "\nGreat job!"]

if (answer2 == ("Yes")) or (answer2 == ("yes")):
	number = random.randint(1,100)
	print("\nAlright" + " " + name + ", I am thinking of a number 1-100. What is it?")
	guesses = 0
	
	while guesses < 5:
		print("\nTake a guess:")
		guess = input()
		guess = int(guess)
		guesses = guesses + 1
		
		if (guess < number) and (guesses < 5):
			print(random.choice(myList3))
			
		if (guess > number) and (guesses < 5):
			print(random.choice(myList4))
			
		if guess == number:
			break
			
	if guess == number:
		print(random.choice(myList5) + " " + "It took you" + " " + str(guesses) + " " + "tries. Press any key to exit the command panel.")
		
	if guess != number:
		print("\nNice try. The number was" + " " + str(number) + ". Press any key to exit the command panel.")
		
myList6 = ["\nHave a good day!", "\nMaybe tomorrow!", "\nSee ya later!"]
		
if (answer2 == ("No")) or (answer2 == ("no")):
	print(random.choice(myList6) + " " + "Press any key to exit the command panel.")
