from typing import List
from queue import SimpleQueue


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ns = len(s); nm = len(words); lm = len(words[0])
        d = {}
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        l = []
        for i in range(lm):
            l += [j * lm + i for j in self.find(s[i:ns - (ns - i) % lm], nm, lm, d)]
        return l

    def find(self, s, nm, lm, d):
        s = [s[i * lm:(i + 1) * lm] for i in range(len(s) // lm)]
        b = {k:SimpleQueue() for k in d}
        cs = 0
        l = []
        for i, w in enumerate(s):
            if w not in d:
                for j in range(cs, i):
                    b[s[j]] = SimpleQueue()
                cs = i + 1
            else:
                bw = b[w]; dw = d[w]
                bw.put(i)
                if bw.qsize() == dw:
                    if cs + nm - 1 == i:
                        l.append(cs)
                        b[s[cs]].get(False)
                        cs += 1
                elif bw.qsize() > dw:
                    i = bw.get(False)
                    for j in range(cs, i):
                        b[s[j]].get(False)
                    cs = i + 1
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstring(s='barfoothefoobarman', words=['foo','bar']))
    print(solution.findSubstring(s='wordgoodgoodgoodbestword', words=['word','good','best','word']))
    print(solution.findSubstring(s='barfoofoobarthefoobarman', words=['bar','foo','the']))
    print(solution.findSubstring(s='lingmindraboofooowingdingbarrwingmonkeypoundcake', words=['fooo','barr','wing','ding','wing']))
