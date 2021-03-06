# LAB 1, VARIANT 4
# Maxim Pupykin, group 6312

import re
correct_numbers = []

with open("phone-numbers.txt", "r") as numbers:
    input_string = numbers.read()
input_numbers = re.split(r"[^0-9+\-()]", input_string)

for number in input_numbers:
    if re.fullmatch(r"(9\d{7}|\(9\d{2}\)\d{3}(?:-\d{2}-|\d{2})|9\d{2}-\d{3}-\d{2}-)\d{2}", number):
        correct_numbers.append(number)
    elif re.fullmatch(r"(?:8|\+?7)(\d{8}|\(\d{3}\)\d{3}(?:-\d{2}-|\d{2})|-\d{3}-\d{3}-\d{2}-)\d{2}", number):
        correct_numbers.append(number)

numbers = open("correct-numbers.txt", "w")

for number in correct_numbers:
    numbers.write(number + "\n")

numbers.close()
