class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        j = 0
        ck =1
        while num not in [2,3,5]:
            for i in [2,3,5]:
                k = num % i
                if k == 0:
                    j = i
                ck = ck*k
            if ck != 0:
                return False
            num = num / j
        return True

c = Solution
c.isUgly(24)