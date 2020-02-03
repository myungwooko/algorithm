def decodeVariations(S):
    d = {}
    # making dictionary
    for i in range(65, 65 + 26):
        ascii_char = chr(i)
        d[str(i - 64)] = ascii_char

    candidates = []
    def helper(S, acc):
        if S == "":
            candidates.append(acc)
            return
        curr = ""
        for i, v in enumerate(S):
            curr = curr + v
            if curr in d:
                helper(S[i + 1:], acc + [curr])
            else:
                break
    helper(S, [])
    print(candidates)
    return len(candidates)


test = decodeVariations("1269")
print(test)