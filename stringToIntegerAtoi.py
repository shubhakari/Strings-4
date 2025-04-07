class Solution(object):
    # TC : O(n) - n is length of string
    # SC : O(1)
    def myAtoi(self, s):
        num = '0123456789'
        res = ''
        for x in s:
            if x == ' ' and len(res) == 0:
                continue
            if x != ' ' and (x in '-+' or x in num) and len(res) == 0:
                res += x
            elif x in num:
                res += x
            else:
                break
        if res == '' or res in '-+':
            return 0
        else:
# to avoid int casting simply run a loop and use ord(char) - ord('0')
            if int(res) < -(2**31):
                return -(2**31)
            elif int(res) > (2**31 - 1):
                return (2**31 - 1)
            else:
                return int(res)