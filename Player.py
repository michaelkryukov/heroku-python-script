import time

from ArenaCardsParser import ArenaCardsParser
from CardsParser import CardsParser
from DuelParser import DuelParser
from DungeonCardsParser import DungeonCardsParser
from SiteFriend import SiteFriend
from Statistics import Statistics

from random import choice


class Player:
	def __init__(self, login, password):
		self.client = SiteFriend()
		self.client.elem_login(login, password)

		self.statistics = Statistics()
		self.cards_parser = CardsParser()
		self.arena_cards_parser = ArenaCardsParser()
		self.dungeon_cards_parser = DungeonCardsParser()
		self.duel_parser = DuelParser()

	def get(self, url):
		return self.client.get(url)

	def do_dungeon(self):
		res = self.get("http://elem.mobi/dungeon/#last")
		lazy_engagind = 7

		print("Let's fight some bosses.")

		while lazy_engagind > 0:
			if "Кампания" in res.text:
				# currently not fighting, time to engage a boss

				res = self.get("http://elem.mobi/dungeon/" + str(lazy_engagind) + "/start/")

				lazy_engagind -= 1

				if lazy_engagind < 0:
					print("All bosses currently dead.")
					return
			else:
				# already fighting

				self.dungeon_cards_parser.feed(res.text)

				differences = [self.get_difference(i, self.dungeon_cards_parser) for i in range(3)]

				chosen_difference = choice(differences)

				hit_link = self.dungeon_cards_parser.cards_urls[chosen_difference[1]]

				print("Hit boss for", chosen_difference[0])

				res = self.get(hit_link)

				if "— Поражение —" in res.text:
					print("Boss won")
					lazy_engagind += 1
				elif "— Победа —" in res.text:
					print("We won")

	def do_arena(self):
		res = self.get("http://elem.mobi/arena/")
		fight = False
		swapped = 0

		maxest_difference = None

		while True:
			if res.url == "http://elem.mobi/arena/":
				# waiting for battle or not fighting
				print("Currently not in fight. Trying to join...")

				self.get("http://elem.mobi/arena/join/")

				res = self.get("http://elem.mobi/arena/")

				time.sleep(2)
			elif len(res.url) > 23 and res.url[:23] == "http://elem.mobi/arena/":
				# battle had started
				arena_id = res.url.split("/arena/")[1].split("/")[0]

				if "Вы пали. Слава героям!" in res.text:
					print("We died. Waiting for game to finish")

					time.sleep(8)

					res = self.get("http://elem.mobi/arena/" + arena_id)

					continue

				if "Ваша команда проиграла" in res.text:
					self.statistics.lose_arena()
					return
				elif "Ваша команда победила" in res.text:
					self.statistics.win_arena()
					return

				if not fight:
					fight = True
					print("Show them what we made of! Arena fight started.")
					print("Arena id:", arena_id)

				self.arena_cards_parser.feed(res.text)

				differences = [self.get_difference(i, self.arena_cards_parser) for i in range(3)]

				if differences.count((-float("inf"), -1)) == 3:
					print("No cards in hand! Waiting")
					time.sleep(1)

					res = self.get("http://elem.mobi/arena/" + arena_id)

					continue

				max_difference = max(differences)

				if max_difference[0] <= 50 and swapped < 3:
					print("Only bad cards in hand. Changing target.")

					if maxest_difference is None or maxest_difference[0][0] < max_difference[0]:
						maxest_difference = [max_difference, 0]

					if self.arena_cards_parser.change_target_url != "":
						res = self.get(self.arena_cards_parser.change_target_url)
						maxest_difference[1] += 1
					else:
						res = self.get("http://elem.mobi/arena/" + arena_id)

					if differences.count((-float("inf"), -1)) == 0:
						swapped += 1

						time.sleep(1.5)

					continue
				elif swapped >= 3:
					print("There are no good cards in hand at all.")

					if maxest_difference is not None:
						for i in range(3 - 3 % maxest_difference[1]):
							self.get(self.arena_cards_parser.change_target_url)

							continue

					swapped = 0
				else:
					swapped = 0

				hit_link = self.arena_cards_parser.cards_urls[max_difference[1]]

				print("Hit enemy for", max_difference[0])

				res = self.get(hit_link)

	def do_duels(self):
		while self.do_duel():
			pass

	def do_duel(self):
		res = self.get("http://elem.mobi/duel/")
		weak_enemies = 0

		while True:
			if res.url == "http://elem.mobi/duel/":
				# no fight right now
				self.duel_parser.feed(res.text)

				if self.duel_parser.current_enemy == "Слабый противник" and weak_enemies < 20:
					weak_enemies += 1

					print("Found weak enemy... (", weak_enemies, " / 20 )")

					res = self.get("http://elem.mobi/duel/")

					continue

				if weak_enemies == 20:
					print("There are no strong enemies! Fight with the weak \_c:_/")
				else:
					print("Found enemy. Fight!")

				res = self.get("http://elem.mobi/duel/tobattle/")

				if res.url == "http://elem.mobi/duel/tobattle/":
					print("There are no availible duels!")
					return False

				continue

			elif len(res.url) > 22 and res.url[:22] == "http://elem.mobi/duel/":
				# fighting now
				self.cards_parser.feed(res.text)

				differences = [self.get_difference(i, self.cards_parser) for i in range(3)]

				max_difference = max(differences)

				hit_link = self.cards_parser.cards_urls[max_difference[1]]

				print("Hit enemy for", max_difference[0])

				res = self.get(hit_link)

				if "— Поражение —" in res.text:
					self.statistics.lose_duel()
					return True
				elif "— Победа —" in res.text:
					self.statistics.win_duel()
					return True

	@staticmethod
	def get_difference(i, parser):
		if len(parser.cards_power) > i and len(parser.my_cards) > i and len(parser.enemy_cards) > i and len(
				parser.cards_urls) > i and parser.cards_urls[i] != "":
			my_power = parser.my_cards[i] * parser.cards_power[i]
			enemy_power = parser.enemy_cards[i] * (2.0 - parser.cards_power[i])

			return (my_power - enemy_power, i)
		else:
			return (-float("inf"), -1)
