

def GetUglyNumber_Solution(index):
        # write code here
        if index == 0:
            return 0
        dp = [0] * index
        a,b,c = 0,0,0
        dp[0] = 1
        for i in range(1,index):
            n2,n3,n5 = dp[a] * 2,dp[b] * 3,dp[c] * 5
            dp[i] = min(n2,n3,n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[index-1]