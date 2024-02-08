class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.sound} my name is {self.name}! {self.sound}')


class Piglet(Animal):
    sound = 'OinK'


class Cow(Animal):
    sound = 'Muuu'


parco = Piglet('Parco')
parco.speak()

mimosa = Cow('Mimosa')
mimosa.speak()
