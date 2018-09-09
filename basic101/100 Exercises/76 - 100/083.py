# Exercise 83

import AppKit

for screen in AppKit.NSScreen.screens():
  print("Width: %s, Height: %s" % (screen.frame().size.width, screen.frame().size.height))

# This solution applies only for MAC

# I had to install pyObjc first:
# pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyobjc
