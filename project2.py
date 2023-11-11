#make different fucntions that do payment history, amount of funds owed, length of credit history,
# and annual income. see if they should be granted a loan

def calcPaymentHistoryPoints(paymentFactor):
# The function returns 100 when the paymentFactor value is yes, otherwise 0
    if (paymentFactor == "yes" or paymentFactor == "Yes"):
        return 100
    else:
        return 0
def calcFundsOwedPoints(fundsFactor):
# Depending on the fundsFactor, the function returns:  0, 30, 80, or 100
    if (fundsFactor >= 5000):
        return 0
    elif (fundsFactor >= 1000 and fundsFactor <= 4999):
        return 30
    elif (fundsFactor >= 1 and fundsFactor <= 999):
        return 80
    else:
        return 100
def calcCreditHistoryPoints(creditFactor):
# Depending on the length of the creditFactor in months, the function returns 0, 80, or 100
    if (creditFactor >= 48):
        return 100
    elif (creditFactor >= 12 and creditFactor <= 47):
        return 80
    else:
        return 0
def calcNumRejectedPoints(rejectedFactor):
# Depending on the number of previously rejected loan applications (rejectedFactor), the function returns 0, 50, or 100.
    if (rejectedFactor >= 5):
        return 0
    elif (rejectedFactor >= 1 and rejectedFactor <= 4):
        return 50
    else:
        return 100
def calcAnnualIncomePoints (incomeFactor):
# Depending on the annual incomeFactor, the function returns 0, 50, or 100
    if(incomeFactor >= 10000):
        return 100
    elif (incomeFactor >= 5000 and incomeFactor <= 9999):
        return 50
    else:
        return 0
def makeDecision(payment, funds, credit, rejected, income):
# use the makeDecision parameters to call calculate the points
# of each factor
    pointsHistory = calcPaymentHistoryPoints(payment)
    pointsFunds = calcFundsOwedPoints(funds)
    pointsCredit = calcCreditHistoryPoints(credit)
    pointsRejected = calcNumRejectedPoints(rejected)
    pointsIncome = calcAnnualIncomePoints(income)
# Use the calculated points to compute the application score
    totalScore = pointsHistory*(.2) + pointsFunds*(.2) + pointsCredit*(.2) + pointsRejected*(.2) + pointsIncome*(.2)
# Use decision structure to determine the final decision
    if totalScore >= 50:
        return totalScore, "ACCEPTED"
    else:
        return totalScore, "REJECTED"
def main():
# Read the number of applications (n) from the user
    app = eval(input("Enter the number of applications: "))
# Loop n times
    for i in range(app):
  # For each iteration
  # Read the factors from the user
        payment = input("Enter payment history: ")
        funds = eval(input("Enter amount of funds owed: "))
        credit = eval(input("Enter the length of credit history: "))
        rejected = eval(input("Enter the number of loan applications rejected: "))
        income = eval(input("Enter the annual Income: "))
  # Call makeDecision to get the loan application score and
  # final decision
  # print the decision
        print("Decision: ", makeDecision(payment, funds, credit, rejected, income))
main()
