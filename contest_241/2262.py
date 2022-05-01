class Solution:

    def appealSum(self, s: str) -> int:
        a = 1
        l = [s[0]]
        r = [1]
        for c in s[1:]:
            if c in l:
                i = l.index(c)
                del l[i]
                l.append(c)
                t = r[i]
                del r[i]
                r.append(1)
                r[i] += t
            else:
                l.append(c)
                r.append(1)
            a += sum([i * c for i, c in zip(r, list(range(len(r), 0, -1)))])
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.appealSum(s='abbca'))
    print(solution.appealSum(s='code'))
