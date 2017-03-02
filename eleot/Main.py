import time

from Player import Player

players = []

with open("data.txt") as f:
	line = f.readline().strip().split(":")

	login = line[0]
	password = line[1]

	players.append(Player(login, password))

while True:
	try:
		for player in players:
			player.do_duels()
			player.do_dungeon()
			player.do_arena()
	except Exception as e:
		print(e.message)
		print("Ignoring it...")

	time.sleep(5)
