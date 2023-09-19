from enemy import Enemy

ghoul = Enemy("Ghoul", 12, 1)
print(ghoul)

ghoul.take_damage(4)
print(ghoul)

ghoul.take_damage(8)
print(ghoul)

ghoul.take_damage(9)
print(ghoul)
