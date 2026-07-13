class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        common_array = []
        len1,len2 = len(nums1),len(nums2)
        i,j = 0,0

        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                common_array.append(nums1[i])
                i += 1
            else:
                common_array.append(nums2[j])
                j += 1
        

        while i < len1:
            common_array.append(nums1[i])
            i += 1
        
        while j < len2:
            common_array.append(nums2[j])
            j += 1


        half = len(common_array)//2
        if len(common_array)%2==0:
            return (common_array[half]+common_array[half-1])/2
        else:
            return float(common_array[len(common_array)//2])

        
