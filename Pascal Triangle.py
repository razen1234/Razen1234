class Solution():
    def generate(self, numRows):
        # Creating an empty list for our pascal triangle
        triangle_pasc = []
        # Cycle for works only in range of "numRows"
        for i in range(numRows):
            #This line of code makes list full of 1 nums(example: i = 0: [1] ; i = 2: [1, 1, 1])
            row = [1]*(i + 1)
            # Cycle "for" to count middle elements
            for e in range(1, i):
                # "triangle_pasc[i - 1]" here is a previous line (example of counting: row[1] = 1 + 2; row[2] = 2 + 1 =3 ; now line is: [1, 3, 3, 1]) 
                row[e] = triangle_pasc[i - 1] [e - 1] + triangle_pasc[i - 1] [e]
            # Now adding line into triangle   
            triangle_pasc.append(row)
        # Returnig an answer    
        return triangle_pasc
