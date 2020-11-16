import itertools
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
         
        '''1.空数组返回空串；
        2.将数组中的数字转化为字符串；
        3.字符串拼接后的字典排序；
        4.拼接返回；'''
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        ret=[]
        for i in itertools.permutations(numbers,len(numbers)):
            ret.append(''.join(i).lstrip('0'))
        ret.sort()
        return ret[0]

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if int(str(numbers[i])+str(numbers[j])) > int(str(numbers[j])+str(numbers[i])):
                    numbers[i],numbers[j] = numbers[j],numbers[i]
        return "".join([str(i) for i in numbers])