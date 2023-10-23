courses =["MIT", "CyberSecurity", "DataScience"]
print(courses)
# Accessing an element in an array
print(courses[1])

# Lopping through an array
for course in courses:
    print(course)

# Adding an element in an array
courses.append("Android Development")
print(courses)

# removing an element in an array
courses.remove("MIT")
print(courses)
