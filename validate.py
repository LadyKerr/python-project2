def validate_phone_number(phone_number):
    if len(phone_number) == 10:
        return True
    else:
        return False


def validate_email(email):
    if "@" in email:
        return True
    else:
        return False


def validate_name(name):
    if len(name) > 0:
        return True
    else:
        return False


def validate_age(age):
    if age >= 18:
        return True
    else:
        return False
