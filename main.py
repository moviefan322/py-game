from enemy import Enemy, Troll, Vampire, VampireKing

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

# ghoul = Enemy("Ghoul", 12, 1)
# troll = Troll("Pug")
# troll2 = Troll("Izmak")
# troll3 = Troll("Urg")
# vamp = Vampire("Dracula")
# troll.grunt()
# troll2.grunt()
# troll3.grunt()
# vamp.take_damage(5)
# troll.take_damage(3)

# while vamp.alive:
#         vamp.take_damage(1)
#             print(vamp)

# vamp._lives = 0
# vamp._hit_points = 1
# 
# king = VampireKing("Rudy")
# print(king)
# 
# king.take_damage(12)
# 
# while king._alive:
#     king.take_damage(12)
#     print(king)
