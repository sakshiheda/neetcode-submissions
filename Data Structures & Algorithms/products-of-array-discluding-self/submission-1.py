class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_prod = 1
        count_0 = []
        for i in range(len(nums)): 
            if nums[i] != 0:
                full_prod *= nums[i]
            else: count_0.append(i)
        if len(count_0) > 1: return [0]*len(nums)
        if len(count_0) == 1:
            output = [0]*len(nums)
            output[count_0[0]] = full_prod
            return output
        output = [full_prod]*len(nums)
        for i in range(len(nums)): output[i] //= nums[i]
        return output