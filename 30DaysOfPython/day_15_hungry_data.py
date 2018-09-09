import csv
import datetime
import os
import shutil
from tempfile import NamedTemporaryFile


def read_data(user_id=None, email=None):
  filename = "data1.csv"
  with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    items = []
    unknown_user_id = None
    unknown_email = None

    for row in reader:
      if user_id is not None:
        if int(user_id) == int (row.get("id")):
          return row
        else:
          unknown_user_id = user_id
      if email is not None:
        if email == row.get("email"):
          return row
        else:
          unknown_email = email
    
    if unknown_user_id is not None:
      return "User id {user_id} not found".format(user_id=user_id)

    if unknown_email is not None:
      return "Email {email} not found".format(email=email)
  return None


def get_length(file_path):
  if os.path.isfile(file_path):
    csvfilereader = open(file_path, "r")
    row_count = sum(1 for row in csvfilereader)
    return row_count
  return 0

def append_data(filepath, name, email, amount):
  fieldNames = ["id", "name", "email", "amount", "sent", "date"]
  # the number of rows
  next_id = get_length(filepath)
  with open(filepath, "a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldNames)
    if next_id < 1:
      writer.writeheader()
      next_id = 1
    writer.writerow({
      "id": next_id,
      "name": name,
      "email": email,
      "sent": "",
      "amount": amount,
      "date": datetime.datetime.now()
    })

# append_data("data1.csv", "User 01", "u1@gmail.com", 123.22)
# append_data("data1.csv", "User 02", "u2@gmail.com", 45.30)
# append_data("data1.csv", "User 03", "u3@gmail.com", 127.80)
# append_data("data1.csv", "User 04", "u4@gmail.com", 56.20)
# append_data("data1.csv", "User 05", "u5@gmail.com", 15)

def edit_data(edit_id=None, email=None, amount=None, sent=None):
  filename = "data1.csv"
  temp_file = NamedTemporaryFile(mode = "w+", delete=False)

  with open(filename, "r") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldNames = ["id", "name", "email", "amount", "sent", "date"]
    writer = csv.DictWriter(temp_file, fieldnames=fieldNames)
    writer.writeheader()
    for row in reader:
      if edit_id is not None:
        if int(row["id"]) == int(edit_id):
          row["amount"] = amount
          row["sent"] = sent
      elif email is not None and edit_id is None:
        if str(row["email"] == str(email)):
          row["amount"] = amount
          row["sent"] = sent
      else:
        pass
      writer.writerow(row)
    shutil.move(temp_file.name, filename)
    return True
  return False


# edit_data(email="u5@gmail.com", amount=69.00, sent="")
print(read_data(user_id=77))
print(read_data(email="u5@gmail.com.ec"))

