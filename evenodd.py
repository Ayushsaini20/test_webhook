def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

# Test the function with some examples
test_numbers = [4, 7, 10, 15, 0, -3]
for num in test_numbers:
    result = check_even_odd(num)
    print(result)

# Alternatively, take user input
try:
    user_num = int(input("Enter a number to check: "))
    print(check_even_odd(user_num))
except ValueError:
    print("Please enter a valid integer!")
    
# check for outputs
#even odd code
