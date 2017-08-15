# VARIABLES for the code


#While many people around the country play horseshoes, you'll find a different game using circles in our state. Tailgate parties even play a smaller version of this using washers tossed into a coffee can with a nail banged in the center, known as Camden __5__.



import sys

# 1ST GAME OPTION
def easy_game():
  
  easy_quiz = "Many NJ residents love going to the beach in the summer, but they don't call it the 'beach'. They call it the ___.", "We  also have a large Italian-American population.  If you ever pass through the 'Burg', an area of Trenton, you must try a special kind of pizza called a tomato ___, which is more focused on the tomatos and less on the cheese.",  "After your meal, head on over to the Yankees minor league baseball team, the Trenton ___.  It's a beautiful park where every seat is close to the field.", "Actually, New Jersey isn't filled of highways.  There are very scenic portions, which is why it's known as the ___ State.",  "But up north in the section that is more metropolitan, we still have our only team of a major sport.  They are the New Jersey ___."
  temporary_answers = [___]
  easy_answers = ["shore", "pie", "Thunder", "Garden", "quoits"]
  
  count = 1 #if it reaches the max count it will end the quiz
  index = 0
  max_count = 6

  print easy_quiz[index]

  # THE QUIZ...
  guesses = 3
	while int(guesses) > 0 :
		user_input = raw_input("Wha's a matter you?  Fill in the blank!")
		if user_input == easy_anaswers[count - 1]:
			print "Oh, a wise guy!"
			easy_quiz[index] = play_game(easy_quiz[index],temporary_answers, user_input)
			print easy_quiz[index]
			index += 1
			count += 1
			if count == max_count:
				break
		else:
			guesses -= 1
			print "Wrong, dingbat! You still have " + str(guesses) + " guesses left."
		print easy_quiz[index]
	if guesses > 0:
		print "Congratulations on not being a stunad!  You finished the quiz!"
	else:
		print "You don't have any guesses left.  Please accept my condolences."

  # Allows user to take a different quiz/retake the quiz
	print " "
	new_quiz = raw_input("If you want to play another quiz you can type in the name (capitals, music or football). If you want to quit hit enter.")
	if new_quiz == "easy way":
		easy_game()
	elif new_quiz == "medium way":
		medium_quiz()
	elif new_quiz == "hard way":
		hard_quiz()
	else:
		sys.exit()


# 2ND GAME OPTION
def easy_game(quiz, blank_set):
  
  medium_quiz = ["New Jersey is home to many celebrities.  Some of them were da best celebrities.  Way back when there was ol' blue eyes, ___.",  "More recently was the Boss, known for his shown at the Stony Pony, ___.",  "But we also got actuhs.  There is the short, balding nut who played George on Seinfeld, ___.",  "And also da short Italian guy who epitimizes our state with his short temper.  ___ played roles in mafia movies, but also the lawyer in My Cousin Vinny.",  "Lastly, I don't want to leave out the famous women from Jersey.  The lovely ___ was in the popular film The Princess Diaries."]
  temporary_answers = [___]
  medium_answers = ["Frank Sinatra", "Bruce Springstein", "Jason Alexander", "Joe Pesci", "Anne Hathaway"]
  
  count = 1
	index = 0
	max_count = 6
	
	  # THE QUIZ...
  guesses = 3
	while int(guesses) > 0 :
		user_input = raw_input("Wha's a matter you?  Fill in the blank!")
		if user_input == easy_anaswers[count - 1]:
			print "Oh, a wise guy!"
			medium_quiz[index] = play_game(medium_quiz[index],temporary_answers, user_input)
			print medium_quiz[index]
			index += 1
			count += 1
			if count == max_count:
				break
		else:
			guesses -= 1
			print "Wrong, dingbat! You still have " + str(guesses) + " guesses left."
		print medium_quiz[index]
	if guesses > 0:
		print "Congratulations on not being a stunad!  You finished the quiz!"
	else:
		print "You don't have any guesses left.  Please accept my condolences."

  # Allows user to take a different quiz/retake the quiz
	print " "
	new_quiz = raw_input("If you want to play another quiz you can type in the name (capitals, music or football). If you want to quit hit enter.")
	if new_quiz == "easy way":
		easy_game()
	elif new_quiz == "medium way":
		medium_quiz()
	elif new_quiz == "hard way":
		hard_quiz()
	else:
		sys.exit()
	
	
def checkAnswer(word, solution):
    for element in solution:
        if element in word:
            return element
        return None


def play_game(ml_string, parts_of_speech, user_input):
    replaced = []
    ml_list = ml_string.split()

    for word in ml_list:
        replacement = checkAnswer(word, parts_of_speech)
        if replacement != None:
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


welcomeMessage = """Hey yo! Welcome to the Joisey Quiz! I hope yous guys have half uh brain to answer these questions correctly. Now we can do this the easy way, or the hard way... or the medium way.  Which will it be?"""

#Actual start of the program
print welcomeMessage
choice = raw_input("Select a categorie by typing it in.")
correctChoice = True
#Defensive programming: as long as the user hasn't typed in a correct categorie, the program will keep asking.
while correctChoice:
	if (choice == "easy way" or choice == "medium way" or choice =="hard way"):
		break
	print "Very creative, but that's not an option."
	choice = raw_input("Would you like the 'easy way', 'medium way', or 'hard way'?")

#Once a correct choise has been made, the program will start one of the three possible quizzes.
#This piece of code selects the right function.
if choice == "easy way":
	easy_game()
elif choice == "medium way":
	medium game()
else:
	hard game()

end = raw_input("Did ya enjoy the quiz?")
