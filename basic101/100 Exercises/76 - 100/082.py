# Exercise #82 - Ephem

import ephem

Jupiter = ephem.Jupiter()

Jupiter.compute("1230/01/01")

print(Jupiter.sun_distance * 149597870.691)
