def replaceBlank(s:str):
    s1 = s.split(' ')
    for i in range(len(s1)-1):
        s1[i] += "%20"
    res = ''
    for i in s1:
        res += i
    return res

if __name__ == "__main__":
    ss = "We are happy"
    print(replaceBlank(ss))
