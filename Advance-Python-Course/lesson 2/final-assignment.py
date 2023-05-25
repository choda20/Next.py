hunger_default = 0


class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=hunger_default):
        self._name = name
        self._hunger = hunger

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hunger(self):
        return self._hunger

    @name.setter
    def name(self, hunger):
        self._hunger = hunger

    def is_hungry(self):
        return True if self._hunger > 0 else False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        print("I am an Animal")

    def special_method(self):
        print("Not implemented")


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

    def special_method(self):
        self.fetch_stick()


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")

    def special_method(self):
        self.chase_laser()


class Skunk(Animal):
    def __init__(self, name, hunger=hunger_default, stink_count=6):
        super(Skunk, self).__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")

    def special_method(self):
        self.stink()

    @property
    def stink_count(self):
        return self._stink_count

    @stink_count.getter
    def stink_count(self,stink_count):
        self._stink_count = stink_count


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")

    def special_method(self):
        self.sing()


class Dragon(Animal):
    def __init__(self, name, hunger=hunger_default, color="Green"):
        super(Dragon, self).__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

    def special_method(self):
        self.breath_fire()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color


if __name__ == '__main__':
    space = "-"*20
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0), Unicorn("Keith", 7), Dragon("Lizzy", 1450)]
    new_animals = [Dog("Doggo", 80), Cat("Kitty", 80), Skunk("Stinky Jr.", 80), Unicorn("Clair", 80),
                   Dragon("McFly", 80)]
    zoo_lst.extend(new_animals)

    for animal in zoo_lst:
        print(space)
        print(animal.__class__.__name__ + " " + animal.name)
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        animal.special_method()

    print(space)
    print("Zoo name is: " + Animal.zoo_name)

