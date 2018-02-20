from Round import Round

class Tournament:
	def __init__(self):
		self.tournament = []			#list of rounds
		self.roundNo = 0				#current round
		
	def addRound(self, round):
		self.tournament.append(round)
		self.roundNo += 1
		
	def getRound(self):
		return self.roundNo
	
	def displayTournament(self):
		count = 1
		for round in range(0, len(self.tournament)):
			print("Round " + count + ":")
			round.displayRound()
			count += 1