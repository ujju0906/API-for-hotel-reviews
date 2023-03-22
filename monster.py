class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
     # @return an list of long
    def solve(self, A, B):
        l = []
        flag = 1
       
            
        tot_monsters = 0
        for j in A:
            
               
            tot_monsters += (j[1]-j[0]) +1
        for i in B:
            count = 0
            for k in A:
                if i[1]>k[2]and i[0]<=k[1]and i[0]>=k[0]:
                    count+=1
            tot_monsters -= count
            l.append((tot_monsters))
        
    
            
                
            
           
               
        return l

