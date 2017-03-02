import datetime


def save_statistics(func):
	def wraper(self):
		func(self)

		self.print()

	return wraper


class Statistics:
	def __init__(self):
		self.duels_won = 0
		self.duels_lost = 0
		self.arenas_won = 0
		self.arenas_lost = 0

	@save_statistics
	def win_duel(self):
		self.duels_won += 1

	@save_statistics
	def lose_duel(self):
		self.duels_lost += 1

	@save_statistics
	def win_arena(self):
		self.arenas_won += 1

	@save_statistics
	def lose_arena(self):
		self.arenas_lost += 1

	def print(self, file="temp.txt"):
		with open(file, "w") as f:
			print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
			print("Duels won:", self.duels_won, file=f)
			print("Duels lost:", self.duels_lost, file=f)
			print("Duels winrate:", self.get_winrate(self.duels_won, self.duels_lost), "%", file=f)
			print("Arenas won:", self.arenas_won, file=f)
			print("Arenas lost:", self.arenas_lost, file=f)
			print("Arenas winrate:", self.get_winrate(self.arenas_won, self.arenas_lost), "%", file=f)

		with open(file, "r") as f:
			print(f.read())

	@staticmethod
	def get_winrate(wins, loses):
		if wins + loses == 0:
			return 0

		return wins / (wins + loses) * 100
