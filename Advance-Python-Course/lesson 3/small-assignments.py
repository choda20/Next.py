def raise_stop_iteration():  # 3.1.3
    iterator = iter([1, 2, 3])
    while True:
        iterator = next(iterator)


def raise_zero_division():  # 3.1.3
    print(str(8/0))


def raise_assertion_error():  # 3.1.3
    x = 5
    y = 10
    assert x>y


def raise_import_error():  # 3.1.3
    import sigitIsCool


def raise_key_error():  # 3.1.3
    my_dict = {}
    print(my_dict["Sigit"])


def raise_syntax_error():  # 3.1.3
    #eval("print("Hello, World!")")
    pass


def raise_indentation_error():  # 3.1.3
    print("OOPS")
        #print("error")


def raise_type_error():  # 3.1.3
    x = "10"
    y = 5
    result = x + y


if __name__ == "__main__":
    pass
