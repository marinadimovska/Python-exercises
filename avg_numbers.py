def avg(*args):
    # Calculate the sum of the arguments
    total = sum(args)
    
    # Calculate the average
    average = total / len(args)
    
    return average

# Test the function with provided arguments
arguments = input().split()
arguments = [int(arg) for arg in arguments]  # Convert arguments to integers
result = avg(*arguments)

# Print the result with exactly 2 decimal places
print("{:.2f}".format(result))
