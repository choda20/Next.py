def raise_stop_iteration():  # 3.1.3
    iterator = iter([1, 2, 3])
    while True:
        iterator = next(iterator)


def raise_zero_division():  # 3.1.3
    print(str(8 / 0))


def raise_assertion_error():  # 3.1.3
    x = 5
    y = 10
    assert x > y


def raise_import_error():  # 3.1.3
    import sigitIsCool


def raise_key_error():  # 3.1.3
    my_dict = {}
    print(my_dict["Sigit"])


def raise_syntax_error():  # 3.1.3
    # eval("print("Hello, World!")")
    pass


def raise_indentation_error():  # 3.1.3
    print("OOPS")
    # print("error")


def raise_type_error():  # 3.1.3
    x = "10"
    y = 5
    result = x + y


def ex313():  # 3.1.3
    raise_stop_iteration()
    raise_indentation_error()
    raise_syntax_error()
    raise_assertion_error()
    raise_import_error()
    raise_key_error()
    raise_zero_division()
    raise_type_error()


def read_file(file_name):  # 3.2.5
    print("__CONTENT_START__")
    try:
        file = open(file_name, "r")
    except:
        print("__NO_SUCH_FILE__")
    else:
        for line in file.readlines():
            print(line.replace("\n", ""))
    finally:
        print("__CONTENT_END__\n")


class UnderAgeException(Exception):  # 3.3.2
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        years_until_18 = str(18 - self._arg)
        return "Provided age " + str(self._arg) + " is below 18, and should not be invited. the person can be " \
                                                  "invited in " + years_until_18 + " years."

    @property
    def arg(self):
        return self._arg


def send_invitation(name, age):  # 3.3.2
    try:
        if int(age) < 18:
            raise UnderAgeException(age)
        print("You should send an invite to " + name)
    except UnderAgeException as e:
        print(e.__str__())


if __name__ == "__main__":
    read_file("test_file.txt")  # 3.2.5, prints contents since file exists
    read_file("my_file.txt")  # 3.2.5, throws an error
    send_invitation("Itay", 17)  # 3.3.2 throws an error
    send_invitation("Ori", 20)  # 3.3.2 works fine since 20>18
