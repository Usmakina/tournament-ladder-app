from Round import Round

class Tournament:
	def __init__(self):
		self.tournament = []			#list of rounds
		self.players = []				#list of players
		self.roundNo = 0				#current round
		
	def getPlayers(self):
		return self.players
		
	def getMaxPlayerLen(self):
		max = 1
		for player in self.players:
			nameLength = player.getNameLength()
			if (nameLength > max):
				max = nameLength
		return max
		
	def addPlayer(self, player):
		self.players.append(player)
	
	def addRound(self, round):
		self.tournament.append(round)
		self.roundNo += 1
		
	def getRound(self, option):
		return self.tournament[option-1]
		
	def getRoundNo(self):
		return self.roundNo
	
	def displayRounds(self):
		for i in range(1, len(self.tournament)+1):
			print(str(i) + ". Round " + str(i))
			
	def displayTournament(self):
		count = 1
		for round in range(0, len(self.tournament)):
			print("Round " + count + ":")
			round.displayRound()
			count += 1