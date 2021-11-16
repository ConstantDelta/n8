from random import randint
k = int(input())
nums = [randint(0, 20) for i in range(randint(k, k+20))]
print(nums)
def kbig(nums, k):
  while (k != 0):
    max_nums = max(nums)
    nums.remove(max_nums)
    k -= 1
  return max_nums

print(kbig(nums, k))