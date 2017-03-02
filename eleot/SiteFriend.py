import requests
import time


class SiteFriend:
	headers = {
		"Host": "elem.mobi",
		"Connection": "keep-alive",
		"Cache-Control": "max-age=0",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Referer": "http://elem.mobi/dungeon/",
		"Accept-Encoding": "gzip, deflate, sdch",
		"Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"
	}

	def __init__(self):
		self.session = requests.Session()

	def elem_login(self, login, password):
		print("Logged in with", login)
		self.session.post('http://elem.mobi/', data={"plogin": login, "ppass": password}, headers=self.headers)

	def get(self, url, deep=0):
		print("Trying to visit", url, "(", deep, "times )")

		time.sleep(0.2)

		result = self.session.get(url, headers=self.headers)

		if "Вы кликаете слишком часто. Одумайтесь." in result.text and deep < 5:
			time.sleep(1 + deep)

			return self.get(url, deep + 1)

		return result
