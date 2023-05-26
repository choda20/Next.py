def translate(sentence):  # 4.1.2
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translate_generator = (words[word] for word in sentence.split(" "))
    translated_sentence = ""
    for translated in translate_generator:
        translated_sentence += translated + " "
    return translated_sentence


def is_prime(n):  # 4.1.3
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):  # 4.1.3
    prime_generator = (number for number in range(n, n ** n) if is_prime(number))
    return next(prime_generator)


def parse_ranges(ranges_string):  # 4.2.2
    range_generator = ((int(number_range.split("-")[0]), int(number_range.split("-")[1])) for number_range
                       in ranges_string.split(","))
    number_generator = (number for start, stop in range_generator for number in range(start, stop + 1))
    return number_generator


def get_fibo():  # 4.3.4
    last = 0
    current = 0
    count = 0
    while True:
        if count == 0:
            yield current
            current += 1
            count += 1
        elif count == 1:
            yield current
            yield current
            last = current
            count += 1
        else:
            yield current + last
            current = current + last
            last = current - last


if __name__ == "__main__":
    print(translate("el gato esta en la casa"))  # 4.1.2
    print(first_prime_over(1000000))  # 4.1.3
    print(list(parse_ranges("1-2,4-4,8-10")))  # 4.2.2
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))  # 4.2.2
    fibo = get_fibo()  # 4.3.4
    for i in range(0, 10):
        print(next(fibo))
