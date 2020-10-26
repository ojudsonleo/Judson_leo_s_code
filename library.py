# Optional Parameters

class help(object):
    class sLib(object):
        def func(word="", add=0, freq=1):
            print(word * (freq + add))

    sLib.func("commands:")
    sLib.func("         Lib.Dog.num_dogs()")
    sLib.func("          print(Lib.Dog.bark)")
    sLib.func("         test = library.NotPrivate(name)")
    sLib.func("         test._display()")
    sLib.func("         test.display()")
    sLib.func("         test.priv()")
    sLib.func("         name1 = library.sLib.func(word, add, freq)")
    sLib.func("         name = library.Point(number, number)")
    sLib.func("         name2 = library.Point(number, number)")
    sLib.func("         print(name>name2)")
    sLib.func("         print(name<=name2)")
    sLib.func("         print(name>=name2)")
    sLib.func("         print(name==name2)")
    sLib.func("         print(name+name2)")
    sLib.func("         print(name-name2)")
    sLib.func("         print(name*name2)")
    sLib.func("         dog = library.Dog(name, age)")
    sLib.func("         dog.speak()")
    sLib.func("         dog.talk()")
    sLib.func("         cat = library.Cat(name, age, color)")
    sLib.func("         cat.speak()")
    sLib.func("         cat.talk()")
    sLib.func("         lion = library.Lion(name, age)")
    sLib.func("         lion.speak()")
    sLib.func("         lion.talk()")
    sLib.func("         snake = library.tiger(name, age)")
    sLib.func("         snake.speak()")
    sLib.func("         snake.talk()")
    print("running on background:")


class Dog(object):

    def add_weight(self, weight):
        self.weight = weight

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                   33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                   58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 77, 78, 78, 79, 79,
                   80, 81, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 90, ]

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a Dog")

    def talk(self):
        print("Bark!")


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow  Hi i am", self.name, "and i am", self.age, "years old and i am a Cat")

    def talk(self):
        print("Meow!")

        # time = 2:57:08 / 6:21:12


class Lion(object):
    # TODO: Lion class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                   33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                   58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 77, 78, 78, 79, 79,
                   80, 81, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 90, ]

    def talk(self):
        print("kkkk!")

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a Lion i will eat every animal")

    def talk(self):
        print("Bark!")


class snake(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                   77, 78, 78, 79, 79, 80, 81, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 90, ]

    def speak(self):
        print("sss Hi i am", self.name, "and i am", self.age, "years old and i am a snake")

    def talk(self):
        print("ssssssss!")


class tiger(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.data = [name]

    def talk(self):
        print("KKKKKKKKKK!")

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a tiger and i will also eat every animal")


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x + self.y + p.x)

    def __sub__(self, p):
        return Point(self.x - p.x - self.y - p.x)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "Point(x=" + str(self.x) + "," + "y=" + str(self.y) + ")"


class _Private:
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("hello")

    def display(self):
        print("hi")


class Lib(object):
    class Dog:
        dogs = []

        def __init__(self, name):
            self.name = name
            self.dogs.append(self)

        @classmethod
        def num_dogs(cls):
            return len(cls.dogs)

        @staticmethod
        def bark(n):
            """barks n times"""
            for _ in range(n):
                print("Bark!")


class car(object):
    def __init__(self, make, model, year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print("this car %s %s from %s, it is  %s and has %s ths." % (
            self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("this car is a %s %s from %s." % (self.make, self.model, self.year))


whip = car("fsjhfs", "adafd", 5353, "ndjsagy", 0)
whip.display(True)
