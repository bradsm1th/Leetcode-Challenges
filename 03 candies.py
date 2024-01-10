def kidsWithCandies(candies, extraCandies):
    # find max of starting candies
    # highest_count = max(candies)
    
    # # do T/F for each kid: if they get all the extra, will they have *at least* highest_count?
    # results = [(candies[index] + extraCandies >= highest_count) for index, kiddo in enumerate(candies)]
    
    # return results
   
    # (someone else's version—does not naming vars save time a/o memory?) 
    return[x+extraCandies>=max(candies) for x in candies]

# ============================
# tests
# ============================

print(kidsWithCandies([2, 3, 5, 1, 3], 3))     # [t, t, t, f, t]
print(kidsWithCandies([4, 2, 1, 1, 2], 1))     # [t, f, f, f, f]
print(kidsWithCandies([12, 1, 12], 10))        # [t, f, t]