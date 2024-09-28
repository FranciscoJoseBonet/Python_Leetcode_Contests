'''
MAXIMIZE THE TOTAL HEIGHT OF UNIQUE TOWERS

You are given an array maximumHeight, where maximumHeight[i] denotes the maximum height the ith tower can be assigned.
Your task is to assign a height to each tower so that:
The height of the ith tower is a positive integer and does not exceed maximumHeight[i].
No two towers have the same height.
Return the maximum possible total sum of the tower heights. If it's not possible to assign heights, return -1
'''




from collections import Counter

class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        # Count the freq of the values in maximumHeight
        counts = Counter(maximumHeight)
        
        # Order by descending values
        sorted_counts = sorted(counts.items(), key=lambda x: x[0], reverse=True)        # sorted(what we order, in base of which parameter, orientation)

        used_numbers = set()
        result_sum = 0

        for number, count in sorted_counts:
            current_value = number

            for _ in range(count):
                
                # Search for the current_value (number) in used_numbers, if we found it and it's higher than zero, we decrease it in one
                # Condition 1
                while current_value in used_numbers and current_value > 0:
                    current_value -= 1

                # Condition 2
                if current_value == 0:
                    return -1

                # Condition 3: The number meets all the requirments
                
                # We add the number to our set
                used_numbers.add(current_value)
                result_sum += current_value

        return result_sum

# Ejemplo de uso
# sol = Solution()
# maximumHeight = [3, 3, 3, 2, 2, 1]
# print(sol.maximumTotalSum(maximumHeight))  # Ejemplo de salida