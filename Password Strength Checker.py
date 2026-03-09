import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    return score


def password_feedback(score):
    if score <= 2:
        return "Weak Password"
    elif score <= 4:
        return "Moderate Password"
    else:
        return "Strong Password"


def main():
    password = input("Enter a password to check: ")
    score = check_password_strength(password)
    result = password_feedback(score)

    print(f"Password Score: {score}/6")
    print(f"Strength: {result}")


if __name__ == "__main__":
    main()