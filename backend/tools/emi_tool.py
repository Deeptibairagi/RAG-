from langchain_core.tools import tool


@tool
def calculate_emi(loan_amount: float, annual_interest_rate: float, tenure_years: float) -> dict:

    """
    Calculate monthly EMI,
    total payment and total interest.
    """

    try:

        monthly_rate = (annual_interest_rate / 12 / 100)

        number_of_months = int(tenure_years * 12)

        if number_of_months <= 0:

            return {"error":"Tenure must be greater than zero."}

        if loan_amount <= 0:

            return {"error":"Loan amount must be greater than zero."}

        if annual_interest_rate < 0:

            return {"error":"Interest rate cannot be negative."}

        if monthly_rate == 0:

            emi = (loan_amount / number_of_months)

        else:

            emi = (loan_amount * monthly_rate * ((1 + monthly_rate) ** number_of_months)/ ((1 + monthly_rate) ** number_of_months - 1))

        total_payment = (emi * number_of_months)

        total_interest = (total_payment - loan_amount)

        return {"loan_amount": loan_amount, "annual_interest_rate": annual_interest_rate, "tenure_years": tenure_years, "tenure_months": number_of_months, "monthly_emi":round(emi, 2),"total_payment": round(total_payment, 2), "total_interest": round(total_interest, 2)}

    except Exception as e:

        return {"error": str(e)}