def two_indices(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    nums = [13, 7, 11, 2, 8]
    target = 9
    indices = two_indices(nums, target)
    print(indices)
