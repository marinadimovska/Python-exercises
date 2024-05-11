def swap_case(s):
    sting_modified = ''
    for i in s:
        if i.upper() == i:  # upper case A -> a
            i = i.lower()
            sting_modified += i
        else:
            i = i.upper()
            sting_modified += i

    return sting_modified

s = input('')
print(f'{s} -> {swap_case(s)}')