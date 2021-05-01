#My Solution
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        large = 0
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
                if large < dic[nums[i]]:
                    key = nums[i]
                    large = dic[nums[i]]
            else:
                dic[nums[i]] = 1
                if large < dic[nums[i]]:
                    key = nums[i]
                    large = dic[nums[i]]
        return key


#Better Solutions
class Solution(object):
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
    def majorityElement2(self, nums):
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
            if m[n] > len(nums)//2:
                return n
            
    def majorityElement(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate
