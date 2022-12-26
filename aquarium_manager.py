import json

f = open("aquarium.json", encoding=utf8)
animal = json.loads(f)
animals = data_aquarium["data"]

def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False



animals_fish = list(filter(verify_fish, animals))
print(animals_fish)