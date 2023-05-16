from utensil import Utensil

from utensil import Person
print()
fork = Utensil("fork", "metal")

spoon = Utensil("spoon", "plastic")

knife = Utensil("knife","gold")

spork = Utensil("spork", "plastic")

print(fork.material)
print(spoon.material)
print(knife.material)
print(spork.material)


print()
knife.cut()
fork.pickfood()
spork.pickfood()


print()








kylee = Person("kylee", 16, 10)
kylee.numberOfFingers()
kylee.driving()


kylee.speak()


bob = Person()
bob.introduceSelf()
kylee.introduceSelf()


kylee.setName("Shane")
kylee.introduceSelf()
kylee.setName("Kylee")
kylee.introduceSelf()