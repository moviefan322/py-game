from enemy import Enemy, Troll

ghoul = Enemy("Ghoul", 12, 1)
print(ghoul)

troll = Troll("")
print("ALAN: {}".format(troll))

troll2 = Troll("Izmak", 15, 1)
print("Troll2: {}".format(troll2))

troll3 = Troll("Urg", 25)
print(troll, troll2, troll3)
