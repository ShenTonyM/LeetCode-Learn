class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = dict()

        num = len(position)

        count = 0
        for i in range(num):
            this_position = position[i]
            this_speed = speed[i]
            this_time = (target - this_position) / this_speed
            flag = True
            for element in cars:
                if (cars[element]['position'] <= this_position and cars[element]['time'] <= this_time) \
                        or (cars[element]['position'] >= this_position and cars[element]['time'] >= this_time):
                    flag = False
                    break
            cars[i] = dict()
            cars[i]['position'] = this_position
            cars[i]['time'] = this_time

            if flag:
                count += 1
            # print(cars)

        return count

if __name__ == '__main__':
    print(Solution().carFleet(10,[0,4,2],[2,1,3]))
