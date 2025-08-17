import doctest
import math


# 1. Write a Python function called `factorial` that takes an integer as input and returns its factorial.
def factorial(n: int) -> int:
    """Calculate the factorial of a given integer.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 2. Write a Python function called `is_palindrome` that takes a string as input and returns `True` if it is
#    a palindrome and `False` otherwise.
def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome.
    
    Args:
        text: Input string to check
        
    Returns:
        True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        False
        >>> is_palindrome("")
        True
    """
    # Remove spaces and convert to lowercase for better comparison
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

# 3. Write a Python function called `even_or_odd` that takes an integer as input and returns "Even" if
#    the number is even and "Odd" if the number is odd.
def even_or_odd(number: int) -> str:
    """Determine if a number is even or odd.
    
    Args:
        number: Integer to check
        
    Returns:
        "Even" if number is even, "Odd" if number is odd
        
    Example:
        >>> even_or_odd(4)
        'Even'
        >>> even_or_odd(7)
        'Odd'
        >>> even_or_odd(0)
        'Even'
        >>> even_or_odd(-3)
        'Odd'
    """
    return "Even" if number % 2 == 0 else "Odd"

# 4. Write a Python function called `list_sum` that takes a list of integers as input and returns the sum
#    of all elements in the list.
def list_sum(numbers: list) -> int:
    """Calculate the sum of all elements in a list of integers.
    
    Args:
        numbers: List of integers
        
    Returns:
        Sum of all elements in the list
        
    Raises:
        TypeError: If list contains non-integer elements
        
    Example:
        >>> list_sum([1, 2, 3, 4, 5])
        15
        >>> list_sum([-1, -2, 3])
        0
        >>> list_sum([])
        0
    """
    if not numbers:
        return 0
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    
    return sum(numbers)

# 5. Write a Python function called `Greatest Common Divisor (GCD)` that takes two integers as input
#    and returns their greatest common divisor.
def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of two integers using Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        The GCD of a and b
        
    Example:
        >>> gcd(48, 18)
        6
        >>> gcd(54, 24)
        6
        >>> gcd(7, 13)
        1
        >>> gcd(0, 5)
        5
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

# 6. Write a Python function called `is_leap_year` that takes a year as input and returns `True` if it is a
#    leap year and `False` otherwise.
def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year.
    
    A leap year is divisible by 4, but not by 100 unless it's also divisible by 400.
    
    Args:
        year: Year to check
        
    Returns:
        True if leap year, False otherwise
        
    Example:
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2023)
        False
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 7. Write a Python function called `math_operations` that takes three numbers and a string
#    representing an operation ('add', 'subtract', 'multiply', or 'divide'). The function should return the
#    result of the specified operation on the three numbers. Implement the math operations as nested functions.
def math_operations(a: float, b: float, c: float, operation: str) -> float:
    """Perform mathematical operations on three numbers using nested functions.
    
    Args:
        a: First number
        b: Second number
        c: Third number
        operation: String representing operation ('add', 'subtract', 'multiply', 'divide')
        
    Returns:
        Result of the specified operation
        
    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If division by zero is attempted
        
    Example:
        >>> math_operations(10, 5, 2, 'add')
        17.0
        >>> math_operations(10, 5, 2, 'multiply')
        100.0
    """
    def add(x, y, z):
        return x + y + z
    
    def subtract(x, y, z):
        return x - y - z
    
    def multiply(x, y, z):
        return x * y * z
    
    def divide(x, y, z):
        if y == 0 or z == 0:
            raise ZeroDivisionError("Division by zero")
        return x / y / z
    
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")
    
    return operations[operation](a, b, c)

# 8. Write a Python function called `temperature_converter` that takes a temperature value and a
#    string representing the scale ('C' for Celsius or 'F' for Fahrenheit) as input.
#    The function should convert the temperature from one scale to the other using nested functions and
#    return the converted value.
def temperature_converter(temp: float, scale: str) -> float:
    """Convert temperature between Celsius and Fahrenheit using nested functions.
    
    Args:
        temp: Temperature value
        scale: Scale of input temperature ('C' for Celsius, 'F' for Fahrenheit)
        
    Returns:
        Converted temperature value
        
    Raises:
        ValueError: If scale is not 'C' or 'F'
        
    Example:
        >>> temperature_converter(32, 'F')
        0.0
        >>> temperature_converter(100, 'C')
        212.0
    """
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    if scale.upper() == 'C':
        return celsius_to_fahrenheit(temp)
    elif scale.upper() == 'F':
        return fahrenheit_to_celsius(temp)
    else:
        raise ValueError("Scale must be 'C' or 'F'")

# =============================================================================
# TOPICS: LISTS (6 questions × 5 = 30 Marks)
# =============================================================================

# 9. Write a Python program to find the maximum and minimum values in a given list of integers.
def find_max_min(numbers: list) -> tuple:
    """Find maximum and minimum values in a list of integers.
    
    Args:
        numbers: List of integers
        
    Returns:
        Tuple containing (maximum, minimum) values
        
    Raises:
        ValueError: If list is empty
        
    Example:
        >>> find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
        (9, 1)
        >>> find_max_min([-5, -10, -3])
        (-3, -10)
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    max_val = min_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    return max_val, min_val

# 10. Write a Python program to reverse a given list without using any built-in functions.
def reverse_list_manual(lst: list) -> list:
    """Reverse a list without using built-in functions.
    
    Args:
        lst: List to reverse
        
    Returns:
        New reversed list
        
    Example:
        >>> reverse_list_manual([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
        >>> reverse_list_manual(['a', 'b', 'c'])
        ['c', 'b', 'a']
    """
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 11. Given two lists of integers, write a Python program to create a new list that contains elements
#     common to both lists.
def find_common_elements(list1: list, list2: list) -> list:
    """Find common elements between two lists.
    
    Args:
        list1: First list of integers
        list2: Second list of integers
        
    Returns:
        List containing common elements
        
    Example:
        >>> find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        [3, 4]
        >>> find_common_elements([1, 2, 3], [4, 5, 6])
        []
    """
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# 12. Given a list of integers, write a Python program to create a new list that contains the squares of
#     the elements using list comprehension.
def square_list_comprehension(numbers: list) -> list:
    """Create a list of squares using list comprehension.
    
    Args:
        numbers: List of integers
        
    Returns:
        List containing squares of input numbers
        
    Example:
        >>> square_list_comprehension([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
        >>> square_list_comprehension([-2, -1, 0, 1, 2])
        [4, 1, 0, 1, 4]
    """
    return [x**2 for x in numbers]

# 13. Write a Python program to transpose a given matrix represented as a nested list.
def transpose_matrix(matrix: list) -> list:
    """Transpose a matrix represented as a nested list.
    
    Args:
        matrix: 2D list representing a matrix
        
    Returns:
        Transposed matrix
        
    Raises:
        ValueError: If matrix is empty or not rectangular
        
    Example:
        >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
        >>> transpose_matrix([[1, 2], [3, 4], [5, 6]])
        [[1, 3, 5], [2, 4, 6]]
    """
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Check if matrix is rectangular
    if not all(len(row) == cols for row in matrix):
        raise ValueError("Matrix must be rectangular")
    
    # Create transposed matrix
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

# 14. Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat
#     list.
def flatten_nested_lists(nested_list: list) -> list:
    """Flatten a list of nested lists into a single flat list.
    
    Args:
        nested_list: List containing nested lists
        
    Returns:
        Flattened list
        
    Example:
        >>> flatten_nested_lists([[1, 2], [3, 4], [5, 6]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_nested_lists([[1], [2, 3], [4, 5, 6]])
        [1, 2, 3, 4, 5, 6]
    """
    flattened = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened.extend(sublist)
        else:
            flattened.append(sublist)
    return flattened

# =============================================================================
# TOPIC: TUPLE (6 questions × 5 = 30 Marks)
# =============================================================================

# 15. Write a Python program to concatenate two tuples and create a new tuple. And then write a
#     Python program to extract a slice of elements from the new tuple.
def concatenate_and_slice_tuples(tuple1: tuple, tuple2: tuple, start: int = 0, end: int = None) -> tuple:
    """Concatenate two tuples and extract a slice.
    
    Args:
        tuple1: First tuple
        tuple2: Second tuple
        start: Start index for slicing (default: 0)
        end: End index for slicing (default: end of tuple)
        
    Returns:
        Sliced portion of concatenated tuple
        
    Example:
        >>> concatenate_and_slice_tuples((1, 2, 3), (4, 5, 6))
        (1, 2, 3, 4, 5, 6)
        >>> concatenate_and_slice_tuples((1, 2), (3, 4, 5), 1, 4)
        (2, 3, 4)
    """
    concatenated = tuple1 + tuple2
    return concatenated[start:end]

# 16. a) Given a tuple with three elements (x, y, z), write a Python program to unpack the tuple
#     and assign the values to three variables.
#     b) Write a Python program to pack three variables into a single tuple and print the tuple.
def tuple_packing_unpacking_demo():
    """Demonstrate tuple packing and unpacking.
    
    Returns:
        Tuple containing packed values
        
    Example:
        >>> result = tuple_packing_unpacking_demo()
        >>> result
        (10, 20, 30)
    """
    # Unpacking example
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    
    # Packing example
    a, b, c = 100, 200, 300
    packed_tuple = (a, b, c)
    
    return packed_tuple

# 17. a) Write a Python program to sort a tuple of integers in ascending order.
#     b) Write a Python program to reverse a tuple without using any built-in functions.
def sort_and_reverse_tuple_demo(numbers_tuple: tuple) -> tuple:
    """Sort and reverse a tuple of integers.
    
    Args:
        numbers_tuple: Tuple of integers
        
    Returns:
        Tuple containing sorted and reversed results
        
    Example:
        >>> sort_and_reverse_tuple_demo((3, 1, 4, 1, 5, 9, 2, 6))
        ((1, 1, 2, 3, 4, 5, 6, 9), (6, 2, 9, 5, 1, 4, 1, 3))
    """
    # Sort tuple (creates new sorted tuple)
    sorted_tuple = tuple(sorted(numbers_tuple))
    
    # Reverse tuple manually
    reversed_tuple = tuple(numbers_tuple[i] for i in range(len(numbers_tuple) - 1, -1, -1))
    
    return sorted_tuple, reversed_tuple

# 18. Given a tuple containing various elements, write a Python program to count the frequency of a
#     specific element in the tuple.
def count_element_frequency(tuple_data: tuple, element) -> int:
    """Count the frequency of a specific element in a tuple.
    
    Args:
        tuple_data: Tuple to search in
        element: Element to count
        
    Returns:
        Frequency count of the element
        
    Example:
        >>> count_element_frequency((1, 2, 2, 3, 2, 4), 2)
        3
        >>> count_element_frequency(('a', 'b', 'a', 'c'), 'a')
        2
    """
    count = 0
    for item in tuple_data:
        if item == element:
            count += 1
    return count

# 19. Given two tuples of integers, write a Python program to perform element-wise addition,
#     subtraction, and multiplication and create new tuples for each operation.
def tuple_element_wise_operations(tuple1: tuple, tuple2: tuple) -> tuple:
    """Perform element-wise operations on two tuples.
    
    Args:
        tuple1: First tuple of integers
        tuple2: Second tuple of integers
        
    Returns:
        Tuple containing (addition, subtraction, multiplication) results
        
    Raises:
        ValueError: If tuples have different lengths
        
    Example:
        >>> tuple_element_wise_operations((1, 2, 3), (4, 5, 6))
        ((5, 7, 9), (-3, -3, -3), (4, 10, 18))
    """
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length")
    
    addition = tuple(a + b for a, b in zip(tuple1, tuple2))
    subtraction = tuple(a - b for a, b in zip(tuple1, tuple2))
    multiplication = tuple(a * b for a, b in zip(tuple1, tuple2))
    
    return addition, subtraction, multiplication

# 20. Write a Python program that takes an element as input and checks if it exists in a given tuple.
def check_element_in_tuple(tuple_data: tuple, element) -> bool:
    """Check if an element exists in a tuple.
    
    Args:
        tuple_data: Tuple to search in
        element: Element to search for
        
    Returns:
        True if element exists, False otherwise
        
    Example:
        >>> check_element_in_tuple((1, 2, 3, 4, 5), 3)
        True
        >>> check_element_in_tuple(('apple', 'banana', 'cherry'), 'orange')
        False
    """
    return element in tuple_data

# =============================================================================
# TESTING FUNCTIONS
# =============================================================================

def test_all_functions():
    """Test all functions with various inputs."""
    print("Testing Assignment-04 Functions...")
    print("=" * 50)
    
    # Test factorial function
    print(f"1. factorial(5) = {factorial(5)}")
    print(f"   factorial(0) = {factorial(0)}")
    
    # Test palindrome function
    print(f"2. is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"   is_palindrome('hello') = {is_palindrome('hello')}")
    
    # Test even/odd function
    print(f"3. even_or_odd(7) = {even_or_odd(7)}")
    print(f"   even_or_odd(8) = {even_or_odd(8)}")
    
    # Test list sum function
    print(f"4. list_sum([1, 2, 3, 4, 5]) = {list_sum([1, 2, 3, 4, 5])}")
    
    # Test GCD function
    print(f"5. gcd(48, 18) = {gcd(48, 18)}")
    
    # Test leap year function
    print(f"6. is_leap_year(2020) = {is_leap_year(2020)}")
    print(f"   is_leap_year(2023) = {is_leap_year(2023)}")
    
    # Test math operations function
    print(f"7. math_operations(10, 5, 2, 'add') = {math_operations(10, 5, 2, 'add')}")
    print(f"   math_operations(10, 5, 2, 'multiply') = {math_operations(10, 5, 2, 'multiply')}")
    
    # Test temperature converter function
    print(f"8. temperature_converter(32, 'F') = {temperature_converter(32, 'F')}")
    print(f"   temperature_converter(100, 'C') = {temperature_converter(100, 'C')}")
    
    # Test list functions
    numbers_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"9. find_max_min({numbers_list}) = {find_max_min(numbers_list)}")
    
    print(f"10. reverse_list_manual([1, 2, 3, 4, 5]) = {reverse_list_manual([1, 2, 3, 4, 5])}")
    
    list1, list2 = [1, 2, 3, 4], [3, 4, 5, 6]
    print(f"11. find_common_elements({list1}, {list2}) = {find_common_elements(list1, list2)}")
    
    print(f"12. square_list_comprehension([1, 2, 3, 4, 5]) = {square_list_comprehension([1, 2, 3, 4, 5])}")
    
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(f"13. transpose_matrix({matrix}) = {transpose_matrix(matrix)}")
    
    nested = [[1, 2], [3, 4], [5, 6]]
    print(f"14. flatten_nested_lists({nested}) = {flatten_nested_lists(nested)}")
    
    # Test tuple functions
    tuple1, tuple2 = (1, 2, 3), (4, 5, 6)
    print(f"15. concatenate_and_slice_tuples({tuple1}, {tuple2}) = {concatenate_and_slice_tuples(tuple1, tuple2)}")
    
    print(f"16. tuple_packing_unpacking_demo() = {tuple_packing_unpacking_demo()}")
    
    numbers_tuple = (3, 1, 4, 1, 5, 9, 2, 6)
    sorted_result, reversed_result = sort_and_reverse_tuple_demo(numbers_tuple)
    print(f"17. sort_and_reverse_tuple_demo({numbers_tuple}) = sorted: {sorted_result}, reversed: {reversed_result}")
    
    print(f"18. count_element_frequency({numbers_tuple}, 1) = {count_element_frequency(numbers_tuple, 1)}")
    
    tuple1, tuple2 = (1, 2, 3), (4, 5, 6)
    add_result, sub_result, mul_result = tuple_element_wise_operations(tuple1, tuple2)
    print(f"19. tuple_element_wise_operations({tuple1}, {tuple2}) = add: {add_result}, sub: {sub_result}, mul: {mul_result}")
    
    test_tuple = (1, 2, 3, 4, 5)
    print(f"20. check_element_in_tuple({test_tuple}, 3) = {check_element_in_tuple(test_tuple, 3)}")
    print(f"    check_element_in_tuple({test_tuple}, 7) = {check_element_in_tuple(test_tuple, 7)}")

if __name__ == "__main__":
    # Run doctests
    doctest.testmod(verbose=True)
    
    # Run demonstration
    test_all_functions()
