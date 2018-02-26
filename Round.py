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
		plist.sort(key=lambda x: x.getGamePt(), reverse=True)
		plist.sort(key=lambda x: x.getGamePerc(), reverse=True)
		plist.sort(key=lambda x: x.getMatchPt(), reverse=True)
		plist.sort(key=lambda x: x.getMatchPerc(), reverse=True)
		plist.sort(key=lambda x: (x.getMatchPt(), x.getOppMatchPerc(), x.getGamePerc(), x.getOppGamePerc()), reverse=True)
		for i in range(0, len(plist)):
			player1 = plist[i]
			player1.setMatches()
			player2 = ""
			if (i == len(plist)-1):
				player2 = "bye"
			else:
			#	print(player1.getName())
				for j in range(i+1, len(plist)):
					if (plist[j] not in player1.getOppList()):
						player2 = plist.pop(j)
			#			print(player2.getName())
						break
				player2.setMatches()
				player2.addOppList(player1)
			player1.addOppList(player2)
			match = Match(player1, player2)
			if (player2 == "bye"):
				match.setPlayer1Score(2)
				match.getWinner()
				self.addMatch(match)
				break
			self.addMatch(match)
			if (len(plist) == (len(self.playersList) / 2)):
				break
		self.displayRound(tournament)
			
	def displayRound(self, tournament):
		count = 1
		for match in self.round:
			match.displayMatches(tournament, count)
			count += 1
			
