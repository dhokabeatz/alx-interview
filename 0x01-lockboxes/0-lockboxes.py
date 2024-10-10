#!/usr/bin/python3
"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])  # Set of unlocked boxes, starting with box 0
    stack = [0]  # Stack to explore boxes starting from box 0

    # Explore boxes using DFS
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    # All boxes are unlocked if the number of unlocked boxes equals total boxes
    return len(unlocked) == n
