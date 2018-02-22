import random
from Match import Match
from Player import Player

class Round:
	def __init__(self, playersList):
		self.round = []						#list of games
		self.playersList = playersList		#list of players
		self.matchNo = 0
	
	def addMatch(self, match):
		self.round.append(match)
		self.matchNo += 1
		
	def getMatch(self, option):
		return self.round[option-1]
		
	def getMatchNo(self):
		return self.matchNo
		
	def matchPlayers(self, tournament):
		plist = list(self.playersList.values())
		random.shuffle(plist)
		plist.sort(key=lambda x: (x.getMatchPt(), x.getOppMatchPerc(), x.getGamePerc(), x.getOppGamePerc()), reverse=True)
		for i in range(0, len(plist), 2):
			player1 = plist[i]
			player1.setMatches()
			player2 = ""
			if (i == len(plist)-1):
				player2 = "bye"
			else:
				player2 = plist[i+1]
				player2.setMatches()
				player2.addOppList(player1)
			player1.addOppList(player2)
			match = Match(player1, player2)
			if (player2 == "bye"):
				match.setPlayer1Score(2)
				match.getWinner()
			self.addMatch(match)
		self.displayRound(tournament)
			
	def displayRound(self, tournament):
		count = 1
		for match in self.round:
			match.displayMatches(tournament, count)
			count += 1
			