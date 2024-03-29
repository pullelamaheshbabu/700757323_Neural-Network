
#PROGRAM 1
# Input the string "Python"
ip_pg1 = list(input("Enter the string: "))

# Deleting at least 2 characters
if len(ip_pg1) >= 2:
    del ip_pg1[:2]

# Reverse the obtained string
resultant_string = ip_pg1[::-1]

# Print the final reversed string
print("Sample output:")
print("".join(resultant_string))

#PROGRAM 2
# Taking two numbers from the user
k1 = int(input("First number: "))
k2 = int(input("Second number: "))

# Performing arithmetic operations
addition_rslt = k1 + k2
subtraction_rslt = k1 - k2
multiplication_rslt = k1 * k2
divison_rslt = k1 / k2

# Print the results of arithmetic operations
print("Arithmetic Operations:")
print(f"Addition: {addition_rslt}")
print(f"Subtraction: {subtraction_rslt}")
print(f"Multiplication: {multiplication_rslt}")
print(f"Division: {divison_rslt}")

#PROGRAM 3
# Taking a sentence from the user
inpt_sentence = input("Enter a sentence: ")

# Replacing each occurrence of 'python' with 'pythons'
opt_sentence = inpt_sentence.replace('python', 'pythons')

# Print the modified sentence
print("Sample output:")
print(opt_sentence)

#PROGRAM 4
# Take the class score from the user
clas_score = float(input("Enter class score: "))

# Determining the letter grade based on the grading scheme
if 90 <= clas_score <= 100:
    grade = 'A'
elif 80 <= clas_score < 90:
    grade = 'B'
elif 70 <= clas_score < 80:
    grade = 'C'
elif 60 <= clas_score < 70:
    grade = 'D'
else:
    grade = 'F'

# Print the letter grade
print(f"The grade {clas_score} is: {grade}")
