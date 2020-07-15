import math
import argparse


# use arguments() for command line execution
def arguments():
    parser = argparse.ArgumentParser(description='Credit Calculator')
    parser.add_argument("--type")
    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")

    args = parser.parse_args()
    type = args.type
    payment = args.payment
    principal = args.principal
    periods = args.periods
    interest = args.interest

    value_list = [type, payment, principal, periods, interest]
    none_count = value_list.count(None)
    negative_count = value_list.count('-')
    percent_count = value_list.count('%')

    if percent_count != 0:
        print("Incorrect parameters")
    elif negative_count != 0:
        print("Incorrect parameters")
    elif none_count > 1:
        print("Incorrect parameters")
    else:
        if type == 'annuity':
            if payment is None:
                annuity_payment(float(principal), float(periods), float(interest))
            elif periods is None:
                month_count(float(principal), float(payment), float(interest))
            elif principal is None:
                credit_principal(float(payment), float(periods), float(interest))
        elif type == 'diff':
            if payment is None:
                differentiate_payment(float(principal), float(periods), float(interest))
            else:
                print("Incorrect parameters")
        else:
            print("Incorrect parameters")


# use credit_calculator for console execution
def credit_calculator():
    operation = input("""What do you want to calculate? 
    type "n" - for count of months,
    type "a" - for annuity monthly payment, 
    type "d" - for differentiate monthly payment 
    type "p" - for credit principal: """)
    if operation == 'n':
        input_principal = float(input("Enter credit principal: "))
        input_monthly_payment = float(input("Enter monthly payment: "))
        input_interest = float(input("Enter credit interest: "))
        month_count(input_principal, input_monthly_payment, input_interest)
    elif operation == 'a':
        input_principal = float(input("Enter credit principal: "))
        input_period_count = float(input("Enter count of periods: "))
        input_interest = float(input("Enter credit interest: "))
        annuity_payment(input_principal, input_period_count, input_interest)
    elif operation == 'p':
        input_monthly_payment = float(input("Enter monthly payment: "))
        input_period_count = float(input("Enter count of periods: "))
        input_interest = float(input("Enter credit interest: "))
        credit_principal(input_monthly_payment, input_period_count, input_interest)
    elif operation == 'd':
        input_principal = float(input("Enter credit principal: "))
        input_period_count = float(input("Enter count of periods: "))
        input_interest = float(input("Enter credit interest: "))
        differentiate_payment(input_principal, input_period_count, input_interest)


# calculation of amount of periods
def month_count(principal, monthly_payment, interest):
    nominal_interest = interest / (12 * 100)
    period_count = math.log(monthly_payment / (monthly_payment - nominal_interest * principal), nominal_interest + 1)
    period_count = math.ceil(period_count)
    years = math.floor(period_count / 12)
    months = math.ceil(period_count % 12)
    overpayment = monthly_payment * period_count - principal
    if months == 12:
        months = 0
        years += 1

    if years == 1:
        if months == 1:
            print("You need 1 year and 1 month to repay this credit!")
        elif months == 0:
            print("You need 1 year to repay this credit!")
        else:
            print("You need 1 year and {} months to repay this credit!".format(months))
    elif years == 0:
        if months == 1:
            print("You need 1 month to repay this credit!")
        elif months == 0:
            print("You need no time to repay this credit!")
        else:
            print("You need {} months to repay this credit!".format(months))
    else:
        if months == 1:
            print("You need {} years and 1 month to repay this credit!".format(years))
        elif months == 0:
            print("You need {} years to repay this credit!".format(years))
        else:
            print("You need {} years and {} months to repay this credit!".format(years, months))
    print("Overpayment = {}".format(overpayment))


# calculation of monthly annuity payment
def annuity_payment(principal, period_count, interest):
    nominal_interest = interest / (12 * 100)
    payment = principal \
              * (nominal_interest * math.pow(1 + nominal_interest, period_count)) \
              / (math.pow(1 + nominal_interest, period_count) - 1)
    payment = math.ceil(payment)
    overpayment = payment * period_count - principal
    print("Your annuity payment = {}!".format(payment))
    print("Overpayment = {}".format(overpayment))


# calculation of credit principal
def credit_principal(monthly_payment, period_count, interest):
    nominal_interest = interest / (12 * 100)
    principal = monthly_payment \
                / ((nominal_interest * math.pow(1 + nominal_interest, period_count)) \
                / (math.pow(1 + nominal_interest, period_count) - 1))
    principal = math.floor(principal)
    overpayment = monthly_payment * period_count - principal
    print("Your credit principal = {}!".format(principal))
    print("Overpayment = {}".format(overpayment))


# calculation of monthly differentiate payment
def differentiate_payment(principal, period_count, interest):
    nominal_interest = interest / (12 * 100)
    total_payout = 0
    for n in range(1, int(period_count) + 1):
        payment = principal / period_count + nominal_interest \
                  * (principal - principal * (n - 1) / period_count)
        total_payout += math.ceil(payment)
        print("Month {}: paid out {}".format(n, math.ceil(payment)))
    overpayment = total_payout - principal
    print()
    print("Overpayment = {}".format(int(overpayment)))


arguments()

