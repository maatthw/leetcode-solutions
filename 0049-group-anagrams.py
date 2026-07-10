def groupAnagrams(strs):
    # We'll use a dictionary where the key is a sorted string and the value is a list of valid anagrams

    anagram_groups = {}

    for s in strs:
        # First we sort the string and then we see if it is already a key in the dict
        key = "".join(sorted(s))

        if key in anagram_groups:
            anagram_groups[key].append(s)
        else:
            anagram_groups[key] = [s]

    v = [value for value in anagram_groups.values()]
    return v

# Time Complexity  : O(n)
# Space Complexity : O(n)