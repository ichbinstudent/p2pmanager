from p2p import bondora, mintos, viainvest
import configparser

config = configparser.ConfigParser()


def setup():
    print("======================================")
    print("\t\tCONFIG")
    print("1) Bondora")
    print("2) Mintos")
    print("Please select one")
    choice = int(input())
    if (choice == 1):
        config.add_section('BONDORA')
        print("Input mail ")
        config.set('BONDORA', 'MAIL', input())
        print("Input password ")
        config.set('BONDORA', 'PW', input())
    if (choice == 2):
        config.add_section('MINTOS')
        print("Input mail ")
        config.set('MINTOS', 'MAIL', input())
        print("Input password ")
        config.set('MINTOS', 'PW', input())

    with open('conf.ini', 'w') as configfile:  # save
        config.write(configfile)


if (not config.read('conf.ini')):
    setup()
print("Do you want to set up? (y/n)")
choice = input()
if (choice == 'y'):
    setup()

mint = None
bond = None
via = None

'''
if 'MINTOS' in config:
    mintos_mail = config['MINTOS']['MAIL']
    mintos_pw = config['MINTOS']['PW']
    mint = mintos.Mintos(mintos_mail, mintos_pw)
    if mint.s is None:
        mint = None
'''

if 'BONDORA' in config:
    bondora_mail = config['BONDORA']['MAIL']
    bondora_pw = config['BONDORA']['PW']
    bond = bondora.Bondora(bondora_mail, bondora_pw)
    if bond.s is None:
        bond = None

if 'VIAINVEST' in config:
    via = viainvest.Viainvest(config['VIAINVEST']['MAIL'], config['VIAINVEST']['PW'])
    if bond.s is None:
        bond = None

if bond is not None:
    print('===================================================')
    print('\t\t\tBONDORA')
    print('{:<30} {:<8.2f}'.format('Current Value', bond.CurrentValue))
    print('{:<30} {:<8.2f}'.format('Available Funds', bond.AvailableFunds))
    print('{:<30} {:<8.2f}'.format('Lifetime Net Profit', bond.LifetimeNetProfit))
    print('{:<30} {:<8.2f}'.format('Lifetime Portfolio Value', bond.LifetimePortfolioValue))
    print('{:<30} {:<8.2f}%'.format('Net Annual Return', bond.YieldToMaturity))
    print('{:<30} {:<8.2f}%'.format('Overdue Rate', bond.OverdueRate))

if via is not None:
    print('===================================================')
    print('\t\t\tVIAINVEST')
    print('{:<30} {:<8.2f}'.format('Current Value', via.CurrentValue))
    print('{:<30} {:<8.2f}'.format('Available Funds', via.AvailableFunds))
    """
    print('{:<30} {:<8.2f}'.format('Available Funds', bond.AvailableFunds))
    print('{:<30} {:<8.2f}'.format('Lifetime Net Profit', bond.LifetimeNetProfit))
    print('{:<30} {:<8.2f}'.format('Lifetime Portfolio Value', bond.LifetimePortfolioValue))
    print('{:<30} {:<8.2f}%'.format('Net Annual Return', bond.YieldToMaturity))
    print('{:<30} {:<8.2f}%'.format('Overdue Rate', bond.OverdueRate))
    """
