import turtle

def mySquare(mySide):
    myT.forward(mySide)
    myT.left(90)
    myT.forward(mySide)
    myT.left(90)
    myT.forward(mySide)
    myT.left(90)
    myT.forward(mySide)
    myT.left(90)
    return mySide * mySide

myT = turtle.Turtle()

area01 = mySquare(25)
myT.left(90)

area02 = mySquare(50)
myT.left(90)

area03 = mySquare(75)
myT.left(90)

area04 = mySquare(100)
myT.left(90)

print(area01,area02,area03,area04)
