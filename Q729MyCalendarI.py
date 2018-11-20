# class MyCalendar1(object):
#     def __init__(self):
#         self._book_time = []
#
#     def book(self, start, end):
#         """
#         :type start: int
#         :type end: int
#         :rtype: bool
#         """
#
#         for prev_book in self._book_time:
#             if (start >= prev_book[0] and start < prev_book[1]) or (end > prev_book[0] and end <= prev_book[1])\
#                     or (start < prev_book[0] and end > prev_book[1]):
#                 return False
#
#         self._book_time.append([start, end])
#         return True




class Node(object):
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
        self.__left = None #两个指针，指向相邻的节点
        self.__right = None

    def insert(self, node):
        if node.__end <= self.__start:
            if not self.__left:
                self.__left = node
                return True
            else:
                return self.__left.insert(node)
        elif node.__start >= self.__end:
            if not self.__right:
                self.__right = node
                return True
            else:
                return self.__right.insert(node)
        else:
            return False


class MyCalendar2(object):
    def __init__(self):
        self.__root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if not self.__root:
            self.__root = Node(start, end)
            return True
        else:
            new_node = Node(start, end)
            return self.__root.insert(new_node)


# class Node(object):
#     def __init__(self, start, end):
#         self.__start = start
#         self.__end = end
#         self.__left = None
#         self.__right = None
#
#
#     def insert(self, node):
#         if node.__start >= self.__end:
#             if not self.__right:
#                 self.__right = node
#                 return True
#             return self.__right.insert(node)
#         elif node.__end <= self.__start:
#             if not self.__left:
#                 self.__left = node
#                 return True
#             return self.__left.insert(node)
#         else:
#             return False
#
#
# class MyCalendar(object):
#     def __init__(self):
#         self.__root = None
#
#
#     def book(self, start, end):
#         """
#         :type start: int
#         :type end: int
#         :rtype: bool
#         """
#         if self.__root is None:
#             self.__root = Node(start, end)
#             return True
#
#         print(self.__root)
#         return self.__root.insert(Node(start, end))




if __name__ == '__main__':
    obj = MyCalendar2()
    print(obj.book(47, 50))
    print(obj.book(33, 41))
    print(obj.book(39, 45))
    print(obj.book(33, 42))
    print(obj.book(25, 32))

