#Create a simple Python user feedback form. Review the language and options for inclusiveness and accessibility, then revise the code to use inclusive language, accessible features, and avoid assumptions that may exclude users    

def ask(prompt, *, required=False, choices=None):
    """Prompt clearly and allow users to skip optional questions."""
    if choices:
        print(prompt)
        print("Options: " + ", ".join(choices))

    while True:
        answer = input("> ").strip()
        if not answer and not required:
            return "Not provided"
        if required and not answer:
            print("This response is required. You can type 'skip' if you prefer not to answer.")
            continue
        if answer.lower() == "skip":
            return "Prefer not to say"
        if choices and answer.lower() not in {choice.lower() for choice in choices}:
            print("Please choose one of the listed options, or type 'skip'.")
            continue
        return answer


def main():
    print("User feedback form")
    print("Your feedback helps us improve. You may skip any question.")
    print("No demographic information is required, and responses are treated respectfully.\n")

    feedback = ask("What would you like to share?", required=True)
    experience = ask(
        "How was your experience?",
        choices=["Very positive", "Positive", "Neutral", "Negative", "Very negative"],
    )
    accessibility = ask(
        "Did you encounter any accessibility barriers or need any accommodations? "
        "Please describe them in your own words, if you wish."
    )
    contact = ask(
        "Would you like us to contact you about this feedback? "
        "If yes, enter a preferred contact method; otherwise type 'skip'."
    )

    print("\nThank you for sharing your feedback.")
    print("Feedback:", feedback)
    print("Experience:", experience)
    print("Accessibility notes:", accessibility)
    print("Preferred contact method:", contact)


if __name__ == "__main__":
    main()
    
    
