from typing import List
def productExcetSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    out2 = []
    for i in range(len(nums) - 1, 0 - 1, -1):
        print(p)
        out2.append(p)
        p = p * nums[i]

    print(out)
    print(out2)

nums = list(map(int, input().split()))
productExcetSelf(nums)