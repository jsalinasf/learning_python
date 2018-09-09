# Exercise 36


def count_words(file_path):
    words_to_count = open(file_path).read()
    return len(words_to_count.split())


print(count_words("words1.txt"))


