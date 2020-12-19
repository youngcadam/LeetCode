class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ctr = 0
        dic = {}
        for num in nums:
            complement = target - num
            if complement in dic:
                return [dic[complement], ctr]
            dic.update({num: ctr})
            ctr += 1