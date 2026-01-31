python# Day 005 - FizzBuzz Challenge
# The classic programming interview question!

# Print numbers 1 to 100, but:
# - Multiples of 3: print "Fizz"
# - Multiples of 5: print "Buzz"  
# - Multiples of both 3 and 5: print "FizzBuzz"
# - Otherwise: print the number

for number in range(1, 101):
    # Check divisible by BOTH 3 and 5 first (divisible by 15)
    if number % 15 == 0:
        print("FizzBuzz")
    # Then check divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # Then check divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # If none of the above, print the number
    else:
        print(number)
