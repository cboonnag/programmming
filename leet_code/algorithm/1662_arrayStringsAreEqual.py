class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s = ""
        word1 = s.join(word1)
        word2 = s.join(word2)
        
        return word1 == word2