s = "abcabcbb"
length = len(s)
i = 0
count = 0
max_len = 0
letters = []
while i < length:
    for l in letters:
        if(s[i] == l):
            print(letters)
            if count > max_len:
                max_len = count
                i = i + 1 - count
                count = 0
                letters = []
                break
            i = i - count + 1
            letters = []
            count = 0
            break

    letters.append(s[i])
    i += 1
    count += 1
print(max_len)