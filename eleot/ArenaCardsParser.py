from Parser import Parser


class ArenaCardsParser(Parser):
	def __init__(self):
		super(ArenaCardsParser, self).__init__()

		self.turn = True

		self.eat_data = False

		self.data_type = 0  # 0 - stats, 1 - multiplier

		self.change_target_url = ""

	def feed(self, data):
		self.clear()

		super(ArenaCardsParser, self).feed(data)

	def clear(self):
		self.my_cards.clear()
		self.enemy_cards.clear()
		self.cards_urls.clear()
		self.cards_power.clear()

		self.eat_data = False
		self.turn = True

	def handle_starttag(self, tag, attrs):
		if tag == "div":  # find cards' multiplier
			for attr in attrs:
				if attr[0] == "class" and attr[1][0:9] == "small mb5":
					self.eat_data = True
					self.data_type = 1
					return

		if tag == "a":
			for attr in attrs:
				if attr[0] == "class" and attr[1] in ["ml5 btn grey w100px mt5", "btn blue w100px mt5 mr5"]:
					for attr2 in attrs:
						if attr2[0] == "href":
							self.change_target_url = "http://elem.mobi" + attr2[1]
							return

		for attr in attrs:  # find cards' stats and powers
			if attr[0] == "class" and attr[1] == "card":
				if tag == "a":
					for attr2 in attrs:
						if attr2[0] == "href":
							self.cards_urls.append("http://elem.mobi" + attr2[1])
							break

				elif tag == "span":
					self.my_cards.append(0)
					self.enemy_cards.append(0)
					self.cards_power.append(0)
					self.cards_urls.append("")

		if tag == "span":
			for attr in attrs:
				if attr[0] == "class" and attr[1] == "stat":
					self.eat_data = True
					self.data_type = 0
					return

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		if self.eat_data:
			if self.data_type == 1:
				if data.strip():
					self.cards_power.append(float(data[2:]))
			elif self.data_type == 0:
				self.cards[self.turn].append(int(data))

				self.turn = not self.turn

		self.eat_data = False
