'''quiz 1. FizzBuzz
Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
"FizzBuzz'''

for Number in range(1, 101):  
    if Number % 3 == 0 and Number % 5 == 0:  # look at at its divisibility for both 3 and 5
        print("FizzBuzz")
    elif Number % 3 == 0:  # look at its divisibility by 3
        print("Fizz")
    elif Number % 5 == 0:  # look at its divisibility by 5
        print("Buzz")
    else:
        print(Number)  
        
'''Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.'''

fib1, fib2 = 0, 1 # starting with the first two numbers

print(fib1, fib2, end=" ")

while True:
    next_fib = fib1 + fib2  # Determine the next sequence of Fibonacci numbers
    if next_fib > 100:  # Stop if the next number exceeds 100
        break
    print(next_fib, end=" ") 
    fib1, fib2 = fib2, next_fib  # go to the next number
    
'''Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.'''

# creating a function to check if a number is a power of two
def Powered2(n):
    if n <= 0:  
        return False
    return (n & (n - 1)) == 0 

# Testing the numbers
print(Powered2(78))  
print(Powered2(0))    
print(Powered2(1))  

'''Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.'''

# creating a Function to capitalize the first letter
def Capital(sentence):
    return sentence.title()

# Testing of the words
print(Capital("hello")) 
print(Capital("hello world!"))

'''Question 5: Reverse Integer

Write a program that takes an integer as input and returns an integer with reversed digit
ordering.'''


def reverse_integer(n):
     
    reversed_num = int(str(abs(n))[::-1]) # reversing the number 
    
    return -reversed_num if n < 0 else reversed_num  # Returning the negative sign if the original number was negative 

# Testing
print(reverse_integer(100))    
print(reverse_integer(91))   
print(reverse_integer(17892)) 

'''Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.'''

# Creating a Function to count vowels in a sentence
def count_vowels(sentence):
    vowels = "aeiouAEIOU"  # the vowels both capital and small letters
    count = sum(1 for char in sentence if char in vowels)
    return count

# Testing of the words
print(count_vowels("Hello World"))   
print(count_vowels("Lynne")) 
print(count_vowels("I love programming!"))  

