def draw_stars(list):
    for number in list:
        print "*" * number

#draw_stars([4, 6, 1, 3, 5, 7, 25])

def draw_stars_list(arr):
    for item in arr:
        if isinstance(item, int):
            print "*" * item
        elif isinstance(item, str):
            length = len(item)
            letter = item[0].lower()
            print length * letter

draw_stars_list([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
