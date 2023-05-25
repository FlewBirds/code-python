def get_longest_substring(string):
    """
    Returns the longest substring that contains only unique characters
    """
    start = 0  # start index of the window
    end = 0  # end index of the window
    longest_substring = ""  # variable to store the longest substring found so far
    seen_chars = set()  # set to store the characters seen in the current window

    while end < len(string):  #  0 < 7
        if string[end] not in seen_chars:  # a
            seen_chars.add(string[end]) #a
            end += 1 # end = 1
            # update the longest substring if the current substring is longer
            if end - start > len(longest_substring): # 0 - 0 > 0
                longest_substring = string[start:end] # a
        else:
            seen_chars.remove(string[start])
            start += 1

    return longest_substring

string = "abcabcbb"
longest_substring = get_longest_substring(string)
print(longest_substring)  # output: "abc"