class Solution(object):
    def rearrangeArray(self, nums):
        
        # Separate positive and negative numbers
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        
        result = []
        i, j = 0, 0
        
        # Interleave positive and negative numbers
        while i < len(positive) and j < len(negative):
            result.append(positive[i])
            result.append(negative[j])
            i += 1
            j += 1
        
        # Add remaining elements
        result.extend(positive[i:])
        result.extend(negative[j:])
        
        # Ensure the rearranged array starts with a positive integer
        if result[0] < 0:
            # Swap the first positive and negative integers
            for k in range(len(result)):
                if result[k] > 0:
                    result[0], result[k] = result[k], result[0]
                    break
        
        return result