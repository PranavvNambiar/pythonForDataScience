import math

cost_of_house = 800_000
down_payment = 0.25 * cost_of_house
loan_duration = 12 * 6
interest_rate = 0.07 / 12


def loan_emi(amt, down_payment, loan_duration, interest_rate):
    total_emi = (amt * interest_rate * (1 + interest_rate) ** (loan_duration)) / (
        (1 + interest_rate) ** (loan_duration) - 1
    )
    total_emi = math.ceil(total_emi)
    print(total_emi)
    return total_emi


emi_house = loan_emi(cost_of_house, down_payment, loan_duration, interest_rate)

cost_of_car = 60_000
car_loan_duration = 1 * 12
car_loan_rate = 0.12 / 12

emi_car = loan_emi(
    amt=cost_of_car,
    down_payment=None,
    loan_duration=car_loan_duration,
    interest_rate=car_loan_rate,
)

print("Total Payment is ${}".format(emi_house + emi_car))
