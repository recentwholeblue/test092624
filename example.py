class character:
    def __init__(self, name, age, eyeColor, height, alive):
        self.name=name
        self.age=age
        self.eyeColor=eyeColor
        self.height=height
        self.alive=alive

def inp(personone):
    name=input("Character name:")
    age=input("Character age: ")
    eyeColor=input("Character eye color:")
    height=input("character height: ")
    alive=input("Is character alive: ")
    personone=character(name, age, eyeColor, height, alive)

inp(personone=1)