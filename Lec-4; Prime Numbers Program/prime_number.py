import time

# Record the start time
start_time = time.time()

# Function to check if a number is prime
def is_prime(number):
    let_prime = True
    # Check if the number is 1
    if number == 1:
        print("1 is not prime or composite")
        let_prime = False
    # Loop through numbers from 2 to number - 1
    for i in range(2, number):
        # If the number is divisible by any number in the range, it's not prime
        if number % i == 0:
            let_prime = False
    # Print the result based on whether the number is prime or not
    if let_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

# Get user input
user_num = int(input("Enter your integer to check for prime numbers: "))

# Call the function to check if the entered number is prime
is_prime(user_num)

# Record the end time
end_time = time.time()

# Calculate and print the total time required for execution
total_time = end_time - start_time
print(f"Total time required for execution: {total_time}")