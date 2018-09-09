# Exercise 73 - Instructor solution

import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")

data_2 = data * 2

data_2.to_csv("/Users/user01/Documents/Developer/learning_python/basic101/100 Exercises/51 - 75/073.txt", index=None)

