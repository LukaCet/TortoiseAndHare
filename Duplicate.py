def find_duplicate(nums):
    tortoise = hare = nums[0]

    while True:
        tortoise = nums[tortoise] 
        hare = nums[nums[hare]] 
        if tortoise == hare: 
            break

    hare = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return tortoise

# Example usage:
nums = [3, 1, 3, 4, 2]
duplicate = find_duplicate(nums)
print(f"The duplicate number is: {duplicate}")
