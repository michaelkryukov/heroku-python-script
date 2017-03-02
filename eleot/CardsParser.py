from Parser import Parser


class CardsParser(Parser):
	def __init__(self):
		super(CardsParser, self).__init__()

		self.eat_data = False

		self.turn = True

	def feed(self, data):
		self.clear()

		super(CardsParser, self).feed(data)

	def clear(self):
		self.my_cards.clear()
		self.enemy_cards.clear()
		self.cards_urls.clear()
		self.cards_power.clear()

		self.eat_data = False
		self.turn = True

	def handle_starttag(self, tag, attrs):
		if tag == "span":  # find cards' powers
			for attr in attrs:
				if attr == ("class", "stat"):
					self.eat_data = True
					return
		elif tag == "div":  # find cards' multiplier
			for attr in attrs:
				if attr[0] == "class" and attr[1][0:9] == "small mb5":
					self.eat_data = True
					return
		elif tag == "a" and not self.turn:  # find links to hit with
			for attr in attrs:
				if attr == ("class", "card"):
					for attr2 in attrs:
						if attr2[0] == "href":
							self.cards_urls.append("http://elem.mobi" + attr2[1])
							return

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		if self.eat_data:
			if data[0:2] == " x":
				self.cards_power.append(float(data[2:]))
			else:
				self.cards[self.turn].append(int(data))

				self.turn = not self.turn

		self.eat_data = False
