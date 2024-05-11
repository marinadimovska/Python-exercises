def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        sub_str = string[i:i+k]
        unique_chars = []
        for char in sub_str:
            if char not in unique_chars:
                unique_chars.append(char)
        print(''.join(unique_chars))


s = input('')
k = input('')
merge_the_tools(s, k)
