def moveZeroes(nums):

# ============================
# V1 (mine, no help)
# ============================
    # for i, n in enumerate(nums):
        # if n == 0:    
            # print(f"index {i} is a 0")
            # print("…swapping it w/ '-' for now")
            # zeroes_to_add += 1
            # nums.append(0)
            # nums.remove(nums[i])
            # nums.append(0)
    # print(f"…now i need to append {zeroes_to_add} 0s to the end")
    # print(nums)
    # nums.extend([0] * zeroes_to_add)


# ============================
# V2 from other submissions
# ============================
    left, right = 0, 1
    for right in range(len(nums)):
        if nums[right] != 0:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
        if nums[left] != 0:
            left += 1


    print(nums)


# ============================
# tests
# ============================

moveZeroes([0, 1, 0, 3, 12])        # [1, 3, 12, 0, 0]
# moveZeroes([0])                     # [0]
# moveZeroes([0, 0, 1])               # [1, 0, 0]