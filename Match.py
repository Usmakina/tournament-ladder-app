from Player import Player

class Match:
	def __init__(self, player1, player2):
		self.player1 = player1					#pointer to player1
		self.player2 = player2					#pointer to player2
		self.player1Score = 0					#player1's score
		self.player2Score = 0					#player2's score
	
	def getPlayer1Score(self):
		return self.player1Score
		
	def setPlayer1Score(self, score):
		self.player1Score = score
		
	def getPlayer2Score(self):
		return self.player2Score
		
	def setPlayer2Score(self, score):
		self.player2Score = score
	
	def getWinner(self):
		if (self.player1Score > self.player2Score):
			return self.player1
		elif (self.player1Score < self.player2Score):
			return self.player2
		elif (self.player1Score == self.player2Score):
			return "Tie"
			
	def displayMatch(self):
		player1Name = self.player1.getName()
		player2Name = "bye"
		if (self.player2 != "bye"):
			player2Name = self.player2.getName()
		print(player1Name + " vs " + player2Name)