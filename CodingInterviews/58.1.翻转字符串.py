# 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
# 同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
# 例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
# Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

def reverse(s):
    ss = s.split(' ')
    ss.reverse()
    return ' '.join(ss)


if __name__ == "__main__":
    word = "word"
    sen = " I am a student."
    print(reverse(sen))

def reverseWord(word):
    if word is None or len(word) == 0:
        return
    w = list(word)
    left = 0
    right = len(w) - 1
    while left < right:
        w[left], w[right] = w[right], w[left]
        left += 1
        right -= 1
    return ''.join(w)

# void Reverse(char *pBegin, char *pEnd) {
#     if (pBegin == nullptr || pEnd == nullptr) {
#         return;
#     }
#     while (pBegin < pEnd) {
#         char temp = *pBegin;
#         *pBegin = *pEnd;
#         *pEnd = temp;
#         pBegin ++;
#         pEnd ++;
#     }
# }

# char* ReverseSentence(char *pData) {
#     if (pData == nullptr)
#         return nullptr;
#     char *pBegin = pData;
#     char *pEnd = pData;
#     while (*pEnd != '\0')
#         pEnd ++;
#     pEnd --;
#     Reverse(pBegin, pEnd);
#     pBegin = pEnd = pData;
#     while (*pBegin != '\0') {
#         if (*pBegin == ' ') {
#             pBegin ++;
#             pEnd ++;
#         }
#         else if (*pEnd == ' ' || *pEnd == '\0') {
#             Reverse(pBegin, --pEnd);
#             pBegin = ++pEnd;
#         }
#         else 
#             pEnd ++;
#     }
#     return pData;
# }

    

