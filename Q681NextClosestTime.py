class Solution:

    def isvalid(self, data):
        if data[0] * 10 + data[1] > 23 or data[0] * 10 + data[1] < 0:
            return False
        if data[2] * 10 + data[3] > 59 or data[2] * 10 + data[3] < 0:
            return False

        return True

    def distance_cal(self, data_0, data_1):
        total_time = 24 * 60

        diff_time = (10 * data_0[0] + data_0[1] - 10 * data_1[0] - data_1[1]) * 60 + \
                    (10 * data_0[2] + data_0[3] - 10 * data_1[2] - data_1[3])

        if diff_time < 0:
            diff_time = total_time + diff_time
        return diff_time

    def nextClosestTime(self, time: str) -> str:
        nums = []
        nums.append(int(time[0]))
        nums.append(int(time[1]))
        nums.append(int(time[3]))
        nums.append(int(time[4]))

        min_time = 24 * 60 + 1
        res = time

        for num_0 in nums:
            for num_1 in nums:
                for num_2 in nums:
                    for num_3 in nums:
                        data_0 = [num_0, num_1, num_2,num_3]
                        data_1 = nums
                        if self.isvalid(data_0):
                            diff_time = self.distance_cal(data_0, data_1)
                            if diff_time != 0 and diff_time < min_time:
                                res = str(num_0) + str(num_1) + ":" + str(num_2) + str(num_3)
                                min_time = diff_time

        return res
if __name__ == "__main__":
    print(Solution().nextClosestTime("19:34"))
