def format_phone_number(func):
    def wrapper(phone):
        new_phone = func(phone)
        if len(new_phone) == 10:
            new_phone = '+38' + new_phone
        elif len(new_phone) == 12:
            new_phone = '+' + new_phone
        print (new_phone)
        return new_phone
    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    print (new_phone)
    return new_phone
phone = ("38050)123-32-34")
sanitize_phone_number(phone)
