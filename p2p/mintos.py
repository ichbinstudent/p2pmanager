# coding: utf8
import requests
import p2p.help_lib as help_lib

class Mintos:

	base_url = 'https://www.mintos.com/en/'

	def __init__(self, mail, pw):
		self.s = requests.Session()
		self.s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
		url = self.base_url + 'login'
		verTokenMatch = 'name="_csrf_token" type="hidden" value="'
		
		r = self.s.get(url)
		init = r.text
		start = init.find(verTokenMatch) + len(verTokenMatch)
		verToken = init[start: init.find('">', start)]
		
		data = {
			'_csrf_token':	verToken,
			'_username':	mail,
			'_password':	pw
		}
		
		url = self.base_url + 'login/check'
		r = self.s.post(url, data=data)
		
		if('overview' in r.url):
			help_lib.printInfo('Logged in')
		else:
			help_lib.printError(r.text)

	#Total Account Balance
	def TotalAmount(self):
		r = self.s.get('https://www.mintos.com/en/overview/')
		start = r.text.find(u'<td>Total</td><td>€ ') + len(u'<td>Total</td><td>€ ')
		return float(r.text[start: r.text.find('</td>', start)])

	#Available Funds
	def AvailableFunds(self):
		r = self.s.get('https://www.mintos.com/en/overview/')
		start = r.text.find(u'<td>Available Funds</td><td>€ ') + len(u'<td>Available Funds</td><td>€ ')
		return float(r.text[start: r.text.find('</td>', start)])

	#Invested Funds
	def InvestedFunds(self):
		r = self.s.get('https://www.mintos.com/en/overview/')
		start = r.text.find(u'<td>Invested Funds</td><td>€ ') + len(u'<td>Invested Funds</td><td>€ ')
		return float(r.text[start: r.text.find('</td>', start)])

	def NetAnnualReturn(self):
		r = self.s.get('https://www.mintos.com/en/overview/')
		start = r.text.find(u'</i></h2><div class="value">') + len(u'</i></h2><div class="value">')
		#print(start, r.text.find('%\n\t\t\t\t\t\t\t\t</div>', start))
		return float(r.text[start: r.text.find('%\n\t\t\t\t\t\t\t\t</div>', start)])
