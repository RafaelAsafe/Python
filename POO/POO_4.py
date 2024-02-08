# metódos nas classes

class Pig:
    name = "pig"
    years = 0

    def speak(self):
        print(f"OinK! i'm {self.name}! OinK!")

    def pig_years(self):
        return print(self.years*18)


pinko = Pig()
pinko.name = "Pinko"
pinko.years = 2
pinko.speak()
pinko.pig_years()
