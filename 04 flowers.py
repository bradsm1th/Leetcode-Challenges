# 0 == 'empty'
# 1 == 'not empty'


def canPlaceFlowers(flowerbed, n):
    print(f" before planting: {flowerbed} ".center(50, "-"))
    planted_so_far = 0
    for flower in range(len(flowerbed)):
        # print(f"index: {flower}\nvalue: {flowerbed[flower]}") 
        print(f"You have {n - planted_so_far} flowers left to plant")
        if flowerbed[flower] == 0:
            # True immediately if it's the very first one — there *isn't* a left side
            left_side_empty = (flower == 0) or (flowerbed[flower - 1] == 0)
            # Right side. Same except last instead of first
            right_side_empty = (flower == len(flowerbed) - 1) or (flowerbed[flower + 1] == 0)
            
            # print(left_side_empty, "<- left side")
            # print(right_side_empty, "<- right side")
   
            if left_side_empty and right_side_empty:
                print(f"you should plant here: '[{flower}]'…")
                flowerbed[flower] = 1
                planted_so_far += 1

    print(f" after planting: {flowerbed} ".center(50, "-"))
    return planted_so_far >= n
    
    # examples


# print(canPlaceFlowers([1,0,0,0,1], 1))     # true
# print(canPlaceFlowers([1,0,0,0,1], 2))     # false
# print(canPlaceFlowers([0, 0, 0, 0, 1], 2))  # true
# print(canPlaceFlowers([1,0,1,0,0], 1))     # true
print(canPlaceFlowers([1,0,1,0,0], 3))     # false

