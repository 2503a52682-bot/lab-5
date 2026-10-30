#Create a simple Python program that predicts whether a student is selected or rejected for admission based on entrance exam score, academic marks, and other criteria. Check whether the program clearly explains its decision. Identify transparency risks, show an example where no explanation is given, and then revise the program to provide a clear reason and list the important factors influencing the decision.
def opaque_decision(entrance_score, academic_marks, interview_score):
	"""Example of a decision that gives no reason to the student."""
	selected = (entrance_score >= 70 and academic_marks >= 60 and interview_score >= 50)
	return "Selected" if selected else "Rejected"


def transparent_decision(entrance_score, academic_marks, interview_score):
	"""Return the decision, a clear reason, and the important factors."""
	factors = {
		"Entrance exam score": entrance_score,
		"Academic marks": academic_marks,
		"Interview score": interview_score,
	}
	requirements = {
		"Entrance exam score": (entrance_score >= 70, "at least 70"),
		"Academic marks": (academic_marks >= 60, "at least 60"),
		"Interview score": (interview_score >= 50, "at least 50"),
	}
	failed = [
		f"{name} was {factors[name]}, but must be {minimum}"
		for name, (passed, minimum) in requirements.items()
		if not passed
	]

	if failed:
		decision = "Rejected"
		reason = "The applicant did not meet: " + "; ".join(failed) + "."
	else:
		decision = "Selected"
		reason = "The applicant met all minimum requirements."
	return decision, reason, factors


def show_result(name, scores):
	print(f"\n{name}")
	print("Opaque example (no explanation):", opaque_decision(*scores))
	decision, reason, factors = transparent_decision(*scores)
	print("Transparent decision:", decision)
	print("Reason:", reason)
	print("Important factors:")
	for factor, value in factors.items():
		print(f"  - {factor}: {value}")


if __name__ == "__main__":
	show_result("Example applicant", (72, 58, 80))
	print("\nTransparency risks in the opaque version:")
	print("- The applicant cannot tell which criterion caused rejection.")
	print("- Hidden thresholds make errors or unfair decisions difficult to challenge.")
	print("- Important factors are not recorded for review.")
