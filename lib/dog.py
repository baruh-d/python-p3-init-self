#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed
        print(f"{name} is born!")
    def bark(self):
        print("Woof!")
    def get_adopted(self, owner_name):
        self.owner = owner_name
    def showing_self(self):
        return self
        
fido = Dog("Fido")
fido.name
fido.breed
# adopt(fido, "Sophie")
fido.get_adopted("Sophie")
print(fido.owner)
# fido.showing_self()

snoopy = Dog("snoopy")
snoopy.name
snoopy.breed