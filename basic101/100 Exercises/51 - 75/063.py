# Exercise 63

import time

i = 0

while True:
  print("Hello")
  i += 1
  if i > 3:
    print("End of Loop")
    break
  time.sleep(i)
  