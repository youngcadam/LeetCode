class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = ""
        l = len(s)
        nrow = numRows

        if l <= nrow:
            return s
        
        elif nrow == 1:
            return s

        elif nrow == 2:
            return (s[0:l:2] + s[1:l:2])


        else:
            if l <= nrow:
                r = s

            else:
                # do first row
                n = nrow-1
                nm = 2*n
                row_1 = s[0:l:nm]
                row_n = s[n:l:nm]

                r = row_1
                for i in range(1, n):
                    row_i = s[i]
                    index = nm - i
                    while index < l:
                        row_i = (row_i + s[index:index+2*i+1:2*i])
                        index = index + nm
                    r = (r + row_i)

                r = (r + row_n)
            
            return r
