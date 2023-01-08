#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    unopened = set(range(1, len(boxes)))
    keys_to_check = boxes[0]
    while keys_to_check:
        key = keys_to_check.pop()
        if key in unopened:
            unopened.remove(key)
            keys_to_check.extend(boxes[key])
    return not unopened

