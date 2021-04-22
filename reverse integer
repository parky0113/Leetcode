#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        z = ""
        
        if x >= 0 :
            s = ""
        else:
            s = "-"
            x*=-1
                  
        x = str(x)
        for i in range(len(x)-1,-1,-1):
            s += x[i]
        if int(s) < -2**31 or int(s) > (2**31)-1:
            return 0
        return int(s)
