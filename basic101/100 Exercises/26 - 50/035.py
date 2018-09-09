# Exercise 35


def count_words(string_to_count):
    total_words = string_to_count.split()
    print(total_words)
    return len(total_words)


print(count_words("Hello my Name is George"))
