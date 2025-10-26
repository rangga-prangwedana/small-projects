import string
from secrets import choice

def password_gen(length:int):
    """
    Returns generated password based on passed length variable.
    """
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    number = string.digits
    symbols = "!@#$%^&*()_+-=[]{},.<>/?"

    all_chars = uppercase + lowercase + number + symbols

    password = "".join(choice(all_chars) for _ in range(length))

    return password


def check_length(length: int, min_value:int, max_value:int):
    """
    Check length if is in the range of min_value and max_value.
    """
    if not (min_value <= length <= max_value):
        raise ValueError(f"Number must be between {min_value} and {max_value}, inclusive.")
    return length


MIN_VALUE = 8
MAX_VALUE = 24

def main():
    while True:
        number = int(input(f"Input the length of the desired password ({MIN_VALUE}-{MAX_VALUE}): "))
        try:
            length = check_length(number, MIN_VALUE, MAX_VALUE)
            break
        except ValueError as e:
            print(f"Error: {e}")

    
    print(f"Generated password: {password_gen(length)}")




if __name__ == "__main__":
    main()
