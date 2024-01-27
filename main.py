##################################################
'''
Task: 
'''

def bank():
    current_balance = 1000
    for year in range(1, 26, 1):
        interest_rate = 6.5/100
        interest = round(current_balance * interest_rate, 0)
        deposit = 100
        new_balance = round(current_balance + interest + deposit, 0)

        print(f'{year}: current_balance: {current_balance}, interest: {interest}, deposit: {deposit}, new balance: {new_balance}')

        current_balance = new_balance

bank()

##################################################
