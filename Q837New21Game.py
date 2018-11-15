class Solution(object):
    def new21Game(self, N, K, W):

        if K == 0 or N >= K + W:
            return 1

        dp = [0] * (N + 1)

        result = 0
        previous_sum = 0

        for i in range(1, N + 1):
            if i <= W:
                dp[i] = previous_sum / W + 1 / W
            else:
                dp[i] = previous_sum / W

            # 超过K就不能再取了
            if i < K:
                previous_sum += dp[i]

            # 只维护最近K个数
            if i > W:
                previous_sum -= dp[i - W]

            # 最终的输出在[K, N] 都符合条件
            if i >= K:
                result += dp[i]

        return result


if __name__ == "__main__":
    print(Solution().new21Game(10,1,10))