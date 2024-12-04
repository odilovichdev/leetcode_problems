from typing import List


# def rotate(nums: List[int], k: int):
# 1-chi usul
#     n = k%len(nums)
#     if n!=0:
#         nums[:] = nums[-n:]+nums[:-n]


def rotate(nums:List[int], k: int):
    # 2-chi usul
    n = k % len(nums)
    if n!=0:
        arr = [0] * len(nums)
        for i in range(len(nums)):
            arr[(i + n) % len(nums)] = nums[i]

        nums[:] = arr



nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums, k)