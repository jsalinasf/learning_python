# Exercise 10.4 - Writing Files - Responses

filename = "responses.txt"
reason = ""

print("\nPoll - Why are you learning how to code")

with open(filename, "w") as file_object:  # In here Im using "WRITE"
    while reason != "n":
        reason = input("Input your reason ('n' to qui)?: ")
        if reason != "n":
            file_object.write(reason + "\n")
