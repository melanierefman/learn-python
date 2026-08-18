print("=== LOAN ELIGIBILITY CHECKER ===")

# system params
THRESHOLD = {
    "min_monthly_income": 5000000,
    "max_loan_amount": 50000000,
    "min_tenor": 6,
    "max_tenor": 36,
    "eligible_employment": "permanent"
}

# TODO:
# wrap dengan error handling int input
def handle_input_error():
    try:
        value = int(input())
        return value
    except Exception as e:
        print(f"Error: {e}")
        return None

name = input("Customer Name: ")

# TODO:
# input monthly income
def get_monthly_income():
    while True:
        print("Monthly Income: ", end="")
        monthly_income = handle_input_error()

        if monthly_income is None:
            continue

        if monthly_income < 0:
            print("Monthly income cannot be negative.")
        else:
            return monthly_income

# TODO:
# input loan amount
def get_loan_amount():
    while True:
        print("Loan Amount: ", end="")
        loan_amount = handle_input_error()

        if loan_amount is None:
            continue

        if loan_amount < 0:
            print("Loan amount cannot be negative.")
        else:
            return loan_amount


# TODO:
# input tenor
def get_tenor():
    while True:
        print("Tenor (in months): ", end="")
        tenor = handle_input_error()

        if tenor is None:
            continue

        if tenor < 0:
            print("Tenor cannot be negative.")
        else:
            print(f"Tenor is: {tenor} months")
            return tenor

# TODO:
# input employment status
def get_employment_status():
    return input("Employment Status (permanent/contract): ").strip().lower()

# TODO:
# hitung cicilan
def calculate_installment(loan_amount, tenor):
    return loan_amount / tenor

# TODO:
# tentukan apakah customer eligible
def check_eligibility(monthly_income, loan_amount, tenor, employment_status):
    reasons = []

    if monthly_income < THRESHOLD["min_monthly_income"]:
        reasons.append("Monthly income is below the minimum threshold.")

    if loan_amount > THRESHOLD["max_loan_amount"]:
        reasons.append("Loan amount exceeds the maximum limit.")

    if tenor < THRESHOLD["min_tenor"] or tenor > THRESHOLD["max_tenor"]:
        reasons.append("Tenor is outside the allowed range.")

    if employment_status != THRESHOLD["eligible_employment"]:
        reasons.append("Employment status is not eligible.")

    return len(reasons) == 0, reasons

# TODO:
# tampilkan hasil
# tampilkan semua alasan penolakan 
def display_result(is_eligible, reasons):
    if is_eligible:
        print("Eligible for the loan.")
    else:
        print("Not eligible for the loan:")
        for reason in reasons:
            print("-", reason)
            
            
monthly_income = get_monthly_income()
loan_amount = get_loan_amount()
tenor = get_tenor()
employment_status = get_employment_status()

is_eligible, reasons = check_eligibility(
    monthly_income,
    loan_amount,
    tenor,
    employment_status
)

display_result(is_eligible, reasons)
