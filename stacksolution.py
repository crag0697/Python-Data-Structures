def check_reverse(input_data):
    stack = []

    # Push each element of input_data onto the stack
    for item in input_data:
        stack.append(item)

    reversed_data = []

    # Pop each element from the stack to construct the reversed data
    for i in range(len(stack)):
        reversed_data.append(stack.pop())

    # Check if the input data is the same as its reverse
    return input_data == reversed_data

# Test cases
print(check_reverse([18, 15, 20, 1, 20, 15, 18]))  # Test 1: True
print(check_reverse([5, 7, 9, 2, 8, 6, 4, 1, 3, 3, 1, 4, 6, 8, 2, 9, 7, 5]))  # Test 2: True
print(check_reverse([42, 17, 36, 42, 16, 42]))  # Test 3: False
print(check_reverse([]))  # Test 4: True
