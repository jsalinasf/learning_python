myName = input('What is your name: ')
print('Hello',myName)

myAge = int(input('Whats is your Age: '))
actualYear = int(input('Whats year is this: '))
birthdayPassed = input('Have you already celebrated your birthday this year (S/N)?: ')

if birthdayPassed == 'S':
    myAge = actualYear - myAge
else:
    myAge = actualYear - myAge - 1

print('You were born on: ', myAge)
