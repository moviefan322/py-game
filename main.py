from enemy import Enemy, Troll

ghoul = Enemy("Ghoul", 12, 1)
print(ghoul)

troll = Troll("Pug")
print("ALAN: {}".format(troll))

troll2 = Troll("Izmak")
print("Troll2: {}".format(troll2))

troll3 = Troll("Urg")
print(troll, troll2, troll3, sep="\n")

troll.grunt()
troll2.grunt()
troll3.grunt()
