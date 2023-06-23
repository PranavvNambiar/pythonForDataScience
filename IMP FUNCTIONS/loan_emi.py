# This is a function to calculate the emi of anything in general.

# This is to import the read_csv file as a module into our function
import sys

sys.path.append("read_csv")
import read_csv

import math
import os


def loan_emi(amount, duration, rate, down_payment=0):
    """
    Calculates the equal monthly installment (EMI) for a loan

    Arguements:
    amount - total amount to be spent(loan + down_payment)
    duration - Duration of the loan (in months)
    rate - Rate of interest (monthly)
    down_payment (optional) - Optional initial payment(deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = (
            loan_amount * rate * ((1 + rate) ** duration) / ((1 + rate) ** duration - 1)
        )
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return float(emi)


def compute_emi(loans):
    for loan in loans:
        loan["emi"] = loan_emi(
            loan["amount"], loan["duration"], loan["rate"] / 12, loan["down_payment"]
        )


loans2 = read_csv.read_csv("./data/loans2.txt")

# ^ These line of code will be used to make the compute_emi function.
# print(loans2)
# for loan in loans2:
#     loan["emi"] = loan_emi(
#         loan["amount"],
#         loan["duration"],
#         loan["rate"] / 12,  # The CSV contains yearly rates
#         loan["down_payment"],
#     )
# print(loans2)

compute_emi(loans2)
# After this function is executed, the new 'emi' column is appended into the loans object
# Now we need to write these changes into a new file


print(loans2)

# This is to write the new emi file into the data directory with the new column called 'emi'
with open("./data/emi2.txt", "w") as f:
    f.write("amount, duration, rate, down_payment, emi\n")
    for loan in loans2:
        f.write(
            "{}, {}, {}, {}, {}\n".format(
                loan["amount"],
                loan["duration"],
                loan["rate"],
                loan["down_payment"],
                loan["emi"],
            )
        )

print(os.listdir("data"))

print("\n" * 2)

with open("./data/emi2.txt", "r") as f:
    print(f.read())


def write_csv(items, path):
    with open(path, "w") as f:
        if len(items) == 0:
            return

        headers = list(items[0].keys())
        f.write(",".join(headers) + "\n")

        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(",".join(values) + "\n")


loans3 = read_csv.read_csv("./data/loans3.txt")
compute_emi(loans3)
write_csv(loans3, "./data/emi3.txt")
with open("./data/emi3.txt", "r") as f:
    print(f.read())

for i in range(1, 4):
    loans = read_csv.read_csv("./data/loans{}.txt".format(i))
    compute_emi(loans)
    write_csv(loans, "./data/emi{}.txt".format(i))
