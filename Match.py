#from Player import Player

class Match:
	def __init__(self, player1, player2):
		self.player1 = player1					#pointer to player1
		self.player2 = player2					#pointer to player2
		self.player1Score = 0					#player1's score
		self.player2Score = 0					#player2's score
		self.winner = ""
		self.played = "no"
	
	def getPlayer1(self):
		return self.player1
		
	def getPlayer2(self):
		return self.player2	
	
	def getPlayer1Score(self):
		return self.player1Score
		
	def setPlayer1Score(self, score):
		self.player1Score = score
		
	def getPlayer2Score(self):
		return self.player2Score
		
	def setPlayer2Score(self, score):
		self.player2Score = score
	
	def getGames(self):
		games = self.getPlayer1Score() + self.getPlayer2Score()
		return games
		
	def getPlayed(self):
		return self.played
		
	def setPlayed(self):
		self.played = "yes"
	
	def resetScores(self):
		winner = self.getWinner()
		if (winner != "Tie"):
			winner[0][0].setMatchW(-2)
			winner[0][0].setGames(-((self.getGames())*2))
			winner[0][0].setGameW(-((winner[0][1])*2))
			winner[0][0].setGameL(-((winner[1][1])*2))
			winner[1][0].setMatchL(-2)
			winner[1][0].setGames(-((self.getGames())*2))
			winner[1][0].setGameW(-((winner[1][1])*2))
			winner[1][0].setGameL(-((winner[0][1])*2))
		else:
			self.player1.setMatchT(-2)
			self.player1.setGameW(-2)
			self.player1.setGameL(-2)
			self.player2.setMatchT(-2)
			self.player2.setGameW(-2)
			self.player2.setGameL(-2)
	
	def getWinner(self):
		if (self.player2 == "bye"):
			self.player1.setMatchW(1)
			self.player1.setGameW(self.player1Score)
		elif (self.player1Score > self.player2Score):
			self.player1.setMatchW(1)
			self.player1.setGames(self.getGames())
			self.player1.setGameW(self.player1Score)
			self.player1.setGameL(self.player2Score)
			self.player2.setMatchL(1)
			self.player2.setGames(self.getGames())
			self.player2.setGameW(self.player2Score)
			self.player2.setGameL(self.player1Score)
			return ((self.player1, self.player1Score), (self.player2, self.player2Score))
		elif (self.player1Score < self.player2Score):
			self.player2.setMatchW(1)
			self.player2.setGames(self.getGames())
			self.player2.setGameW(self.player2Score)
			self.player2.setGameL(self.player1Score)
			self.player1.setMatchL(1)
			self.player1.setGames(self.getGames())
			self.player1.setGameW(self.player1Score)
			self.player1.setGameL(self.player2Score)
			return ((self.player2, self.player2Score), (self.player1, self.player1Score))
		else:
			self.player1.setMatchT(1)
			self.player1.setGames(self.getGames())
			self.player1.setGameW(self.player2Score)
			self.player1.setGameL(self.player1Score)
			self.player2.setMatchT(1)
			self.player2.setGames(self.getGames())
			self.player2.setGameW(self.player1Score)
			self.player2.setGameL(self.player2Score)
			return "Tie"
			
	def displayMatches(self, tournament, count):
		player1Name = self.player1.getName()
		player2Name = "bye"
		if (self.player2 != "bye"):
			player2Name = self.player2.getName()
		maxPlayerLen = tournament.getMaxPlayerLen()
		print(('{:<3}{:<' + str(maxPlayerLen) + '}   vs   {:<' + str(maxPlayerLen) + '}').format(str(count) + ".", player1Name, player2Name))
		
	def displayMatch(self, tournament):
		player1Name = self.player1.getName()
		player2Name = "bye"
		if (self.player2 != "bye"):
			player2Name = self.player2.getName()
		maxPlayerLen = tournament.getMaxPlayerLen()
		print(('{} ({})  vs  ({}) {:<' + str(maxPlayerLen) + '}').format(player1Name, self.player1Score, self.player2Score, player2Name))