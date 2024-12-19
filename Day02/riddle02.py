def riddle1():
    result = 0
    with open("Day02/input.txt", "r") as f:
        for line in f:
            levels = list(map(int, line.split()))  # Convert space-separated strings to integers
            result += is_safe_with_dampener(levels)
    return result


def is_safe(levels):
    """
    Checks if the levels are safe without removing any level.
    A list is safe if:
    - All differences are between 1 and 3.
    - The sequence is strictly increasing or strictly decreasing.
    """
    if all(earlier > later and 1 <= (earlier - later) <= 3 for earlier, later in zip(levels, levels[1:])):
        return True
    elif all(earlier < later and 1 <= (later - earlier) <= 3 for earlier, later in zip(levels, levels[1:])):
        return True
    return False


def is_safe_with_dampener(levels):
    """
    Checks if the levels are safe with the help of the Problem Dampener.
    - If the list is safe as-is, return 1 (safe).
    - Otherwise, try removing each level and check if it becomes safe.
    """
    if is_safe(levels):
        return 1

    # Try removing each level
    for i in range(len(levels)):
        temp_levels = levels[:i] + levels[i + 1:]  # Remove the i-th level
        if is_safe(temp_levels):
            return 1

    return 0  # Unsafe even with the Dampener


if __name__ == "__main__":
    # Example test cases
    list_full = [
        [7, 6, 4, 2, 1],  # Safe without removing any level
        [1, 2, 7, 8, 9],  # Unsafe regardless of which level is removed
        [9, 7, 6, 2, 1],  # Unsafe regardless of which level is removed
        [1, 3, 2, 4, 5],  # Safe by removing the second level, 3
        [8, 6, 4, 4, 1],  # Safe by removing the third level, 4
        [1, 3, 6, 7, 9],  # Safe without removing any level
    ]

    safe_reports = 0
    for thing in list_full:
        print(f"Report {thing}: {'Safe' if is_safe_with_dampener(thing) else 'Unsafe'}")
        safe_reports += is_safe_with_dampener(thing)
    
    print(f"Number of safe reports: {safe_reports}")
    print(f"Result from file: {riddle1()}")
