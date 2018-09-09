# Exercise 74

import pandas

data_1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

pandas.concat([data_1, data_2])

pandas.concat([data_1, data_2]).to_csv("/Users/user01/Documents/Developer/learning_python/basic101/100 Exercises/51 - 75/074.txt", index=None)

