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
		
	def getMatches(self):
		return self.matches
	
	def setMatches(self):
		self.matches += 1
	
	def getMatchW(self):
		return self.matchW
		
	def setMatchW(self):
		self.matchW += 1
		
	def getMatchL(self):
		return self.matchL
	
	def setMatchL(self):
		self.matchL += 1
		
	def getMatchT(self):
		return self.matchT
	
	def setMatchT(self):
		self.matchT += 1
		
	def getMatchPt(self):
		self.matchPt = (3 * self.matchW) + (0 * self.matchL) + (1 * self.matchT)
		return self.matchPt
		
	def getMatchPerc(self):
		self.matchPerc = self.matchPt / (self.matches * 3)
		return self.matchPerc
		
	def getOppMatchPerc(self):
		#TODO
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
		return self.gamePerc
		
	def getOppGamePerc(self):
		#TODO
		return self.oppGamePerc
		
	def getOppList(self):
		#TODO
		return self.oppList
		
	def setOppList(self, opponent):
		self.oppList.append(opponent)
	
	def displayStats(self):
		return ('{0}' + '\t' + '{1}-{2}-{3}' + '\t' + '{4} pts').format(self.name, str(self.matchW), str(self.matchL), str(self.matchT), str(self.matchPt)).expandtabs(10)
