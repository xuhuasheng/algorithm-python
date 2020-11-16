def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid
    return -1

# 若有重复元素 则返回重复元素左边界(左侧的第一个元素)的索引
#     0  1  2  3
# 如 [0, 2, 2, 4] 
# target=2,   返回索引1
# target= 1, 虽然不存在, 但返回索引1, 即大于等于target的最小的元素位置
# target= 3, 虽然不存在, 但返回索引3, 即大于等于target的最小的元素位置
# target=-1, 虽然不存在, 但返回索引0, 即大于等于target的最小的元素位置
# target= 5, 虽然不存在, 但返回索引len(nums), 该索引越上界
def left_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            right = mid - 1
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

# 变种
def left_bound_(nums, target):
    left = 0
    right = len(nums)
    # 左闭右开 [left, right)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] == target:
            right = mid
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

# 若有重复元素 则返回重复元素右边界(右侧的最后一个元素)的索引
#     0  1  2  3
# 如 [0, 2, 2, 4] 
# target=2,  返回索引2
# target=3, 虽然不存在, 但返回索引2, 即小于等于target的最大的元素位置
# target=1, 虽然不存在, 但返回索引0, 即小于等于target的最大的元素位置
# target=-1, 虽然不存在, 但返回索引-1, 该索引越下界
# target= 5, 虽然不存在, 但返回索引3, 即小于等于target的最大的元素位置
def right_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            left = mid + 1
    if right < 0 or nums[right] != target:
        return -1
    return right

# 变种
def right_bound_(nums, target):
    left = 0
    right = len(nums)
    # 左闭右开 [left, right)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] == target:
            left = mid + 1
    if right < 0 or nums[right-1] != target:
        return -1
    return right-1
    
    