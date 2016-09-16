class  Solution(object):
    def  minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n =  len(triangle)
        for  i in  xrange(n -  2, - 1, - 1):
            for  j in  xrange(0, i +  1):
                triangle[i][j] +=  min(triangle[i +  1][j], triangle[i +  1][j +  1])
        return  triangle[0][0]
                    
