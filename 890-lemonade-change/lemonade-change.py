class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5=0
        change10=0
        for i in range(len(bills)):
            if bills[i]==5:
                change5+=1
            elif bills[i]==10:
                change5-=1
                change10+=1
            else:
                if change10>0 :
                    change10-=1
                    change5-=1
                else:
                    change5-=3
            if change5<0 or change10<0:
                return False
        return True


        