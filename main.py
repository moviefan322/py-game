from enemy import Enemy, Troll, Vampire

ghoul = Enemy("Ghoul", 12, 1)
print(ghoul)

troll = Troll("Pug")
print("ALAN: {}".format(troll))

troll2 = Troll("Izmak")
print("Troll2: {}".format(troll2))

troll3 = Troll("Urg")
print(troll, troll2, troll3, sep="\n")

vamp = Vampire("Dracula")

troll.grunt()
troll2.grunt()
troll3.grunt()

print(vamp)
vamp.take_damage(5)
print(vamp)

troll.take_damage(3)

while vamp.alive:
    vamp.take_damage(1)
    print(vamp)
