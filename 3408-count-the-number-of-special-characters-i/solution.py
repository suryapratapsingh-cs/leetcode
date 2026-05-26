class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return len(set(word) & set(word.swapcase()) & set("abcdefghijklmnopqrstuvwxyz"))
