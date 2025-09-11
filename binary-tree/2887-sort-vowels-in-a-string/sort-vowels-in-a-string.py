class Solution:
    def sortVowels(self, s: str) -> str:
        st = "AEIOUaeiou"
        # print(sorted(st))
        sList = list(s)
        vowels = []
        pos = []
        for i, c in enumerate(sList):
            if c in st:
                vowels.append(c)
                pos.append(i)

        vowels.sort()
        for i in range(len(pos)):
            sList[pos[i]] = vowels[i]

        return "".join(sList)

        