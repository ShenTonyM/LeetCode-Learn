if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split(' ')))
    if len(array) != n:
        print(0)
    if len(set(array)) <3:
        print(-1)
    else:
        s = sorted(set(array))
        print(s[2])