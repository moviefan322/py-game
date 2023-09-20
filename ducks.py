class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water is lovely")

    def quack(self):
        print("Quack quack")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle")

    def swim(self):
        print("Come on in, but it's a bit chilly")

    def quack(self):
        print("Are you 'avin a larf?")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)
    percy = Penguin()
    test_duck(percy)
