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
		for player in plist:
			gamePt = player.getGamePt()
			gamePerc = player.getGamePerc()
			matchPt = player.getMatchPt()
			matchPerc = player.getMatchPerc()
		plist.sort(key=lambda x: (x.getMatchPt(), x.getOppMatchPerc(), x.getGamePerc(), x.getOppGamePerc()), reverse=True)
		matchList = []
		matchList = self.match(plist, matchList)
		for match in matchList:
			player1 = match[0]
			player2 = match[1]
			player1.setMatches()
			player1.addOppList(player2)
			match = Match(player1, player2)
			if (player2 == "bye"):
				match.setPlayer1Score(2)
				match.getWinner()
				self.addMatch(match)
				break
			player2.setMatches()
			player2.addOppList(player1)
			self.addMatch(match)
		self.displayRound(tournament)
			
	def match(self, plist, matchList):
		player1 = plist[0]
		player2 = ""
		if (len(plist) == 1):
			player1 = plist.pop(0)
			player2 = "bye"
			matchList.append((player1, player2))
			return matchList
		for i in range(1, len(plist)):
			if (plist[i] not in player1.getOppList()):
				plistTemp = list(plist)
				player2 = plistTemp.pop(i)
				player1 = plistTemp.pop(0)
				matchList.append((player1, player2))
				currentLen = len(matchList)
				if (len(plistTemp) == 0):
					return matchList
				else:
					matchList2 = self.match(plistTemp, matchList)
					if (len(matchList2) == currentLen):
						matchList = matchList2[:-1]
					else:
						matchList = matchList2
						break
		return matchList
			
	def displayRound(self, tournament):
		count = 1
		for match in self.round:
			match.displayMatches(tournament, count)
			count += 1
			
	def displayRounds(self, maxPlayerLen):
		for match in self.round:
			match.displayMatchHistory(maxPlayerLen)