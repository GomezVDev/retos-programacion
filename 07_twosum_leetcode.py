"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ 
        Runtime : 38ms

        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    suma = nums[x] + nums[y]
                    if suma == target:
                        return [x,y]
                    else:
                        suma = 0

        """
        #CHATGPT me sugirio calcular el len antes, efectivamente el Runtime fue menor
        nums_len = len(nums)
        for x in range(nums_len):
            for y in range(x+1,nums_len): #X+1 Ya que si en el primer ciclo ese numero no pudo "ayudar" con la suma, tampoco lo hara despues.
                    suma = nums[x] + nums[y]
                    if suma == target:
                        return [x,y]
                    else:
                        suma = 0
