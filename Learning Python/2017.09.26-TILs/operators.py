"""Operators in Python"""

A_ = 3
B_ = 7
C_ = 0

#Addition (+)
C_ = A_ + B_
print(A_, '+', B_, '=', C_, sep=' ')
#enumerate with commas, use separator character

#Subtraction (-)
C_ = A_ - B_
print(str(A_) + ' - ' + str(B_) + ' = ' + str(C_))
#or concatenate manually, cast to str through constructor

#Multiplication (*)
C_ = A_ * B_
print("%3.2f * %3.2f = %3.2f" % (A_, B_, C_))
#the string modulo overload - use as placeholder with tuple
#in this case - 3 digits total, 2 after decimal point, float
#https://www.python-course.eu/python3_formatted_output.php

#Division (/)
CC_ = A_ / B_
print("%i / %i = %f" % (A_, B_, CC_))

#Modulus (divide and return remainder) (%)
C_ = A_ % B_
print("%3.1f %% %3.1f = %.1f" % (A_, B_, C_))
#to escape the % str placeholder, use %% in the string

#Exponent (power) (**)
C_ = A_ ** B_
print(A_, '**', B_, '=', C_, sep=" ")

#Floor division (truncates decimal symbols) (//)
AA_ = 3.5
BB_ = 6.7
CC_ = BB_ // AA_
print(AA_, '//', BB_, '=', CC_, sep=" ")
