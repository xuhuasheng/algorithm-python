def countBinarySubstrings(s: str) -> int:
    ls = list(map(int, list(s)))
    cnt = 0
    for i in range(len(ls)-1):
        num = 0
        for j in range(i, len(ls)):
            if ls[j] == 0:
                num += 1
            else:
                num -= 1
            if num == 0:
                cnt += 1
                break 
    return cnt

if __name__ == "__main__":
    s = "000111"
    print(countBinarySubstrings(s))