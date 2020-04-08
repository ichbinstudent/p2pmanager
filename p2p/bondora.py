# coding: utf8
import json

import requests
import p2p.help_lib as help_lib
from . import p2p_values


class Bondora(p2p_values.P2pValues):
    s: requests.Session = None
    base_url = "https://www.bondora.com/en/"

    def __init__(self, mail, pw):
        super().__init__()
        self.s = requests.Session()
        url = self.base_url + "login"
        verTokenMatch = '<input name="__RequestVerificationToken" type="hidden" value="'

        r = self.s.get(url)
        init = r.text
        start = init.find(verTokenMatch) + len(verTokenMatch)
        verToken = init[start: init.find('" />', start)]

        data = {
            '__RequestVerificationToken': verToken,
            'returnUrl': '/de/statistics',
            'TimeZone': '',
            'Email': mail,
            'Password': pw
        }

        url = 'https://www.bondora.com/de/login'
        r = self.s.post(url, data=data)

        if 'statistics' in r.url:
            help_lib.printInfo('Logged in')
        else:
            help_lib.printError('Login Failed')
            self.s = None

        self.update()

    def update(self):
        r = self.s.get(self.base_url + 'dashboard/overviewnumbers/')
        self.CurrentValue = float(r.json()['Stats'][0]['ValueTooltip'][1:-1])
        self.LifetimeNetProfit = float(r.json()['Stats'][1]['ValueTooltip'][1:-1])
        self.YieldToMaturity = 0 if (r.json()['Stats'][2]['Value'][0:-1] == '') else float(r.json()['Stats'][2]['Value'][0:-1])
        self.LifetimePortfolioValue = float(r.json()['Stats'][3]['ValueTooltip'][1:-1])
        self.AvailableFunds = float(r.json()['Stats'][4]['ValueTooltip'][1:-1])

        loanstatusbybalance = str(self.s.get(self.base_url + 'statistics/loanstatusbybalancechartdata/').json()['ChartData'])
        loanstatusbybalance.replace('\\"', '"')

        rows = json.loads(loanstatusbybalance)['rows']
        self.OverdueRate = 100
        self.OverdueValue = None
        total_value = 0
        self.OverdueRate -= float(rows[0]['c'][1]['v'])     # current
        self.OverdueRate -= float(rows[10]['c'][1]['v'])    # paid back

