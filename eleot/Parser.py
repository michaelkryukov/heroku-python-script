from html.parser import HTMLParser


class Parser(HTMLParser):
	def __init__(self):
		super(Parser, self).__init__()

		self.my_cards = []
		self.enemy_cards = []

		self.cards = [self.my_cards, self.enemy_cards]
		self.cards_power = []
		self.cards_urls = []
