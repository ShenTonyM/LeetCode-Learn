def findLongest(arr):
    length = len(arr)
    max_length = 0
    for i in range(length):
        for j in range(length):
            path = []
            path.append((i, j))
            visited = []
            visited.append((i, j))
            while path:
                cur_posi = path[-1]
                if cur_posi[1] + 1 < length and (cur_posi[0], cur_posi[1] + 1) not in visited and arr[cur_posi[0]][
                            cur_posi[1] + 1] > arr[cur_posi[0]][cur_posi[1]]:
                    cur_posi = (cur_posi[0], cur_posi[1] + 1)
                    path.append(cur_posi)
                    visited.append(cur_posi)
                    continue
                elif cur_posi[1] - 1 >= 0 and (cur_posi[0], cur_posi[1] - 1) not in visited and arr[cur_posi[0]][
                            cur_posi[1] - 1] > arr[cur_posi[0]][cur_posi[1]]:
                    cur_posi = (cur_posi[0], cur_posi[1] - 1)
                    path.append(cur_posi)
                    visited.append(cur_posi)
                    continue
                elif cur_posi[0] - 1 >= 0 and (cur_posi[0] - 1, cur_posi[1]) not in visited and arr[cur_posi[0] - 1][
                    cur_posi[1]] > arr[cur_posi[0]][cur_posi[1]]:
                    cur_posi = (cur_posi[0] - 1, cur_posi[1])
                    path.append(cur_posi)
                    visited.append(cur_posi)
                    continue
                elif cur_posi[0] + 1 < length and (cur_posi[0] + 1, cur_posi[1]) not in visited and \
                                arr[cur_posi[0] + 1][cur_posi[1]] > arr[cur_posi[0]][cur_posi[1]]:
                    cur_posi = (cur_posi[0] + 1, cur_posi[1])
                    path.append(cur_posi)
                    visited.append(cur_posi)
                    continue
                else:
                    length1 = len(path)
                    if length1 > max_length:
                        max_length = length1
                    path.pop()

    return max_length


input_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = findLongest(input_array)
print(ans)
