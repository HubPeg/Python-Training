# 1 Comparison Operators
# 10 > 3      # ("is greater then")
# True
# 10 >= 3     # ("is greater or equal to")
# True
# 10 < 20     # ("is less then")
# True
# 10 <= 20    # ("is equal or less then")
# True
# 10 == 10    # ("is equal to")
# True
# 10 == "10"  # ("is equal to")
# False
# 10 != "10"  # ("Is not Equal to")
# True

# Comparison operators with Strings
# "bag > "apple"
# -------------------------------------------------
''' Comment Section
# 2 Conditional Statements
temperature = 45
if temperature > 47:  # That's called a bullient expression.
    print("It's", temperature, "Degrees in here.")
elif temperature > 40:
    print("Can you open the window!")
else:
    print("I'm freezing.")
# -------------------------------------------------
# # 3 Ternary Operator
age = 22

# The below Code is simmilar with the second Part.
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

message = "Eligible" if age >= 18 else "Not eligible"
print(message)
# -------------------------------------------------
# 4 Logical Operators
# "and", "or", "not"

# "and"
high_income = False
good_credit = True
student = False

message = "Eligible" if high_income and good_credit else "Not eligible"
print(message)

# "or"
message1 = "Eligible" if high_income or good_credit else "Not eligible"
print(message1)

# "not"
message2 = "Eligible" if (
    high_income or good_credit) and not student else "Not eligible"
print(message2)
# -------------------------------------------------
# 5 Short-circuit Evaluation

# Is working with "high income", "good credit", "student"
if high_income and good_credit and not student:
    print("Eligible")
# -------------------------------------------------
# 6 Chaining Comparison Operators
# age should be between 18 and 65
# age = 22
# if age <= 18 and age > 65:
# Below is the same line of Code just cleaner.
if 18 <= age < 65:  # This is what we call Chaining Comparison Operators
    print("Eligible again")
'''
# -------------------------------------------------
# 8. For Loops
# We use Loops to create repetitions
# Build in Function called range.
'''
for number in range(4): #range(1,4) or range(1, 10, 2)
    print("Great", number, (number) * ".")
'''
# -------------------------------------------------
# 9. For... Else
'''
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
'''
# -------------------------------------------------
# 10. Nested Loops
'''
# So we can put one loop inside of another Loop = Nested Loops
for x in range(1, 6):  # This is the outer Loop
    for y in range(1, 4):  # This is the inner Loop
        print(f"({x}, {y})")
'''
# -------------------------------------------------
# 11. Iterables
'''
print(type(5))
print(type(range(5)))

# Iterable
for x in "Python":  # For each Iteration you will have on Value.
    print(x)
'''
# -------------------------------------------------
# 12. While Loop
'''
number = 100
while number > 25:
    print(number)
    number //= 2

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
'''
# -------------------------------------------------
# Exercise
count = 0
for number in range(1, 20):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers!")
