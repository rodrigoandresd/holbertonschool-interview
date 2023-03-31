#!/usr/bin/python3
"""
We have n number of locked boxes in front of us.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):

    n = len(boxes)
    visited = [False] * n  # initially, no boxes are visited
    visited[0] = True  # mark the first box as visited
    queue = [0]  # start the BFS from the first box
    while queue:
        box = queue.pop(0)  # get the next box from the queue
        for key in boxes[box]:  # check all keys in the box
            if key < n and not visited[key]:
            # make sure the key is valid and not visit
                visited[key] = True  # mark the box as visited
                queue.append(key)
                # add the box to the queue for further exploration
    return all(visited)  # check if all boxes are visited
