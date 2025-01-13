class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            char = nums[i]
            hashmap[char] = hashmap.get(char, 0) + 1
        
        valuemax = max(hashmap.values())  # gets ans
        keymax = max(hashmap, key=hashmap.get)  # gets 'num'
        print(keymax)
        return keymax