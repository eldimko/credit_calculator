import math


def credit_calculator():
    operation = input("""What do you want to calculate? 
    type "n" - for count of months,
    type "a" - for annuity monthly payment, 
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


def month_count(principal, monthly_payment, interest):
    nominal_interest = interest / (12 * 100)
    period_count = math.log(monthly_payment / (monthly_payment - nominal_interest * principal), nominal_interest + 1)
    math.ceil(period_count)
    years = math.floor(period_count / 12)
    months = math.ceil(period_count % 12)
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


def annuity_payment(principal, period_count, interest):
    nominal_interest = interest / (12 * 100)
    payment = principal \
              * (nominal_interest * math.pow(1 + nominal_interest, period_count)) \
              / (math.pow(1 + nominal_interest, period_count) - 1)
    payment = math.ceil(payment)
    print("Your annuity payment = {}!".format(payment))


def credit_principal(monthly_payment, period_count, interest):
    nominal_interest = interest / (12 * 100)
    principal = monthly_payment \
                / ((nominal_interest * math.pow(1 + nominal_interest, period_count)) \
                / (math.pow(1 + nominal_interest, period_count) - 1))
    principal = math.floor(principal)
    print("Your credit principal = {}!".format(principal))


credit_calculator()
