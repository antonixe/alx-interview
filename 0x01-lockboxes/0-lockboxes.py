def canUnlockAll(boxes):
    keys = [0]
    opened = [False] * len(boxes)
    opened[0] = True
    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)
