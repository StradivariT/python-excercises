import re

emailRegex = re.compile(r"[^@]+@[^@]+\.[^@]+")
invalidEmail = "not valid email"
validEmail = "something@gmail.com"

print("\nCheck email address")
print(f"{invalidEmail} -> {emailRegex.match(invalidEmail)}")
print(f"{validEmail} -> {emailRegex.match(validEmail)}")