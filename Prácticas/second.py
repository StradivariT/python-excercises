import re

properString = "Fer"
def isFirstLetterUppercase(word):
    return word.istitle()

print("Check if first letter of word is uppercase")
print(f"{properString} -> {isFirstLetterUppercase(properString)}")

otherString = "Final Fantasy VII Remake"
def countWords(words):
    return len(words.split())

print("\nCount words in sentence")
print(f"{otherString} -> {countWords(otherString)}")

def getWords(words):
    return words.split()

print("\nGet words in sentence")
print(f"{otherString} -> {getWords(otherString)}")

def reverseString(str):
    return str[::-1]

print("\nReverse string")
print(f"{otherString} -> {reverseString(otherString)}")

def lastLetterUpper(word):
    return word[:-1] + word[-1].upper()

print("\nLast letter upper")
print(f"{otherString} -> {lastLetterUpper(otherString)}")

emailRegex = re.compile(r"[^@]+@[^@]+\.[^@]+")
invalidEmail = "not valid email"
validEmail = "something@gmail.com"

print("\nCheck email address")
print(f"{invalidEmail} -> {emailRegex.match(invalidEmail)}")
print(f"{validEmail} -> {emailRegex.match(validEmail)}")