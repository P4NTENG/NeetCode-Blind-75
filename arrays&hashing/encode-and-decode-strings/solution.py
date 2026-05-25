def encode(strs: List[str]) -> str:
    encoded_string = ""
    for s in strs:
        encoded_string += str(len(s)) + ':' + s

    print(encoded_string)
    return encoded_string

def decode(s: str) -> List[str]:
    decoded_strs = []

    while len(s) > 0:
        length = ""
        for i in range(0, len(s)):
            if s[i] == ':':
                break
            length += s[i]
        length = int(length)
        print(length)
        word = s[1+i:1+i+length]
        print(word)
        decoded_strs.append(word)
        s = s[length+1+i:]

    return decoded_strs

strs=["we","say",":","yes","!@#$%^&*()"]
encoded_string = encode(strs)
print(decode(encoded_string))