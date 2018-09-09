# learning try-except blocks


def count_words(filename):
    """ Count the approximate words in a file"""

    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        msg = "Sorry, the file '{}' does not exists".format(filename)
        print(msg)

    else:
        words = contents.split()
        num_words = len(words)
        print("'{}' has {} words approximately".format(filename, num_words))

filenames = ["alice.txt", "whatever.txt", "hamlet.txt", "moby_dick.txt"]

for filename in filenames:
    count_words(filename)