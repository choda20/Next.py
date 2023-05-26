def check_id_valid(id_number):
    numbers = [int(number) for number in str(id_number)]  # turns the number into a list
    numbers = [number * 2 if (i + 1) % 2 == 0 else number for i, number in enumerate(numbers)]  # allows iteration
    # while keeping the current index, doubles the even indexed numbers
    number_sum = sum([sum([int(digit) for digit in str(number)]) for number in numbers])  # sums numbers above 9,
    # and then sums all numbers together
    return number_sum % 10 == 0


class IDIterator:
    def __init__(self, initial_id):
        self._id = initial_id

    @property
    def id(self):
        return self._id

    def __iter__(self):
        return self

    def __next__(self):
        while self.id < 999999999:
            last_id = self._id
            self._id += 1
            if check_id_valid(last_id):
                return last_id
        raise StopIteration


def id_generator(initial_id):
    current_id = initial_id
    while current_id < 999999999:
        last_id = current_id
        current_id += 1
        if check_id_valid(last_id):
            yield last_id


if __name__ == "__main__":
    user_id = int(input("Enter an ID: "))
    user_choice = input("Generator or Iterator? (gen/it)? ")
    id_maker = "will be assigned to what the user chooses"
    i = 0

    if user_choice == "it":
        id_maker = IDIterator(user_id)
    else:
        id_maker = id_generator(user_id)

    for id_num in id_maker:
        print(id_num)
        i += 1
        if i > 9:
            break
