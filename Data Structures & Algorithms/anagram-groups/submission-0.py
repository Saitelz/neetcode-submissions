class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vocab = {}

        for w in strs:
            hash_w = "".join(sorted(w))

            vocab[hash_w] = vocab.get(hash_w, []) + [w]
        
        return list(vocab.values())