# How to write / read  a CSV File

import csv

# Writing a CSV File
with open("/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/data.csv", "w+") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Description", "Price"])
    writer.writerow(["Platforms II", "IT Book", "16.00"])
    writer.writerow(["SQL queries", "IT Book", "27.10"])
    writer.writerow(["Windows Server", "IT Book", "7.50"])
csv_file.close()

# Reading a CSV File
with open("/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
csv_file.close()

# Appending to a CSV File
with open("/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/data.csv", "a+") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Linux Server", "IT Book", "79.00"])
    writer.writerow(["Electronic Engines", "Mechanic Book", "118.40"])
csv_file.close()

# Reading a CSV File
with open("/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
csv_file.close()

# Reading with DICTIONARIES
with open("/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/data.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
csv_file.close()

# Writting with DICTIONARIES
with open("/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/data.csv", "w") as csv_file:
    fieldnames = ["title", "description", "price"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"title": "New Book 1", "description": "Book 001 USA", "price": 18.90})
    writer.writerow({"title": "New Book 2", "description": "Book 002 ARG", "price": 21.50})
csv_file.close()


# Reading with DICTIONARIES
with open("/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/data.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
csv_file.close()