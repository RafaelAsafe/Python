class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

green_apple = Apple("Green","bitter")

green_grape = Grape("Green","bitter")

print(green_apple.color, green_apple.flavor)


