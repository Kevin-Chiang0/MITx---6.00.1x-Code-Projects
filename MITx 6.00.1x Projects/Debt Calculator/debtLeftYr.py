def minMonthlyPayment(balance, monthlyPaymentRate):
    return balance * monthlyPaymentRate

def monthlyUnpaidBalance(balance, minMonthlyPayment):
    return balance - minMonthlyPayment

def updatedBalance(unpaidBalance, monthlyInterestRate):
    return unpaidBalance + (monthlyInterestRate * unpaidBalance)
    

def debt(balance, monthlyInterestRate, monthlyPaymentRate, time = 0):
    if time > 12:
        print("Your final balance is", round(balance,2))
    elif time < 12:
        minPay = minMonthlyPayment(balance, monthlyPaymentRate)
        unpaidBalance = monthlyUnpaidBalance(balance, minPay)
        newBal = updatedBalance(unpaidBalance, monthlyInterestRate)
        print("Month", time + 1,"remaining balance:", round(newBal,2))
        debt(newBal, monthlyInterestRate, monthlyPaymentRate, time+1)

## calculates debt remaining after making minimum payments for a year
balance = 484
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
monthlyPaymentRate = .04

debt(balance, monthlyInterestRate, monthlyPaymentRate)