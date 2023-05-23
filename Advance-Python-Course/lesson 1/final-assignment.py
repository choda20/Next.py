import functools


def get_longest_name(file_name):  # 1
    with open(file_name, "r") as names:
        return functools.reduce(max, [name.replace("\n", "") for name in names.readlines()])


def sum_names_length(file_name):  # 2
    with open(file_name, "r") as names:
        return functools.reduce(lambda x, y: x + y, [len(name.replace("\n", "")) for name in names.readlines()])


def print_shortest_names(file_name):  # 3
    with open(file_name, "r") as names:
        names_in_file = names.readlines()
        shortest_length = functools.reduce(min, [len(name.replace("\n", "")) for name in names_in_file])
        print("".join([name for name in names_in_file if (len(name.replace("\n", "")) == shortest_length)]))


def create_length_file(file_name):  # 4
    with open(file_name, "r") as names:
        with open("name_length.txt", "w") as dest:
            dest.write("\n".join([str(len(name.replace("\n", ""))) for name in names]))


def print_names_by_length(file_name):  # 5
    length = int(input("Enter name length: "))
    with open(file_name, "r") as names:
        print("".join([name for name in names.readlines() if len(name.replace("\n", "")) == length]))


if __name__ == '__main__':
    print(get_longest_name("names.txt"))
    print(sum_names_length("names.txt"))
    print_shortest_names("names.txt")
    create_length_file("names.txt")
    print_names_by_length("names.txt")
