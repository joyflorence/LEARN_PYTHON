client_name = input('Enter Client name:')
loan = float(input('Enter amount of loan: '))
days = int(input('Enter days taken with the loan: '))

def calculateloan():
    interest = 0.1
    fine = 0.01
    loan_duration = 30

    if days <= loan_duration:
        amount = loan * (1 + interest)
    else:
        interest_amount = loan * interest
        late_days = days - loan_duration
        late_amount = loan * late_days * fine
        amount = loan + interest_amount + late_amount
    
    return amount

total = calculateloan()
print('Total amount from John is:',total)

       

