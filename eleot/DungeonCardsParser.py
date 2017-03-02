from Parser import Parser


class DungeonCardsParser(Parser):
	def __init__(self):
		super(DungeonCardsParser, self).__init__()

		self.eat_data = False

	def feed(self, data):
		self.clear()

		self.cards_power = [1, 1, 1]
		self.enemy_cards = [0, 0, 0]

		super(DungeonCardsParser, self).feed(data)

	def clear(self):
		self.my_cards.clear()
		self.enemy_cards.clear()
		self.cards_urls.clear()
		self.cards_power.clear()

		self.eat_data = False

	def handle_starttag(self, tag, attrs):
		for attr in attrs:  # find cards' stats and powers
			if attr[0] == "class" and attr[1] == "card":
				if tag == "a":
					for attr2 in attrs:
						if attr2[0] == "href":
							self.cards_urls.append("http://elem.mobi" + attr2[1])
							return

		if tag == "span":
			for attr in attrs:
				if attr[0] == "class" and attr[1] == "stat":
					self.eat_data = True
					return

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		if self.eat_data:
			self.my_cards.append(int(data))

		self.eat_data = False
