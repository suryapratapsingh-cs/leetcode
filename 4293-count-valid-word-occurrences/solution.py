import re
from collections import Counter

class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        # Concatenate strings: O(N) where N is total length of chunks
        s = "".join(chunks)
        
        # Regex for valid words: O(N)
        # Matches lowercase letters with optional single hyphens between them
        pattern = re.compile(r'[a-z]+(?:-[a-z]+)*')
        
        # Count occurrences directly from the iterator to save memory
        word_counts = Counter(match.group() for match in pattern.finditer(s))
        
        # O(Q) where Q is number of queries
        return [word_counts[q] for q in queries]
