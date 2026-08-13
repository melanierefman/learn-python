print("=== LOAN ELIGIBILITY CHECKER ===")

# system params
THRESHOLD = {
    "min_monthly_income": 5_000_000,
    "max_loan_amount": 50_000_000,
    "min_tenor": 6,
    "max_tenor": 36,
    "eligible_employment": "permanent"
}

# TODO:
# wrap dengan error handling

name = input("Customer Name: ")

# TODO:
# input monthly income
def get_monthly_income():
    while True:
        monthly_income = int(input("Monthly Income: "))

        if monthly_income < 0:
            print("Monthly income cannot be negative.")
        else:
            print(f"Monthly income is: {monthly_income}")
            return monthly_income

# TODO:
# input loan amount
def get_loan_amount():
    while True:
        loan_amount = int(input("Loan Amount: "))

        if loan_amount < 0:
            print("Loan amount cannot be negative.")
        else:
            print(f"Loan amount is: {loan_amount}")
            return loan_amount


# TODO:
# input tenor

# TODO:
# input employment status

# TODO:
# hitung cicilan

# TODO:
# tentukan apakah customer eligible

# TODO:
# tampilkan hasil
# tampilkan semua alasan penolakan 