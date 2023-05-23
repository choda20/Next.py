import functools


def double_letter(my_str):  # 1.1.2
    return ''.join([char * 2 for char in my_str])


def four_dividers(number):  # 1.1.3
    return [num for num in range(1, number + 1) if num % 4 == 0]


def sum_of_digits(number):  # 1.1.4
    return functools.reduce(lambda x, y: x + y, [int(digit) for digit in str(number)])


def intersection(list_1, list_2): # 1.3.1
    return [element1 for element1 in list_1 for element2 in list_2 if element2 == element1]


def is_prime(number): # 1.3.2
    return len([divider for divider in range(2, number) if number % divider == 0]) == 0


def is_funny(string): # 1.3.3
    return len([word for word in string if word == 'h' or word == 'a']) == len(string)


def ex134(): # 1.3.4
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print("".join([chr((ord(word) - ord("a") + 2) % 26 + ord("a")) if word != " " and word != ":" else word for word in
                   password]))


def combine_coins(coin, numbers):
    return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))


if __name__ == '__main__':
    print(double_letter("str"))
    print(four_dividers(9))
    print(sum_of_digits(104))
    print(intersection([1, 2, 3, 4], [8, 3, 1]))
    print(str(is_prime(42)) + ", " + str(is_prime(43)))
    print(is_funny("hahahahahaha"))
    ex134()
    
