""" by 紫玉 """
# def robotSim(commands, obstacles):
#     """
#     :type commands: List[int]
#     :type obstacles: List[List[int]]
#     :rtype: int
#     """
#     x = 0
#     y = 0
#     max = 0
#     # loction = [x,y]
#     direct_num = 1
#     # 面向+Y方向
#     # direct_num += 1
#     # direction = direct_num % 4
#     # print(direction)
#     for each in commands:
#         if each == -1:
#             direct_num -= 1
#         elif each == -2:
#             direct_num += 1
#         else:
#             if direct_num % 4 == 0:
#                 #               +X方向
#                 for tem in range(each):
#                     if [x + 1, y] not in obstacles:
#                         x += 1
#                     # else:
#                     #     print(x+1, y, "blocked at:", each)
#
#
#             elif direct_num % 4 == 1:
#                 #               +Y方向
#                 for tem in range(each):
#                     if [x, y + 1] not in obstacles:
#                         y += 1
#                     # else:
#                     #     print(x, y + 1, "blocked at:",each)
#
#             elif direct_num % 4 == 2:
#                 #               -X方向
#                 for tem in range(each):
#                     if [x - 1, y] not in obstacles:
#                         x -= 1
#                     # else:
#                     #     print(x-1, y, "blocked at :",each)
#
#             elif direct_num % 4 == 3:
#                 #               -Y方向
#                 for tem in range(each):
#                     if [x, y - 1] not in obstacles:
#                         y -= 1
#                     # else:
#                     #     print(x,y-1,"blocked at : ",each)
#
#         # print("at:",x,y)
#         tem = x ** 2 + y ** 2
#         if tem > max:
#             max = tem
#     return max

class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        print(obstacleSet)
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans


if __name__ == "__main__":
    print(Solution().robotSim([4,-1,4,-2,4], [[2,4],[1,2]]))