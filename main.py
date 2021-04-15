from os import system
from time import sleep
from random import randrange, choice

class bcolors:
    YELLOW = '\033[1;33'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    PURPLE = '\033[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Globals
user = 0
questions_answered = 0
health = 50
i = 5
dif = 1
teacher_finish = ["Stay were you belong... In my memories...", "You are dead...", "HAHAHAHAHA!!!!!!!", "DIE YOU FOOL!!! HAHAHAHAHA!!!!!!!!!"]
teacher_quote = ["I'm glad your dead... HAHAHAHAHA!!!", "Get better soon...", "Wow, you are terrible..."]
teacher_rematch = ["You want to get beat down again?", "Do you want to die again?", "Do you want to try again... And DIE!!!!!", "HAHAHAHAHA... do you want to get killed again?"]
names = ["stupid", "dumb", "bad"]
correct_qoutes = ["meh.", "Okay.", "Fine."]
wrong_quotes = ["Bang.", "Slice.", "HAHAHAHAHA...", "Easy", "You will DIE!!!", "VANISH!!!", "NOPE.", "?!?!?!", "JUST WHY!!!"]
type_error_qoutes = ["Learn HOw To tYPE A STUPID NUMBER!!!!!!!!!!!!!!!", "tHat ISn't A numBER!?!?! Why ARE yOu sO DUmB????????!!!!!", "NuMBERS ONlY!?!!? yOU SUCK aT mATH!!!"]


# Game start
system("clear")

try:
	game = input(f"{bcolors.OKGREEN}{bcolors.BOLD}\tMATH-KILLER\n\n{bcolors.ENDC}[PRESS ENTER TO START GAME]\n")

	if game == "":
		system("clear")
	else:
		system("clear")
		exit()
except KeyboardInterrupt:
	system("clear")
	exit()


while True:
	try:
		problem = f"{randrange(1, i)} * {randrange(1, i)}"
		answer = eval(problem)
		
		system("clear")
		print(f"{bcolors.UNDERLINE}CURRENT PROBLEM: {questions_answered + 1} | Health: {health}{bcolors.ENDC}\n")

		try:
			user = int(input(f"{bcolors.UNDERLINE}{problem}{bcolors.ENDC} = "))
		except ValueError:
			system("clear")

			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}{problem} = INVALID NUMBER!!!{bcolors.ENDC}")

			sleep(0.5)
			print(choice(type_error_qoutes))
			sleep(2)
			system("clear")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print("YOU LOSE...")
			print(f"Questions answered: {questions_answered}")
			input("\n[PRESS ANY KEY TO CONTINUE]")
			system("clear")
			break


		if user == answer:
			system("clear")
			print(f"CURRENT PROBLEM: {questions_answered + 1} | Health: {bcolors.UNDERLINE}{bcolors.OKGREEN}{bcolors.BOLD}{health}{bcolors.ENDC}\n")
			print(f"{bcolors.UNDERLINE}{bcolors.OKGREEN}{bcolors.BOLD}{problem} = {user}{bcolors.ENDC}")
			print(choice(correct_qoutes))
			sleep(0.5)
		else:
			health -= dif * 5
			system("clear")
			
			if health <= 0:
				print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD\n")
			else:
				print(f"CURRENT PROBLEM: {questions_answered + 1} | Health: {bcolors.FAIL}{bcolors.UNDERLINE}{health}{bcolors.ENDC}\n")
			

			print(f"{bcolors.FAIL}{bcolors.UNDERLINE}{problem} = {user}{bcolors.ENDC}")
						
			sleep(0.5)
			print(f"The answer was {answer}.")
			sleep(0.5)
			print(f"{choice(wrong_quotes)}")
			sleep(0.5)
			print(f"-{dif*5}, Your health is now: {health}")

			if health <= 0:
				sleep(0.5)
				print("YOU ARE NOW DEAD...")
			sleep(2)

		dif += 1
		i += 1
		questions_answered += 1

		if health <= 0:
			system("clear")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			sleep(0.5)
			print(choice(teacher_quote))
			sleep(0.5)
			print(choice(teacher_finish))
			sleep(0.5)
			rematch = input(f"{choice(teacher_rematch)}\n> ").lower()

			if "y" in rematch:
				system("clear")
				questions_answered = 0
				health = 50
				i = 5
				dif = 1
			else:
				system("clear")
				print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
				print("YOU LOSE...")
				print(f"Questions answered: {questions_answered}")
				input("\n[PRESS ANY KEY TO CONTINUE]")
				system("clear")
				break
	except KeyboardInterrupt:
			system("clear")

			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}{problem} = ^C{bcolors.ENDC}")

			sleep(0.5)
			print(choice(teacher_quote))
			sleep(2)
			system("clear")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print("YOU LOSE...")
			print(f"Questions answered: {questions_answered}")
			input("\n[PRESS ANY KEY TO CONTINUE]")
			system("clear")
			break