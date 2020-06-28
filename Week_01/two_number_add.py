class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        same_list = []
        old_nums = nums[:]
        nums.sort()
        j = len(nums) - 1
        for i in range(len(nums)):
            while i != j:
                if (nums[i] + nums[j]) > target:
                    j -= 1
                if (nums[i] + nums[j]) < target:
                    i += 1              
                if nums[i] + nums[j] == target:
                    if old_nums.index(nums[i]) == old_nums.index(nums[j]):
                        for key, value in enumerate(old_nums):
                            if value == nums[i]:
                                same_list.append(key)
                        return same_list
                    return [old_nums.index(nums[i]), old_nums.index(nums[j])]
