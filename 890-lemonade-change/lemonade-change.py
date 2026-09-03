class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        
        count_5=0
        count_10=0
        count_20=0
        for x in bills:
            if x==5:
                count_5+=1
            elif x==10:
                if count_5>=1:
                    count_10+=1
                    count_5-=1
                else:
                    return False
            else:
                if count_5>=1 and count_10>=1:
                    count_20+=1
                    count_5-=1
                    count_10-=1
                elif count_5>=3:
                    count_20+=1
                    count_5-=3
                else:
                    return False
        return True
