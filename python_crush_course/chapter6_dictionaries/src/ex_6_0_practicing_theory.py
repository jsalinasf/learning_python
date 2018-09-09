# Practicing Book Examples

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)
print("Alien's color is: {}".format(alien_0["color"]))

alien_0["color"] = "yellow"
print(alien_0)
print("NEW Alien's color is: {}".format(alien_0["color"]))

alien_0["speed"] = "fast"

print("Alien's Position: {}".format(alien_0["x_position"]))

if alien_0["speed"] == "low":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

alien_0["x_position"] += x_increment
print("Alien's New Position: {}".format(alien_0["x_position"]))

print(alien_0)
del alien_0["points"]
print(alien_0)
