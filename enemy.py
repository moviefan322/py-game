class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("{} took {} damage and has {} left".format(self.name, damage, self.hit_points))
        else:
            self.lives = self.lives - 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}; Lives: {0.lives}; HitPoints: {0.hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}, {0.name} stomp you".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        # super(Vampire, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=3, hit_points=12)

    def hiss(self):
        print("Me {0.name}, {0.name} drink your blood".format(self))
