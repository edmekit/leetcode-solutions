def solution(nums,target):
    numbers = {}
    for i, value in enumerate(nums):
        diff = target - value
        if diff in numbers:
            return [numbers[diff], i]
        numbers[value] = i

def merdian(nums1, nums2):
    merged_array = (nums1 + nums2)
    merged_array.sort()
    length = len(merged_array)
    if length % 2 == 0:
        return (merged_array[(length // 2) - 1] + merged_array[(length // 2)]) / 2
    else:
        return merged_array[length // 2]

def isPalindrome(x):
    word_x = str(x)
    new_x = word_x[::-1]
    if new_x == word_x:
        return True
    else:
        return False

