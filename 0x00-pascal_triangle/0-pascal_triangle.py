#!/usr/bin/python3
"""
0-pascal_triangle
Module to generate Pascal's Triangle without using any external modules
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows without using any external modules.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of lists of int: The Pascal's Triangle up to n rows.
                              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []  # Initialize the triangle list

    for row_num in range(n):
        if row_num == 0:
            # The first row is always [1]
            triangle.append([1])
        else:
            prev_row = triangle[-1]  # Get the last row from the triangle
            current_row = [1]  # Start the current row with 1

            # Compute the intermediate values by summing adjacent elements from the previous row
            for i in range(1, len(prev_row)):
                current_row.append(prev_row[i - 1] + prev_row[i])

            current_row.append(1)  # End the current row with 1
            triangle.append(current_row)

    return triangle
