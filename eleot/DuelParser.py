from html.parser import HTMLParser


class DuelParser(HTMLParser):
	def __init__(self):
		super(DuelParser, self).__init__()

		self.current_enemy = ""

		self.eat_data = False

	def handle_starttag(self, tag, attrs):
		if tag == "div":  # find cards' powers
			for attr in attrs:
				if attr == ("class", "fttl green mt5"):
					self.eat_data = True
					return

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		if self.eat_data:
			self.current_enemy = data

		self.eat_data = False
