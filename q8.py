#Team name : Py-Pioneers
def sanitize_email(raw_input: str) -> str:
    email = raw_input.strip().lower()
    if email.count('@') == 1:
        return email
    else:
        return "Invalid Email"
