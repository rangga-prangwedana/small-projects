def password_gen(length:int):
    pass


def check_length(length: int):
    if not (8 <= length <= 24):
        raise ValueError("Number must be between 8 and 24, inclusive.")
    return length


def main():
    number = int(input("Input the length of the desired password (8-24):"))
    try:
        length = check_length(number)
    except ValueError as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    main()
