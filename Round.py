import random
from Match import Match

class Round:
	def __init__(self, playersList):
		self.round = []						#list of games
		self.playersList = playersList		#list of players
		
	def addMatch(self, match):
		self.round.append(match)
		
	def matchPlayers(self):
		plist = list(self.playersList.values())
		random.shuffle(plist)
		plist.sort(key=lambda x: x.getMatchPt())
		for i in range(0, len(plist), 2):
			player1 = plist[i]
			player2 = ""
			if (i == len(plist)-1):
				player2 = "bye"
			else:
				player2 = plist[i+1]
			match = Match(player1, player2)
			self.addMatch(match)
		self.displayRound()
		
	def displayRound(self):
		for match in self.round:
			match.displayMatch()