class Solution(object):
    def robotSim(self, commands, obstacles):
        direction_set = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = 0, 0
        direction = 0

        # Convert list obstacles to set with tuple
        obstacles = set(map(tuple, obstacles))

        max_distance = 0

        for com in commands:
            if com == -1:
                direction = (direction + 1) % 4
            elif com == -2:
                direction = (direction - 1) % 4
            else:
                distance = com
                for i in range(distance):
                    if (x + direction_set[direction][0], y + direction_set[direction][1]) not in obstacles:
                        x += direction_set[direction][0]
                        y += direction_set[direction][1]
                        max_distance = max(max_distance, x**2 + y**2)
                    else:
                        break

        return max_distance

if __name__ == "__main__":
    print(Solution().robotSim([4,-1,4,-2,4], [[2,4],[1,2]]))