# Exercise 37


def count_words(file_path):
    words_to_count = open(file_path).read()
    return len(words_to_count.replace(",", " ").split())


print(count_words("words2.txt"))


