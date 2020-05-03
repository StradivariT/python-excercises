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
    return "".join(list(map(lambda x : x[:-1] + x[-1].upper() + " ", word.split())))

print("\nLast letter upper")
print(f"{otherString} -> {lastLetterUpper(otherString)}")