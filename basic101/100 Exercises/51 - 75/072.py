# Exercise 72
from selenium import webdriver

base_url = "https://www.google.com/search?source=hp&ei=b3v0WpjaJ5CYzwKj5Z_gDg&q="

search_string = input("Enter search term: ")

url = base_url + search_string

driver = webdriver.Firefox()
driver.get(url)
