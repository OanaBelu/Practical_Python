# This is an Age Calculator that shows how many decades old a person is

age = int(input("How old are you ? \n"))

decades = age // 10
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old. ")
