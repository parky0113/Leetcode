class Solution(object):    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def charcheck(fword,sword):
            fcheck = ""
            scheck = ""
                
            for i in range(len(fword)):
                if fcheck == scheck:
                    fcheck += fword[i]
                    scheck += sword[i]
                else:
                    return fcheck[:-1]
            if fcheck == scheck:
                return fcheck
            else:
                return fcheck[:-1]
        
        cword = strs[0]
            
        for i in range(1, len(strs)):
            if len(cword) >= len(strs[i]):
                cword = charcheck(strs[i], cword)
            else:
                cword = charcheck(cword, strs[i])
        return cword
            
            
            
    
