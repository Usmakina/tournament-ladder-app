from Match import Match

class Player:
	def __init__(self, player, name):
		self.player = player		# the player number
		self.name = name			# the player's name
		self.matches = 0			# the number of matches played
		self.matchW = 0				# the number of matches won
		self.matchL = 0				# the number of matches lost
		self.matchT = 0				# the number of matches tied
		self.matchPt = 0			# the number of match points
		self.matchPerc = 0			# the percentage of matches won
		self.oppMatchPerc = 0		# the percentage of opponents' matches won
		self.games = 0				# the number of games played
		self.gameW = 0				# the number of games won
		self.gameL = 0				# the number of games lost
		self.gameT = 0				# the number of games tied
		self.gamePt = 0				# the number of game points
		self.gamePerc = 0			# the percentage of games won
		self.oppGamePerc = 0		# the percentage of opponents' games won
		self.oppList = []			# the list of opponents faced
	
	def getPlayerNo(self):
		return self.player
	
	def getName(self):
		return self.name
	
	def setName(self, name):
		self.name = name
		
	def getNameLength(self):
		return len(self.name)
	
	def getMatches(self):
		return self.matches
	
	def setMatches(self):
		self.matches += 1
	
	def getMatchW(self):
		return self.matchW
		
	def setMatchW(self, matchW):
		self.matchW += matchW
		
	def getMatchL(self):
		return self.matchL
	
	def setMatchL(self, matchL):
		self.matchL += matchL
		
	def getMatchT(self):
		return self.matchT
	
	def setMatchT(self, matchT):
		self.matchT += matchT
		
	def getMatchPt(self):
		self.matchPt = (3 * self.matchW) + (0 * self.matchL) + (1 * self.matchT)
		return self.matchPt
		
	def getMatchPerc(self):
		if (self.matches != 0):
			self.matchPerc = self.matchPt / (self.matches * 3)
		if (self.matchPerc < 0.33):
			self.matchPerc = 0.33
		return self.matchPerc
		
	def getOppMatchPerc(self):
		count = 0
		self.oppMatchPerc = 0
		if (len(self.oppList) != 0):
			for opponent in self.oppList:
				if (opponent != 'bye'):
					self.oppMatchPerc += opponent.getMatchPerc()
					count += 1
		if (count != 0):
			return self.oppMatchPerc / count
		else:
			return self.oppMatchPerc
		
	def getGames(self):
		return self.games
		
	def setGames(self, games):
		self.games += games
		
	def getGameW(self):
		return self.gameW
		
	def setGameW(self, gameW):
		self.gameW += gameW
	
	def getGameL(self):
		return self.gameL
	
	def setGameL(self, gameL):
		self.gameL += gameL
		
	def getGameT(self):
		return self.gameT
		
	def setGameT(self, gameT):
		self.gameT += gameT
		
	def getGamePt(self):
		self.gamePt = (3 * self.gameW) + (0 * self.gameL) + (1 * self.gameT)
		return self.gamePt
		
	def getGamePerc(self):
		if (self.games != 0):
			self.gamePerc = self.gamePt / (self.games * 3)
		if (self.gamePerc < 0.33):
			self.gamePerc = 0.33
		return self.gamePerc
		
	def getOppGamePerc(self):
		count = 0
		self.oppGamePerc = 0
		if (len(self.oppList) != 0):
			for opponent in self.oppList:
				if (opponent != 'bye'):
					self.oppGamePerc += opponent.getGamePerc()
					count += 1
		if (count != 0):
			return self.oppGamePerc / count
		else:
			return self.oppGamePerc
		
	def getOppList(self):
		line = ""
		if (len(self.oppList) != 0):
			for i in range(0, len(self.oppList)):
				if (i == len(self.oppList)-1):
					if (self.oppList[i] == "bye"):
						line += "bye"
					else:
						line += (self.oppList[i]).getName()
				else:
					if (self.oppList[i] == "bye"):
						line += "bye, "
					else:
						line += (self.oppList[i]).getName() + ", "
		else:
			line = "No opponents played"
		return line
		
	def addOppList(self, opponent):
		self.oppList.append(opponent)
	
	def displayStats(self, maxPlayerLen):
		scores = str(self.matchW) + '-' + str(self.matchL) + '-' + str(self.matchT)
		points = str(self.matchPt) + ' pts'
		return ('{:<' + str(maxPlayerLen) + '} ' + '{:<10}{:<12}' + self.getOppList()).format(self.name, scores, points)
