def productExceptSelf(nums: List[int]) -> List[int]:
    product = []
    for i, num in enumerate(nums):
        a = nums[:i]
        b = nums[i+1:]
        c = a + b
        prod = 1
        for d in c:
            prod *= d
        product.append(prod)
    return product

print(productExceptSelf([1,2,4,6]))