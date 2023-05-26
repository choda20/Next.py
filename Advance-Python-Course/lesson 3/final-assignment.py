import re

password_regex_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).+$'
username_regex_pattern = r'^[A-Za-z0-9_]+$'


class PasswordMissingCharacterException(Exception):  # 3.3.2
    def __init__(self, arg):
        self._arg = arg
        self._missing_type = "Not Found"

        uppercase_regex = r'[A-Z]'
        lowercase_regex = r'[a-z]'
        digit_regex = r'[\d]'
        special_regex = r'[\W_]'
        if not re.findall(uppercase_regex, arg):
            self._missing_type = "Uppercase"
        elif not re.findall(lowercase_regex, arg):
            self._missing_type = "Lowercase"
        elif not re.findall(digit_regex, arg):
            self._missing_type = "Digit"
        elif not re.findall(special_regex, arg):
            self._missing_type = "Special"

    def __str__(self):
        return "The password is missing a character (" + self.missing_type + ")"

    @property
    def arg(self):
        return self._arg

    @property
    def missing_type(self):
        return self._missing_type


class PasswordTooShortException(Exception):  # 3.3.2
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The password is too short"

    @property
    def arg(self):
        return self._arg


class PasswordTooLongException(Exception):  # 3.3.2
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The password is too long"

    @property
    def arg(self):
        return self._arg


class UsernameContainsIllegalCharacterException(Exception):  # 3.3.2
    def __init__(self, arg):
        self._arg = arg
        reverse_username_regex_pattern = r'[^A-Za-z0-9_]'
        self._invalid_index = re.search(reverse_username_regex_pattern, arg).start()

    def __str__(self):
        return "The username contains an illegal character \"" + self.arg[self.invalid_index] \
               + "\" at index: " + str(self.invalid_index)

    @property
    def arg(self):
        return self._arg

    @property
    def invalid_index(self):
        return self._invalid_index


class UsernameTooLongException(Exception):  # 3.3.2
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The username is too long"

    @property
    def arg(self):
        return self._arg


class UsernameTooShortException(Exception):  # 3.3.2
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The username is too short"

    @property
    def arg(self):
        return self._arg


def check_input(username, password):
    valid_username = check_valid_username(username)
    if valid_username:
        valid_password = check_valid_password(password)
        if valid_password:
            print("OK!")


def check_valid_password(password):
    regex_pattern = password_regex_pattern
    valid_characters = re.match(regex_pattern, password)
    valid = False
    try:
        if len(password) < 8:
            raise PasswordTooShortException(password)
        elif len(password) > 40:
            raise PasswordTooLongException(password)
        elif not valid_characters:
            raise PasswordMissingCharacterException(password)
        else:
            valid = True
    except Exception as e:
        print(e.__str__())
    finally:
        return valid


def check_valid_username(username):
    regex_pattern = username_regex_pattern
    valid_characters = re.match(regex_pattern, username)
    valid = False
    try:
        if len(username) < 3:
            raise UsernameTooShortException(username)
        elif len(username) > 16:
            raise UsernameTooLongException(username)
        elif not valid_characters:
            raise UsernameContainsIllegalCharacterException(username)
        else:
            valid = True
    except Exception as e:
        print(e.__str__())
    finally:
        return valid


def first_check():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


def second_check():
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")


if __name__ == "__main__":
    first_check()
    print()
    second_check()


