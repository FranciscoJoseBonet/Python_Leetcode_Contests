'''
Check if array pairs are divisible by k

Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
Return true If you can find a way to do that or false otherwise.
'''

class Solution:
    def canArrange(self, arr: list, k: int) -> bool:
        countRest = [0] * k
        
        for num in arr:
            div = num % k
            countRest[div] += 1
        
        if countRest[0] % 2 != 0:    # Si los números que son divisibles por k no son pares no se pueden emparejar
            return False

        for i in range(1, (k // 2) + 1):
            if countRest[i] != countRest[k - i]:    # Si no existe la misma cantidad de números con restos complementarios 
                return False                        # no es posible agrupar en pares divisibles por k
        
        return True
