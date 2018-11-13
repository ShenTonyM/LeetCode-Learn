class Solution(object):
    # PART 1: Build a tree
    def get_level(self, item):
        return len(item) - len(item.lstrip('\t'))

    def fill_out_tree(self, root, items, cur_level):
        global i
        while i < len(items) and cur_level == self.get_level(items[i]):
            item_name = items[i].lstrip('\t')
            i += 1
            if '.' in item_name:
                root[item_name] = '#'
            else:
                root[item_name] = {}
                self.fill_out_tree(root[item_name], items, cur_level + 1)

    # PART 2: Find longest path (DFS)
    def max_len_path(self, node, len_so_far):
        if len(node) == 0:
            return 0
        else:
            max_len = 0
            for child_name in node:
                if "#" in node[child_name]:
                    max_len = max(max_len, len_so_far + len(child_name))
                else:
                    max_len = max(max_len, self.max_len_path(node[child_name], len_so_far + len(child_name) + 1))
            return max_len



    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        items = input.split('\n')  # item can be either a file or a folder

        global i  # to make i persistent
        i = 0
        root = {}

        self.fill_out_tree(root, items, 0)
        print(root)
        return self.max_len_path(root, 0)







if __name__ == '__main__':
    print(Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")