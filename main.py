# 26.1
# Checking, using list comprehension, how to square a list
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [number * number for number in numbers]
#
#
# print(squared_numbers)

# 26.2
# Checking, using list comprehension, how to find an even number out of a list
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# result = [num for num in numbers if (num % 2) == 0]
#
# print(result)

# 26.3
# Opens 2 files containing numbers and find the common things between the 2 lists.
file1 = open("file1.txt", "r")
new_file1 = [int(file) for file in file1]

file2 = open("file2.txt", "r")
new_file2 = [int(file) for file in file2]

s = set(new_file2)

result = [file for file in new_file1 if file in s]

# Write your code above 👆

print(result)

