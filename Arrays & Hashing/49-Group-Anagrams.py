class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            # Sort each word to use as a key
            sorted_word = ''.join(sorted(word))

            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]
        return list(anagram_map.values())
'''
aet
aet
ant
aet
ant
abt
'''