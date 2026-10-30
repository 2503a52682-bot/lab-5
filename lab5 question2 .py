
#Create a simple Python scholarship eligibility checker based on a student's academic score, family income, and location. Then analyze the code to identify whether the eligibility rules unfairly favor or disadvantage any particular group. Provide the code, brief observations about fairness, and suggest 2–3 improvements to make the scholarship decision more equitable and unbiased.``

def check_eligibility(academic_score, family_income, location):
	"""Return eligibility and the reasons used in the decision.

	Rules:
	- Academic score must be at least 75.
	- Annual family income must not exceed 500,000.
	- Students in rural areas receive a 5-point location adjustment.
	"""
	location = location.strip().lower()
	location_adjustment = 5 if location == "rural" else 0
	adjusted_score = academic_score + location_adjustment

	eligible = adjusted_score >= 75 and family_income <= 500000
	reasons = [
		f"adjusted academic score: {adjusted_score}/100",
		f"family income: {family_income}",
		f"location: {location}",
	]
	return eligible, reasons


if __name__ == "__main__":
	try:
		score = float(input("Academic score (0-100): "))
		income = float(input("Annual family income: "))
		location = input("Location (urban/rural): ")

		if not 0 <= score <= 100 or income < 0:
			raise ValueError("Enter a valid score and non-negative income.")

		eligible, reasons = check_eligibility(score, income, location)
		print("Eligible" if eligible else "Not eligible")
		print("; ".join(reasons))
	except ValueError as error:
		print(f"Invalid input: {error}")


