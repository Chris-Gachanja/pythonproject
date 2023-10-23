# Data type
number = 100  # int
second = 56.78  # this data type is called a float
text = "Hello there"  # string
ispythoninteresting = True  # boolean

# stores multiple value in a variable
cars = ["toyota", "nissan", "VW", 60]  # list
fruits = ("bananas", "oranges", "apples")  # Tuple
countries = {"Kenya", "Tanzania", "Tunisia", "Algeria"}
details = {
    "firstname":"Chris",
    "age": 37,
    "course" : "Trainer",
    "nationality": "Kenyan"
} # dictionary

print(details["firstname"])
print(details["age"])
print(second)
print(text)
print(cars)
print(countries)

# determine a data type
print(type(text))
print(type(countries))
print(type(details))

# Typecasting- converting one data type to another
print(float(number))
print(int(second))
