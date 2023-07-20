#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    :param boxes: a list of lists, where each inner list represents the keys in a box
    :return: True if all boxes can be opened, else False
    """
    n = len(boxes)
    keys = [0]
    opened = [False] * n
    opened[0] = True
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)
