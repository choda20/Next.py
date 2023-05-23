class Dog:
    count_animals = 0

    def __init__(self, age, name="Octavio"):
        self._age = age
        self._name = name
        Dog.count_animals += 1

    def birthday(self):
        self._age += 1

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._y = y
        self._x = x

    def set_greyscale(self):
        avg = (self._green + self._red + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        is_one_color = [self._red, self._green, self._blue].count(0) == 2
        pixel_color = ""
        if is_one_color:
            pixel_color = "Red" if self._red != 0 else "Green" if self._green != 0 else "Blue"
        print("X: {x}, Y: {y}, Color: ({red},{green},{blue}) {pixel_color}".format(x=self._x, y=self._y, red=self._red,
                                                                                   green=self._green, blue=self._blue,
                                                                                   pixel_color=pixel_color))


def ex222():  # 2.2.2
    dog_1 = Dog(8)
    dog_2 = Dog(12)
    dog_1.birthday()
    print("Dog 1 age is: " + str(dog_1.age))
    print("Dog 2 age is: " + str(dog_2.age))


def ex233():  # 2.3.3
    print("\n")
    dog_1 = Dog(8, "Sid")
    dog_2 = Dog(12)
    print("Dog 1 name is: " + dog_1.name)
    print("Dog 2 name is: " + dog_2.name)
    dog_1.name = "Haim"
    print("Dog 1 new name is: " + dog_1.name)
    print("Animal count is: " + str(Dog.count_animals))
    print("\n")


def ex234():  # 2.3.4
    pixel = Pixel(5, 6, 250, 0, 0)
    pixel.print_pixel_info()
    pixel.set_greyscale()
    pixel.print_pixel_info()
    print("\n")


if __name__ == '__main__':
    ex222()
    ex233()
    ex234()
