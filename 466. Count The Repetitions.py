class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # s2_index = 0
        # s2_count = 0
        
        # for _ in range(n1):
        #     for ch in s1:
        #         if ch == s2[s2_index]:
        #             s2_index += 1
                    
        #             if s2_index == len(s2):
        #                 s2_index = 0
        #                 s2_count += 1
        
        # return s2_count // n2
        if not set(s2).issubset(set(s1)):
            return 0
        
        index = 0 # pointer for s2
        count_s2 = 0
        s1_count = 0      
        
        recall = {}# for cycle detection
        
        while s1_count < n1:
            s1_count += 1
            
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    
                    if index == len(s2):
                        index = 0
                        count_s2 += 1
            
            # cycle detection
            if index in recall:
                prev_s1_count, prev_s2_count = recall[index]
                
                cycle_s1 = s1_count - prev_s1_count
                cycle_s2 = count_s2 - prev_s2_count
                
                remaining = n1 - s1_count
                times = remaining // cycle_s1
                
                s1_count += times * cycle_s1
                count_s2 += times * cycle_s2
            else:
                recall[index] = (s1_count, count_s2)
        
        return count_s2 // n2
        