# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr = 0
        right_ptr = 0
        unique_symbols = dict()
        best_length = 0

        for symbol in s:
            if symbol in unique_symbols:
                # set left_ptr of the window to the previous+1 position
                previous_entrance = unique_symbols[symbol]
                left_ptr = previous_entrance + 1

                # remove from dict of last entrances everything what is lefter than left_ptr
                for x in unique_symbols.copy():
                    if unique_symbols[x] < left_ptr:
                        unique_symbols.pop(x, None)

            # update where last entrance of current symbol is
            unique_symbols[symbol] = right_ptr

            if right_ptr - left_ptr + 1 > best_length:
                best_length = right_ptr - left_ptr + 1
                longest_substring_candidate = s[left_ptr:left_ptr+best_length]
                print(longest_substring_candidate)

            # move on right pointer
            right_ptr += 1

        return best_length
