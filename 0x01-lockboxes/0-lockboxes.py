#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [key for key in boxes[0]]
    while keys:
        key = keys.pop(0)
        if key >= 0 and key < n:
            if not opened[key]:
                opened[key] = True
                keys.extend(boxes[key])
    return all(opened)
