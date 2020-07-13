def credit_calculator():
    credit_principal = int(input("Enter the credit principal:"))
    operation = input("""What do you want to calculate? 
                         type "m" - for count of months, 
                         type "p" - for monthly payment """)
    if operation == 'm':
        month_count(credit_principal, int(input("Enter monthly payment:")))
    elif operation == 'p':
        monthly_payment(credit_principal, int(input("Enter count of months:")))


def month_count(principal, payment):
    count = principal / payment
    if count % 2 == 0:
        print("It takes {} months to repay the credit".format(count))
    else:
        print("It takes {} month to repay the credit".format(count))


def monthly_payment(principal, month):
    payment = principal // month
    last_payment = principal - (month - 1) * payment
    if payment == last_payment:
        print("Your monthly payment = {}".format(payment))
    else:
        payment += 1
        last_payment = principal - (month - 1) * payment
        print("Your monthly payment = {} with last month payment = {}.".format(payment, last_payment))

credit_calculator()