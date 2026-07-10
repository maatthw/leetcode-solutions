def lengthOfLongestSubstring(s):
    max_length = 0
    left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Time Complexity  : O(n)
# Space Complexity : O(min(n, m)) -> Seen stores characters. There are only so many possible characters that exist.
    # Thus, the size of seen is at worst, m, which is the size of the character set.
    # Character set could be all lowercase letters, all uppercase and lowercase, all ASCII, all Unicode (1m+), a combination, or god knows what else
    # Based on the constraint of this problem: "s consists of English letters, digits, symbols, and spaces", it is reasonable to assume a character set of 128 (ASCII)
    # Thus, the space complexity would really be O(min(n, 128)) which resolves to O(1) since for large values of n our function never exceeds 128
    # O(1) would be the more "precise" answer given the constraints, but O(min(n, m)) is a more general answer for broader constraints that could be applied to this problem