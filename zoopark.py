class Animal:
    def reply(self):
        self.speak()


class Mamal(Animal):
    def speak(self):
        print('Mamal.Speak')


class Dog(Mamal):
    def speak(self):
        print('Dog.speak')


class Cat(Mamal):
    def speak(self):
        print('Cat.speak')


class Primate(Mamal):
    def speak(self):
        print('Primate.speak')


class Hacker(Primate):
    pass


if __name__ == '__main__':
    spot = Cat()
    spot.reply()
    data = Hacker()
    data.reply()