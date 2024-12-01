num = int(input("Enter the position (n) of the Fibonacci number: "))
if num < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"The {num}th Fibonacci number is:", fibonacci(num))