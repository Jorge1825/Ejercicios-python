class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for i in s:
            if i == "I":
                num += 1
            elif i == "V":
                num += 5

            elif i == "X":
                num += 10

            elif i == "L":
                num += 50
            elif i == "C":
                num += 100
            elif i == "D":
                num += 500
            else:
                num += 1000

        return num


num = Solution()
print(num.romanToInt("III"))
1900