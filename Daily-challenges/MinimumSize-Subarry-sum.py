def minSubarrayLength(nums, target):
    left = 0
    currentSum = 0
    minLength = float('inf')

    for right in range(len(nums)):
        currentSum += nums[right]

        while currentSum >= target:
            minLength = min(minLength, right - left + 1)
            currentSum -= nums[left]
            left += 1

    if minLength == float('inf'):
        return 0
    else:
        return minLength
nums = [2, 3, 1, 2, 4, 3]
target = 7
result = minSubarrayLength(nums, target)
print(result)  