class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_product = []
        l_product = []
        result = []
        
        product = nums[0]
        r_product.append(product)
        for n in nums[1:]:
            product *= n
            r_product.append(product)

        product = nums[-1]
        l_product.append(product)
        for n in nums[-2::-1]:
            product *= n
            l_product.append(product)
        l_product = l_product[::-1]

        for i, n in enumerate(nums):
            if i == 0:
                result.append(l_product[i+1])
            elif i == len(nums)-1:
                result.append(r_product[i-1])
            else:
                result.append(r_product[i-1] * l_product[i+1])

        return result