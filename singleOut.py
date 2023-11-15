class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 4 1 2 2 1
        # 100 001 010 010 001
        val = nums[0]
        for i in range(1, len(nums)):
            val = val ^ nums[i]

        return val


if __name__ == "__main__":
    obj = Solution()
    nums = [4,1,2,1,2]
    x  = obj.singleNumber(nums)
    print(x)