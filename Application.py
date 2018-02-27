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

def display_separator(symbol):
    lines = symbol * 58
    print(lines)

def input_code(item_list):
	code = input("Enter item code: ")
	item = item_list.find_item(code)
	return item

def get_user_input(start,end):
	choice = input("Enter your choice: ")
	while (not choice.isdigit() or int(choice) > end or int(choice) < start):
		print("Invalid option.")
		choice = input("Please try again: ")
	return int(choice)
	
def matchPlayers(playersList, tournament):
	round = Round(playersList)
	tournament.addRound(round)
	roundNo = tournament.getRoundNo()
	print("Match Players (Round " + str(roundNo) + ")")
	print()
	round.matchPlayers(tournament)
	
def showScores(playersList, tournament):
	print()
	plist = list(playersList.values())
	for player in plist:
		gamePt = player.getGamePt()
		gamePerc = player.getGamePerc()
		matchPt = player.getMatchPt()
		matchPerc = player.getMatchPerc()
	plist.sort(key=lambda x: (x.getMatchPt(), x.getOppMatchPerc(), x.getGamePerc(), x.getOppGamePerc()), reverse=True)
	count = 1
	maxPlayerLen = tournament.getMaxPlayerLen() + 1
	if (maxPlayerLen < 10):
		maxPlayerLen = 10
	print(('Rank  {:<' + str(maxPlayerLen) + '} MatchScore  MatchPts    MatchPerc   OppMatchPerc  GameScore   GamePts   GamePerc   OppGamePerc  Opponents').format('Player'))
	for player in plist:
		stats = player.displayStats(maxPlayerLen)
		print((str(count) + '.\t').expandtabs(6) + stats)
		count += 1
	
def editScores(tournament):
	print("Edit Scores")
	print()
	tournament.displayRounds()
	rounds = tournament.getRoundNo()
	if (rounds != 0):
		print(str(rounds+1) + ". Cancel")
		display_separator("-")
		option = get_user_input(1, rounds+1)
		display_separator("-")
		if (option != (rounds+1)):
			round = tournament.getRound(option)
			print("Edit Scores (Round " + str(option) + ")")
			print()
			round.displayRound(tournament)
			matches = round.getMatchNo()
			print(str(matches+1) + ". Cancel")
			display_separator("-")
			option = get_user_input(1, matches+1)
			display_separator("-")
			if (option != (matches+1)):
				match = round.getMatch(option)
				print("Edit Scores (Match " + str(option) + ")")
				print()
				match.displayMatch(tournament.getMaxPlayerLen())
				player1 = match.getPlayer1()
				player2 = match.getPlayer2()
				display_separator("-")
				if (player2 != "bye"):
					if (match.getPlayed() == "yes"):
						match.resetScores()
					while True:
						try:
							player1Score = int(input(player1.getName() + "'s Score: "))
							if (player1Score > 2 or player1Score < 0):
								print("Invalid input.")
							else:
								break
						except ValueError:
							print("Invalid input.")
					while True:
						try:
							player2Score = int(input(player2.getName() + "'s Score: "))
							if (player2Score > 2 or player2Score < 0):
								print("Invalid input.")
							else:
								break
						except ValueError:
							print("Invalid input.")
					match.setPlayed()
					match.setPlayer1Score(player1Score)
					match.setPlayer2Score(player2Score)
					winner = match.getWinner()
				else:
					print("Cannot edit score.")
	else:
		print("No rounds have been played.")

def main_menu(playersList, tournament):
	display_menu()
	display_separator("-")
	option = get_user_input(1,5)
	while option != 5:
		display_separator("-")
		if option == 1:
			matchPlayers(playersList, tournament)
		elif option == 2:
			print("Show Scores")
			showScores(playersList, tournament)
		elif option == 3:
			editScores(tournament)
		else:
			tournament.displayTournament()
		display_separator("=")
		display_menu()
		display_separator("-")
		option = get_user_input(1,5)
	display_separator("=")
	print("Final Ranking")
	showScores(playersList, tournament)
	display_separator("=")

def players(noOfPlayers, tournament):
	playersList = {}
	for i in range(1, noOfPlayers+1):
		name = input("Player " + str(i) + ": ")
		player = Player(i, name)
		playersList[i] = player
		tournament.addPlayer(player)
	return playersList	

def main():
	display_separator("=")
	display_intro()
	display_separator("=")
	while True:
		try:
			noOfPlayers = int(input("Number of players: "))
			if (noOfPlayers < 2):
				print("Not enough players. Please try again.")
			else:
				break
		except ValueError:
			print("Invalid input. Please Try again.")
	tournament = Tournament()
	playersList = players(noOfPlayers, tournament)
	display_separator("-")
	main_menu(playersList, tournament)

main()