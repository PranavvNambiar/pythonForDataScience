def loan_emi(amt, years, down_payment):
    print(
        "Downpayment of $300,000 so the loan becomes $1,260,000 - $300,000 =", end=" "
    )
    final_amt = amt - down_payment
    print(final_amt)
    emi = final_amt / (12 * years)
    print(f"The EMI in scenario 1 is {emi}")
    # emi = (amt*rate*(1+r)**n) / (1+r)**n - 1


def loan_emi_2(amt, years):
    emi = amt / (12 * years)
    print(f"The EMI in scenario 2 is {emi}")


def main():
    amt = int(input("What is the total amt of the EMI?\n"))
    # years = int(input("How many years to pay back the loan\n"))
    loan_emi(amt, 8, 3e5)
    loan_emi_2(amt, 10)


if __name__ == "__main__":
    main()
