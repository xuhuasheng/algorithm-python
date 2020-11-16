def leftRotateString(s, n):
    return s[n:] + s[:n]

if __name__ == "__main__":
    s = "abcdefg"
    print(leftRotateString(s, 2))