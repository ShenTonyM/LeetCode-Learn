class ReplaceItem:
    def __init__(self, index, source, target):
        self.index = index
        self.source = source
        self.target = target




class Solution:
    def findReplaceString(self, S: str, indexes, sources, targets) -> str:
        replace_items = []
        for i in range(len(indexes)):
            item = ReplaceItem(indexes[i], sources[i], targets[i])
            replace_items.append(item)

        replace_items = sorted(replace_items, key=lambda x:x.index, reverse=True)


        for item in replace_items:
            index = item.index
            source_str = item.source
            target_str = item.target

            source_len = len(source_str)

            if S[index:index + source_len] == source_str:
                S = S[:index] + target_str + S[index+source_len:]

        return S




if __name__ == "__main__":
    print(Solution().findReplaceString("abcd",[0, 2],["a", "cd"],["eee", "ffff"]))