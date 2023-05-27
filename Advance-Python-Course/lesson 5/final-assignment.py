def check_id_valid(id_number):
    """
    Checks if the provided ID number is valid.

    Args:
        id_number (int): The ID number to validate.

    Returns:
        bool: True if the ID is valid, False otherwise.
    """
    numbers = [int(number) for number in str(id_number)]
    numbers = [number * 2 if (i + 1) % 2 == 0 else number for i, number in enumerate(numbers)]
    number_sum = sum([sum([int(digit) for digit in str(number)]) for number in numbers])
    return number_sum % 10 == 0


class IDIterator:
    """
    An iterator class for generating valid IDs.

    Attributes:
        id (int): The current ID number.

    Methods:
        __init__(self, initial_id): Initializes the IDIterator object.
        __iter__(self): Returns the iterator object.
        __next__(self): Generates the next valid ID.

    """

    def __init__(self, initial_id):
        """
        Initializes the IDIterator object with the initial ID.

        Args:
            initial_id (int): The starting ID number.

        """
        self._id = initial_id

    @property
    def id(self):
        """
        Property method to access the current ID number.

        Returns:
            int: The current ID number.

        """
        return self._id

    def __iter__(self):
        """
        Returns the iterator object.

        Returns:
            IDIterator: The iterator object.

        """
        return self

    def __next__(self):
        """
        Generates the next valid ID.

        Returns:
            int: The next valid ID.

        Raises:
            StopIteration: If there are no more valid IDs to generate.

        """
        while self.id < 999999999:
            last_id = self._id
            self._id += 1
            if check_id_valid(last_id):
                return last_id
        raise StopIteration


def id_generator(initial_id):
    """
    A generator function for generating valid IDs.

    Args:
        initial_id (int): The starting ID number.

    Yields:
        int: The next valid ID.

    """
    current_id = initial_id
    while current_id < 999999999:
        last_id = current_id
        current_id += 1
        if check_id_valid(last_id):
            yield last_id


if __name__ == "__main__":
    user_id = int(input("Enter an ID: "))
    user_choice = input("Generator or Iterator? (gen/it)? ")
    id_maker = None
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
