

def devowel(word: str) -> str:
    return ''.join('*' if c.lower() in "aeiou" else c.lower() for c in word)

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)  # exact matches
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()
            mask = devowel(word)

            if lower not in case_map:   # first occurrence
                case_map[lower] = word
            if mask not in vowel_map:   # first occurrence
                vowel_map[mask] = word

        ans = []
        for q in queries:
            if q in words:  # exact
                ans.append(q)
            elif q.lower() in case_map:  # case-insensitive
                ans.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:  # vowel-error
                ans.append(vowel_map[devowel(q)])
            else:
                ans.append("")  # no match
        return ans
