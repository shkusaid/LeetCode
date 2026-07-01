# _________________ BRUTE FORCE APPROACH _____________________

# def product_subarray(nums):
#     max_product = -10 # as numbers are 32-bits according to constraint
#     for i in range(len(nums)):
#         product = 1
#         for j in range(i , len(nums)):
#             product *= nums[j]
#             max_product = max(max_product , product)
#     return max_product


# _____________________ OPTIMAL APPROACH ___________________

def product_subarray(nums):
    prefix = 1
    suffix = 1
    max_product = -10
    for i in range(len(nums)):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[len(nums) - i - 1]
        max_product = max(max_product , max(suffix , prefix))   

    return max_product

arr = [2,3,-2,4]
print(product_subarray(arr))