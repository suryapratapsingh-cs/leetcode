class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        
        for word in words:
            # Calculate total weight of the word
            weight_sum = sum(weights[ord(char) - ord('a')] for char in word)
            
            # Map the modulo result to reverse alphabetical order (0 -> 'z', 1 -> 'y', ...)
            mapped_char = chr(ord('z') - (weight_sum % 26))
            res.append(mapped_char)
            
        return "".join(res)
