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
# file1 = open("file1.txt", "r")
# new_file1 = [int(file) for file in file1]
#
# file2 = open("file2.txt", "r")
# new_file2 = [int(file) for file in file2]
#
# s = set(new_file2)
#
# result = [file for file in new_file1 if file in s]
#
# # Write your code above 👆
#
# print(result)

# 26.4 Uses dictionary comprehension to create a dictionary of all the words in the string and then give the length
# of the word in the dic.
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# words = sentence.split()
#
# result = {word:len(word) for word in words}
#
# print(result)


# 26.5 Uses dictionary comprehension to go over a dictionary and change the temps from C to F

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day:((temp * 9/5) + 32) for (day,temp) in weather_c.items()}
#
# print(weather_f)

# 26.6 Looping through Pandas

# import pandas
# student_dict = {
#     "student": ["angela", "james", "lily"],
#     "score": [56, 76, 98]
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # loop through a data frame
#
# for (key, value) in student_data_frame.items():
#     print(value)

# loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)

# # Loop through row with a specific row in mind
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "angela":
#         print(row.score)