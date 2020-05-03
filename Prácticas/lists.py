import math

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mid = math.floor(len(lst) / 2)

print("Sublist with two elements, which corresponds to half the elements")
print([lst[:mid], lst[mid:]])

print("\nFirst and last elem")
print(f"{lst[0]} {lst[-1]}")

doubleList = lst + lst
print("\nAdding the elements of the list to the end")
print(doubleList)

doubleList.sort()
print("\nSort double list")
print(doubleList)

doubleList.sort(reverse = True)
print("\nSort in reverse")
print(doubleList)

cubeList = map(lambda x: x * x * x, doubleList)
print("\nElements cube")
print(list(cubeList))