# Exercise 075

import pandas
import pylab as plt

data_1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_1.plot(x="x", y="y", kind="scatter")
data_1.plot(x="x", y="y", kind="line")
data_1.plot(x="x", y="y", kind="bar")
plt.show()
