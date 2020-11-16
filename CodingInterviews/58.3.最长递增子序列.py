import sys
# https://blog.csdn.net/qq_41765114/article/details/88415541
# 时间复杂度：o(n^2)
# dp[n] 当前以第n个字符结尾的字符串的最长递增子序列长度
def LIS(arr):
    # dp = [1]*len(arr)
    dp = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

import bisect
def deal(arr):
    d = []
    count = []
    for val in arr:
        if not d: # 选中队列中的一个学生，以该学生为核心
            d.append(val)
            count.append(1)
        elif d[-1] < val:
            d.append(val)
            count.append(count[-1]+1)
        else:
            d[bisect.bisect_left(d, val)] = val
            count.append(count[-1])
    return count
# // 二分查找变体 找到第一个大于n的位置index 
# int BinarySearch(int *dp, int len, int n){
# 	int left = 1;
# 	int right = len;
# 	while(left < right){
# 		int mid = (left+right)/2;
# 		if(dp[mid] > n){
# 			right = mid;
# 		}
# 		else{
# 			left = mid+1;
# 		}
# 	}
# 	return right;
# }

# // 优化的dp dp数组的最终下标为答案 
# int getResult1(int n){
# 	 dp[1] = arr[0];
# 	 int index = 1;
# 	 for(int i = 1; i < n; i++){
# 	 	if(arr[i] > dp[index]){
# 	 		// 更新index 
# 	 		dp[++index] = arr[i];
# 		 }
# 		 else{
# 		 	// 把dp数组中第一个大于n的数字替换为arr[i] 
# 		 	int tempIndex = BinarySearch(dp, index, arr[i]);
# 		 	dp[tempIndex] = arr[i];
# 		 }
# 	 }
# 	 return index;

if __name__ == "__main__":
    # # 打开输入文件
    # f = open("0.inputfile.txt", "r")
    # # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    # sys.stdin = f
    # arr = list(map(int, input().split(' '))
    arr = [1, 7, 3, 5, 9, 4, 8]
    print(LIS(arr))
