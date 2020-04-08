# coding: utf8
import requests
import p2p.help_lib as help_lib
from p2p import p2p_values


class Viainvest(p2p_values.P2pValues):
    base_url = 'https://viainvest.com/'

    def __init__(self, mail, pw):
        self.s = requests.Session()
        self.s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
        url = self.base_url
        verTokenMatch = 'name="data[_Token][key]" value="'

        r = self.s.get(url)
        init = r.text
        start = init.find(verTokenMatch) + len(verTokenMatch)
        verToken = init[start: init.find('"', start)]

        dataTokenFieldsMatch = 'name="data[_Token][fields]" value="'
        start = init.find(dataTokenFieldsMatch) + len(dataTokenFieldsMatch)
        dataTokenFields = init[start: init.find('"', start)]

        data = {
            '_method': ' POST',
            'data[_Token][key]': verToken,
            'data[User][email]': mail,
            'data[User][passwd]': pw,
            'data[_Token][fields]': dataTokenFields,
            'data[User][is_remember]': {"data[User][is_remember]": ["0", "1"]},
            'data[_Token][unlocked]': 'Attachment.filename%7CCdata.Project.post%7CCity.id%7CCity.name%7CCity.name%7CEquity%7CForm%7CLend%7CPledge%7CProject.Publish%7CProject.Update%7CProject.address%7CProject.back%7CProject.country_id%7CProject.draft%7CProject.gateway_method_id%7CProject.id%7CProject.is_agree_terms_conditions%7CProject.latitude%7CProject.longitude%7CProject.next%7CProject.normal%7CProject.payment_gateway_id%7CProject.payment_id%7CProject.post%7CProject.project_type%7CProject.project_type_id%7CProject.project_type_slug%7CProject.publish%7CProject.step%7CProject.sudopay_gateway_id%7CProject.type%7CProject.user_id%7CProject.wallet%7CProjectReward%7CState.id%7CState.id%7CState.name%7CSudopay%7C_wysihtml5_mode%7Cs3_file_url',
        }

        url = self.base_url + 'users/login'
        r = self.s.post(url, data=data)

        if ('dashboard' in r.url):
            help_lib.printInfo('Logged in')
            self.update()
        else:
            help_lib.printError(r.text)



    def update(self):
        r = self.s.get(self.base_url + 'users/dashboard')
        find = 'Available funds:</strong></td>\n                  <td><strong>'
        start = r.text.find(find) + len(find)
        self.AvailableFunds = float(r.text[start: r.text.find('€', start)])
        find = 'TOTAL:</strong></td>\n				<td><strong>'
        start = r.text.find(find) + len(find)
        self.CurrentValue = float(r.text[start: r.text.find('€', start)])

    # Total Account Balance
    def TotalAmount(self):
        r = self.s.get('https://www.mintos.com/en/overview/')
        start = r.text.find(u'<td>Total</td><td>€ ') + len(u'<td>Total</td><td>€ ')
        return float(r.text[start: r.text.find('</td>', start)])

    # Available Funds
    def AvailableFunds(self):
        r = self.s.get('https://www.mintos.com/en/overview/')
        start = r.text.find(u'<td>Available Funds</td><td>€ ') + len(u'<td>Available Funds</td><td>€ ')
        return float(r.text[start: r.text.find('</td>', start)])

    # Invested Funds
    def InvestedFunds(self):
        r = self.s.get('https://www.mintos.com/en/overview/')
        start = r.text.find(u'<td>Invested Funds</td><td>€ ') + len(u'<td>Invested Funds</td><td>€ ')
        return float(r.text[start: r.text.find('</td>', start)])

    def NetAnnualReturn(self):
        r = self.s.get('https://www.mintos.com/en/overview/')
        start = r.text.find(u'</i></h2><div class="value">') + len(u'</i></h2><div class="value">')
        # print(start, r.text.find('%\n\t\t\t\t\t\t\t\t</div>', start))
        return float(r.text[start: r.text.find('%\n\t\t\t\t\t\t\t\t</div>', start)])
