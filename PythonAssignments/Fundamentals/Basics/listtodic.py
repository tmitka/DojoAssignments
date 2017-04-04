name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    favorites = zip(arr1, arr2)
    favorites_dict = dict(favorites)
    return favorites_dict

make_dict(name, favorite_animal)