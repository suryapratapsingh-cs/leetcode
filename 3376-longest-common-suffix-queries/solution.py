class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the index of the optimal word passing through / ending at this node
        self.best_idx = -1 

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        # Helper to check if current index is better than the existing best index
        def get_better_index(idx1, idx2):
            if idx1 == -1: return idx2
            if idx2 == -1: return idx1
            len1, len2 = len(wordsContainer[idx1]), len(wordsContainer[idx2])
            if len1 != len2:
                return idx1 if len1 < len2 else idx2
            return idx1 if idx1 < idx2 else idx2

        # 1. Build the Trie
        for i, word in enumerate(wordsContainer):
            curr = root
            curr.best_idx = get_better_index(curr.best_idx, i)
            
            # Traverse/insert the word in reverse order (suffix -> prefix)
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                curr.best_idx = get_better_index(curr.best_idx, i)
                
        # 2. Process Queries
        ans = []
        for query in wordsQuery:
            curr = root
            # Follow the reversed query string as far as possible
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_idx)
            
        return ans
