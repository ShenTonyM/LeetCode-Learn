class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s_data = S.split('-')
        s_raw = "".join(s_data)

        first_len = len(s_raw) % K

        res = ""
        if first_len != 0:
            res += s_raw[:first_len].upper() + "-"

        for i in range(first_len, len(s_raw) - first_len, K):
            res +=  s_raw[i:i+K].upper() + "-"

        return res[:-1]

if __name__ == "__main__":
    print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))