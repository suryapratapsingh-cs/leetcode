class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Keep track of the last index where each character appears
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            # If the character is already in our stack, we don't need it again
            if char in seen:
                continue
            
            # If the current character is smaller than the last character in the stack,
            # and the last character in the stack appears again later in the string,
            # we can safely remove it from the stack to get a lexicographically smaller result.
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                seen.remove(stack.pop())
            
            # Add the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
