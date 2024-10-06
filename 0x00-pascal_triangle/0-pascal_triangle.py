#!/usr/bin/python3

from math import factorial


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows using the combinatorial formula.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of lists of int: The Pascal's Triangle up to n rows.
                              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []  # Initialize the triangle list

    for row in range(n):
        current_row = []  # Initialize the current row
        for r in range(row + 1):
            # Compute the combinatorial number C(row, r)
            ncr = factorial(row) // (factorial(r) * factorial(row - r))
            current_row.append(ncr)
        triangle.append(current_row)

    return triangle
