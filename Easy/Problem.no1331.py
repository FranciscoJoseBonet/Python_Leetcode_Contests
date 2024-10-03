'''
Rank Transform of an array

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_arr = sorted(list(set(arr)))
        rank_dict = {val: i + 1 for i, val in enumerate(unique_arr)}
        return [rank_dict[val] for val in arr]