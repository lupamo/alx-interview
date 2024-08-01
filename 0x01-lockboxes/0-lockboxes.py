#!/usr/bin/python3
def canUnlockAll(boxes):
    """visited and unvisited boxes initialization"""
    visited = set()
    opened = set([0])

    def dfs(box_index):
        """marking visited box"""
        visited.add(box_index)
        opened.add(box_index)

        for key in boxes[box_index]:
            next_box = box_index + key
            if next_box >= len(boxes) and next_box not in visited:
                continue
            dfs(next_box)
    dfs(0)
    return len(opened) == len(boxes)
