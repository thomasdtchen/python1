def permutations(chars, i=0):
    """
    :param chars: characters to permute
    :param i: starting index of subarray of characters to permute. (default 0)
    :return:
    """
    chars_len = len(chars)
    #print("--------------------------------------------", chars)
    #print("i:", i, ",", "chars_len:", chars_len)
    if i == chars_len - 1:
        print(chars)
    #print("i:", i)
    for j in range(i, chars_len):
        #print("i:", i, ",", "j:", j)
        #print(chars[i], ",", chars[j])

        chars[i], chars[j] = chars[j], chars[i]

        #print(chars[i], ",", chars[j])

        permutations(chars, i+1)

        #print("---------")
        #print("i:", i, ",", "j:", j)
        #print(chars[i], ",", chars[j])

        chars[i], chars[j] = chars[j], chars[i]

        #print(chars[i], ",", chars[j])

target = ["c", "a", "t"]
permutations(target)