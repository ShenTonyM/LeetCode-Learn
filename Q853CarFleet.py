class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        times = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        print([[p, s] for p, s in sorted(zip(position, speed))])
        print(times)
        result, curr = 0, 0
        for t in reversed(times):
            if t > curr:
                result += 1
                curr = t
        return result

if __name__ == '__main__':
    print(Solution().carFleet(10,[0,4,2],[2,1,3]))
