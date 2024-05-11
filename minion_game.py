def minion_game(s):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)