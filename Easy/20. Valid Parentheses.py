class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        if len(s) % 2 == 1:
            return False
        for char in s:
            if char in mapping: # Check if the character is one of the closing brackets
                top_element = stack.pop() if stack else '#' 
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))  # False
    print(s.isValid("([)]"))  # False
    print(s.isValid("{[]}"))  # True