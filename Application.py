from Player import Player
from Match import Match
from Round import Round
from Tournament import Tournament

def display_intro():
    message = "Tournament Ladder App by Henry Wong"
    print(message)

def display_menu():
	print("1. Match Players")
	print("2. Show Scores")
	print("3. Edit Scores")
	print("4. Show Match History")
	print("5. Finish")

def display_separator():
    lines = "-" * 58
    print(lines)

def input_code(item_list):
	code = input("Enter item code: ")
	item = item_list.find_item(code)
	return item

def get_user_input(start,end):
	choice = input("Enter your choice: ")
	while (not choice.isdigit() or int(choice) > end or int(choice) < start):
		print("Invalid menu option.")
		choice = input("Please try again: ")
	return int(choice)

def matchPlayers(playersList, tournament):
	round = Round(playersList)
	tournament.addRound(round)
	roundNo = tournament.getRound()
	print("Round " + str(roundNo))
	print()
	round.matchPlayers()
	
def showScores(playersList):
	plist = list(playersList.values())
	plist.sort(key=lambda x: (x.getPlayerNo(), x.getMatchPt(), x.getOppMatchPerc(), x.getGamePerc(), ))
	count = 1
	print("Rank  Player    W-L-T     Match Pts")
	for player in plist:
		stats = player.displayStats()
		# if (len(str(count)) > 1):
			# print(str(count) + ('.\t').expandtabs(2) + stats)
		# else:
		print((str(count) + '.\t').expandtabs(6) + stats)
		count += 1
	
def editScores():
	#TODO
	pass
	
def main_menu(playersList, tournament):
	display_menu()
	display_separator()
	option = get_user_input(1,5)
	while option != 5:
		display_separator()
		if option == 1:
			matchPlayers(playersList, tournament)
		elif option == 2:
			showScores(playersList)
		elif option == 3:
			editScores()
		else:
			tournament.displayTournament()
		display_separator()
		display_menu()
		display_separator()
		option = get_user_input(1,6)
	line = "=" * 58
	print(line)
	showScores(playersList)
	print(line)

def players(noOfPlayers):
	playersList = {}
	for i in range(1, noOfPlayers+1):
		name = input("Player " + str(i) + ": ")
		player = Player(i, name)
		playersList[name] = player
	#print(playersList)
	return playersList	

def main():
	line = "=" * 58
	print(line)
	display_intro()
	print(line)
	while True:
		try:
			noOfPlayers = int(input("Number of players: "))
			if (noOfPlayers < 2):
				print("Not enough players. Please try again.")
			else:
				break
		except ValueError:
			print("Invalid input. Please Try again.")
	playersList = players(noOfPlayers)
	display_separator()
	tournament = Tournament()
	main_menu(playersList, tournament)

main()