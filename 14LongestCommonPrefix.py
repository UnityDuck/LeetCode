# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        prefix_length = len(shortest_str)
        
        for i in range(prefix_length):
            current_char = shortest_str[i]
            for string in strs:
                if string[i] != current_char:
                    return shortest_str[:i]
        
        return shortest_str