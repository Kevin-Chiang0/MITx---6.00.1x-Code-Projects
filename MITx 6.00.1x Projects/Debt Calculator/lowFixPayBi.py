def monthlyUnpaidBalance(balance, minPayment):
    return balance - minPayment

def updatedBalance(unpaidBalance, monthlyInterestRate):
    return unpaidBalance + (monthlyInterestRate * unpaidBalance)

def payPerMonth(balance, monthlyInterestRate, lowBound, highBound, iterCheck):
    iterCheck += 1
    minPayment = (lowBound + highBound)/2
    tempBal = balance
    for x in range(12):
        tempUnpaidBal = monthlyUnpaidBalance(tempBal, minPayment)
        tempBal = updatedBalance(tempUnpaidBal, monthlyInterestRate)
    if abs(tempBal) < .05:
        print(iterCheck)
        return print("Lowest Payment:", round(minPayment,2))
    elif tempBal < 0:
        return payPerMonth(balance, monthlyInterestRate, lowBound, minPayment, iterCheck)
    elif tempBal > 0:
        return payPerMonth(balance, monthlyInterestRate, minPayment, highBound, iterCheck)

##Determines the minimum fixed payment for a balance with interest in a year using bisection search
balance =  10
annualInterestRate = .2
monthlyInterestRate = annualInterestRate/12
lowBound = balance/12
highBound = (balance*(1+ monthlyInterestRate)**12)/12
iterCheck = 0            

payPerMonth(balance, monthlyInterestRate, lowBound, highBound, iterCheck)