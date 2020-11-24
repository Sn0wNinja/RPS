from random import randint


print("Rock...")
print("Paper...")
print("Scissors...")
print("")


while True:
	
	comp_choice = randint(0, 2)
	
	try:
		player = input("Please enter your choice: ").lower()

		if player == "paper":
			if comp_choice == 0:
				print("Player has won!")
			elif comp_choice == 1:
				print("It's a tie!")
			else:
				print("Computer has won!")
		elif player == "scissors":
			if comp_choice == 1:
				print("Player has won!")
			elif comp_choice == 2:
				print("It's a tie!")
			else:
				print("Computer has won!")
		elif player == "rock":	
			if comp_choice == 2:
				print("Player has won!")
			elif comp_choice == 0:
				print("It's a tie!")
			else:
				print("Computer has won!")

		else: 
			print("Something went wrong!")
	except:
		pass
	else:
		wanna = input("Wanna play again? Y or N ").lower()

		if wanna == "y":
			print("Okay, let's do this!")
		elif wanna == "n":
			print("Shame, see you next time")
			break