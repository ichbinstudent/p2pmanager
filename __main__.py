from p2p import bondora, mintos
import configparser

config = configparser.ConfigParser()

def setup():
	print("======================================")
	print("\t\tCONFIG")
	print("1) Bondora")
	print("2) Mintos")
	print("Please select one")
	choice = int(input())
	if(choice == 1):
		config.add_section('BONDORA')
		print("Input mail ")
		config.set('BONDORA', 'MAIL', input())
		print("Input password ")
		config.set('BONDORA', 'PW', input())
	if(choice == 2):
		config.add_section('MINTOS')
		print("Input mail ")
		config.set('MINTOS', 'MAIL', input())
		print("Input password ")
		config.set('MINTOS', 'PW', input())
		
	with open('conf.ini', 'w') as configfile:    # save
		config.write(configfile)


if(not config.read('conf.ini')):
	setup()
print("Do you want to set up? (y/n)")
choice = input()
if(choice == 'y'):
	setup()

mint = None
bond = None

if('MINTOS' in config):
	mintos_mail =	config['MINTOS']['MAIL']
	mintos_pw =		config['MINTOS']['PW']
	mint = mintos.Mintos(mintos_mail, mintos_pw)
	if(mint.s == None):
		mint = None
if('BONDORA' in config):
	bondora_mail =	config['BONDORA']['MAIL']
	bondora_pw =	config['BONDORA']['PW']
	bond = bondora.Bondora(bondora_mail, bondora_pw)
	if(bond.s == None):
		bond = None

if(mint and bond):
	print('===================================================')
	print('\t\t\tMINTOS\tBONDORA')
	print('Total Value\t\t'		+ str(mint.TotalAmount()) + '\t' + str(bond.AccountValue()))
	print('Available Funds\t\t'	+ str(mint.AvailableFunds()) + '\t' + str(bond.AvailableFunds()))
	print('Invested Funds\t\t'	+ str(mint.InvestedFunds()) + '\t' + str(bond.InvestedFunds()))
	print('Net Annual Return\t' + str(mint.NetAnnualReturn()) + '%\t' + str(bond.YieldToMaturity()) + '%')
elif(bond):
	print('===================================================')
	print('\t\t\tBONDORA')
	print('Total Value\t\t'		+ str(bond.AccountValue()))
	print('Available Funds\t\t'	+ str(bond.AvailableFunds()))
	print('Invested Funds\t\t'	+ str(bond.InvestedFunds()))
	print('Net Annual Return\t' + str(bond.YieldToMaturity()) + '%')

input()
"""
"""