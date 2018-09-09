# Exercise 29


from math import pi


def liquid_volume(h, r=10):
    answer = ((4 * pi * (r ** 3)) / 3) - ((pi * (h ** 2) * ((3 * r) - h)) / 3)
    return answer


print(liquid_volume(2))
