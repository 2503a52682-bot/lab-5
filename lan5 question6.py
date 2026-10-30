
#Create a simple Python loan approval system using income, age, employment status, credit score, and loan amount. Analyze it for discrimination based on gender, religion, race, or other sensitive attributes, then revise it to make decisions only using relevant financial factors and explain how this improves fairness.

def approve_loan(income, age, employment_status, credit_score, loan_amount):
	"""Return an approval decision and a short, transparent explanation.

	This is an educational rule-based example, not a real lending model.
	"""
	if income <= 0 or loan_amount <= 0:
		return False, "Income and loan amount must be positive."
	if not 18 <= age <= 100:
		return False, "Applicant must be between 18 and 100 years old."
	if not 300 <= credit_score <= 850:
		return False, "Credit score must be between 300 and 850."

	stable_employment = employment_status.lower() in {
		"employed",
		"self-employed",
		"retired",
	}
	debt_to_income_proxy = loan_amount / income

	# All decision factors are stated, measurable, and related to repayment.
	approved = (
		credit_score >= 650
		and stable_employment
		and debt_to_income_proxy <= 3.0
		and (age >= 18)
	)

	if approved:
		return True, "Approved: credit, employment, and requested amount meet the rules."
	return False, "Declined: the financial eligibility rules were not met."


if __name__ == "__main__":
	applicants = [
		(60000,  thirty := 30, "employed", 720, 120000),
		(35000, 45, "unemployed", 680, 150000),
	]

	for applicant in applicants:
		decision, explanation = approve_loan(*applicant)
		print(f"{decision}: {explanation}")

	print(
		"Fairness note: removing gender, religion, race, and other sensitive "
		"attributes prevents direct discrimination and makes decisions based "
		"on consistent, relevant financial criteria. Results should still be "
		"audited for disparate impact and reviewed for legal compliance."
	)

