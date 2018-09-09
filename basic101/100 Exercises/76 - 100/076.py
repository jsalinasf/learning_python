# Exercise 076

# Esta fue mi solucion:

# import datetime
# myDate = datetime.date.today()
# print("Today is {}, {} {}, {}".format(myDate.strftime("%A"), myDate.strftime("%B"), myDate.day, myDate.year))

from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y"))
