
def monthlyUnpaidBalance(balance, minPayment):
    return balance - minPayment

def updatedBalance(unpaidBalance, monthlyInterestRate):
    return unpaidBalance + (monthlyInterestRate * unpaidBalance)

def payPerMonth(balance, monthlyInterestRate, minPayment):
    tempBal = balance
    for x in range(12):
        tempUnpaidBal = monthlyUnpaidBalance(tempBal, minPayment)
        tempBal = updatedBalance(tempUnpaidBal, monthlyInterestRate)
    if tempBal > 0:
        return payPerMonth(balance, monthlyInterestRate, minPayment + 10)
    elif tempBal <= 0:
        return print("Lowest Payment:", minPayment)

##Determines the minimum fixed payment for a balance with interest in a year using incremental search
balance =  3926
annualInterestRate = .2
monthlyInterestRate = annualInterestRate/12
minPayment = 10            

payPerMonth(balance, monthlyInterestRate, minPayment)