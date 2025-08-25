class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        tempMap = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}
        rMap = {}
        for key, value in tempMap.items():
            for v in value:
                rMap[v] = key

        ans = []
        for word in words:
            curRow = rMap[word[0].lower()]
            for i in range(1, len(word)):
                if rMap[word[i].lower()] != curRow:
                    break
            else:
                ans.append(word)

        return ans


        