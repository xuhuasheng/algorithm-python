# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。

#  

# 示例 1:

# nums1 = [1, 3]
# nums2 = [2]

# 则中位数是 2.0
# 示例 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# 则中位数是 (2 + 3)/2 = 2.5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 法1：暴力合并取中位数
# space:    o(m+n)
# time:     o(m+n)
class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        k = (len(num1) + len(num2) + 1) // 2
        res = []
        while len(num1) > 0 and len(num2) > 0:
            if num1[0] <= num2[0]:
                res.append(num1.pop(0))
            else:
                res.append(num2.pop(0))
        res += num1
        res += num2
        if len(res) & 1 == 0:
            return (res[k-1] + res[k]) /2
        else:
            return res[k-1]

# 法2：非合并，双指针遍历(m+n)/2+1次，取中位数
# space:    o(m+n)
# time:     o(1)
# length = m+n, 
# if length % 2 == 1:
#   mid = arr[lenght//2+1]
# else:
#   mid = ( arr[length//2] + arr[length//2 + 1] ) / 2
# 将奇偶数的情况合并，即遍历次数都得是length//2 + 1
class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        m = len(num1)
        n = len(mun2)
        length = m+n
        prevMid, curMid = -1, -1
        p1, p2 = 0, 0
        for i in range(length//2+1):
            prevMid = curMid
            if p1 < m and (p2 >= n or num1[p1] < num2[p2]) :
                curMid = num1[p1]
                p1 += 1
            else:
                curMid = num2[p2]
                p2 += 1
        if length & 1 == 0:
            return (prevMid + curMid) / 2.0
        else:
            return float(curMid)

class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        m = len(num1)
        n = len(num2)
        if m > n:
            return self.findMedianSortedArrays(num2, num1)
        
        totalLeft = (m+n+1)//2
        iLeft, iRight = 0, m

        while iLeft < iRight:
            i = iLeft + (iRight-iLeft)//2
            j = totalLeft - i
            if num1[i] < num2[j-1]:
                iLeft = i+1
            else:
                iRight = i
        
        i = iLeft
        j = totalLeft - i
        nums1LeftMax = -float('inf') if (i==0) else num1[i-1]
        nums1RightMin = float('inf') if (i==m) else num1[i]
        nums2LeftMax = -float('inf') if (j==0) else num2[j-1]
        nums2RightMin = float('inf') if (j==n) else num2[j]

        if (m+n) & 1 == 1:
            return float(max(nums1LeftMax, nums2LeftMax))
        else:
            return float((max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2)
