class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocab_s = {}
        vocab_t = {}
        for l in s:
            vocab_s[l] = vocab_s.get(l, 0) + 1

        for l in t:
            vocab_t[l] = vocab_t.get(l, 0) + 1

        return vocab_s == vocab_t