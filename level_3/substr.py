# LEVEL 3:
#   Given a string, find the length of the longest substring without repeating characters.

#   Input: "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.

#   Input: "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.

#   Input: "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def substr(string):
    if len(string) == 0:
        return ''

    ss_letters = {}

    ss_idx_lo = 0
    ss_idx_hi = 0
    ss_letters[string[0]] = 1

    longest_ss = string[ss_idx_lo:1+ss_idx_hi]

    while (ss_idx_hi < len(string)-1):
        ss_idx_hi += 1
        next_char = string[ss_idx_hi]

        while next_char in ss_letters:
            ss_letters.pop(string[ss_idx_lo])
            ss_idx_lo += 1

        if len(string[ss_idx_lo:1+ss_idx_hi]) > len(longest_ss):
            longest_ss = string[ss_idx_lo:1+ss_idx_hi]

        ss_letters[next_char] = 1

    return longest_ss

if __name__ == '__main__':
    import sys
    print(substr(sys.argv[1]))
