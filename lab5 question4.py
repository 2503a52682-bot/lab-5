#Create a simple Python employee performance evaluation system based on project completion rate, teamwork score, and attendance. Analyze the scoring logic to identify any unfair weighting or hidden bias, and briefly explain whether the evaluation criteria are balanced and justifiable.

def evaluate_employee(project_completion_rate, teamwork_score, attendance_rate):
	"""Calculate a performance score and rating.

	Each argument is a percentage from 0 to 100. The weights are explicit:
	project completion 40%, teamwork 35%, and attendance 25%.
	"""
	values = {
		"project completion rate": project_completion_rate,
		"teamwork score": teamwork_score,
		"attendance rate": attendance_rate,
	}

	if any(not isinstance(value, (int, float)) for value in values.values()):
		raise TypeError("All scores must be numbers.")
	if any(value < 0 or value > 100 for value in values.values()):
		raise ValueError("All scores must be between 0 and 100.")

	score = (
		project_completion_rate * 0.40
		+ teamwork_score * 0.35
		+ attendance_rate * 0.25
	)

	if score >= 90:
		rating = "Excellent"
	elif score >= 75:
		rating = "Good"
	elif score >= 60:
		rating = "Needs Improvement"
	else:
		rating = "Unsatisfactory"
	return round(score, 2), rating


if __name__ == "__main__":
	score, rating = evaluate_employee(88, 92, 95)
	print(f"Performance score: {score}/100")
	print(f"Rating: {rating}")

	print("\nFairness analysis:")
	print(
		"The criteria are transparent and total 100%, but they are not "
		"automatically unbiased. Project completion has the greatest impact; "
		"attendance can disadvantage employees with disabilities, caregiving "
		"responsibilities, or approved leave; and teamwork may be subjective. "
		"The system is balanced only when the weights fit the role, attendance "
		"exceptions are accommodated, teamwork uses documented evidence, and "
		"scores are audited consistently with an employee appeal process."
	)
