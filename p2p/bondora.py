# coding: utf8
import requests
import p2p.help_lib as help_lib

class Bondora:
	def __init__(self, mail, pw):
		self.s = requests.Session()
		url = "https://www.bondora.com/de/login"
		verTokenMatch = '<input name="__RequestVerificationToken" type="hidden" value="'
		
		r = self.s.get(url)
		init = r.text
		start = init.find(verTokenMatch) + len(verTokenMatch)
		verToken=init[start: init.find('" />',start)]
		
		data = {
			'__RequestVerificationToken': verToken,
			'returnUrl':	'/de/statistics',
			'TimeZone':		'',
			'Email':		mail,
			'Password':		pw
		}
		
		url = 'https://www.bondora.com/de/login'
		r = self.s.post(url, data=data)
		
		if('statistics' in r.url):
			help_lib.printInfo('Logged in')
		else:
			help_lib.printError('Login Failed')
			self.s = None


	#Invested Funds
	def InvestedFunds(self):
		r = self.s.get('https://www.bondora.com/en/statistics/getportfolioprofitability')
		seq = u'∑';
		start = r.text.find(seq) + len(seq)
		start = r.text.find('<td>', start) + len('<td>') + 1
		return float(r.text[start: r.text.find(' ', start)])

	#Account value
	def AccountValue(self):
		r = self.s.get('https://www.bondora.com/en/dashboard/overviewnumbers/')
		return float(r.json()['Stats'][0]['ValueTooltip'][0:-1])

	#Lifetime net profit
	def LifetimeNetProfit(self):
		r = self.s.get('https://www.bondora.com/en/dashboard/overviewnumbers/')
		return float(r.json()['Stats'][1]['ValueTooltip'][0:-1])

	#Yield to maturity
	def YieldToMaturity(self):
		r = self.s.get('https://www.bondora.com/en/dashboard/overviewnumbers/')
		if(r.json()['Stats'][2]['Value'][0:-1] == ''):
			return 0
		return float(r.json()['Stats'][2]['Value'][0:-1])

	#Lifetime portfolio value
	def LifetimePortfolioValue(self):
		r = self.s.get('https://www.bondora.com/en/dashboard/overviewnumbers/')
		return float(r.json()['Stats'][3]['ValueTooltip'][0:-1])

	#Available funds
	def AvailableFunds(self):
		r = self.s.get('https://www.bondora.com/en/dashboard/overviewnumbers/')
		return float(r.json()['Stats'][4]['ValueTooltip'][0:-1])
