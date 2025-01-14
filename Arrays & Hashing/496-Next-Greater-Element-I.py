class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hash_map = {}
        result = [-1] * len(nums1)
        hash_map = {value: index for index, value in enumerate(nums1)}

        for n1 in range(len(nums2)):
            if nums2[n1] not in hash_map:
                continue
            for n2 in range(n1+1, len(nums2)):
                if nums2[n2] > nums2[n1]:
                    index = hash_map[nums2[n1]]
                    result[index] = nums2[n2]
                    break
        print(result)
        return result
