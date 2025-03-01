# 6. String Methods
course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("pro"))
print(course.replace("p", "g"))
print("pro" in course)
print("swift" in course)

# 7. Numbers
x = 1
x = 1.1
x = 1+2j  # a + bi

# Standard operators
print(10 + 3)  # addition
print(10 - 3)  # substraction
print(10 * 3)  # multiplication
print(10 / 3)  # division
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
c = x + 3
x += 3

# 8. Working with Numbers
print(round(2.9))
print(abs(-2.9))

# print(math.ceil(2.9))

# https://docs.python.org/3/library/math.html

# 9. Type Conversion
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy
# ""
# 0
# None

# 10. Quiz

# What are the primitive types in Python?
# We have Strings (str), Numbers (int) and Floats (float)

# What is shown in this Task
fruit = "Apple"
print(fruit[1])
# Answer is "p"

print(fruit[1:-1])
# Answer is "ppl"

# What is the result of..
print(10 % 3)
