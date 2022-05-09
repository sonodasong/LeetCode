from typing import List


class Solution:

    def __init__(self):
        t = {}
        t['2'] = ['a', 'b', 'c']
        t['3'] = ['d', 'e', 'f']
        t['4'] = ['g', 'h', 'i']
        t['5'] = ['j', 'k', 'l']
        t['6'] = ['m', 'n', 'o']
        t['7'] = ['p', 'q', 'r', 's']
        t['8'] = ['t', 'u', 'v']
        t['9'] = ['w', 'x', 'y', 'z']
        self.table = t

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        if len(digits) == 1: return self.table[digits[0]]
        l = []
        for t in self.letterCombinations(digits[:-1]):
            for c in self.table[digits[-1]]:
                l.append(t + c)
        return l



if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations(digits='23'))
